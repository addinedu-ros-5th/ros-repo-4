#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from order_list import OrderList  

from task_manager.msg import DbUpdate, GuiUpdate
from task_manager.msg import StartInspection, InspectionComplete, SendAllocationResults
from task_manager.srv import GenerateOrder, AllocatorTask
from robot_state.srv import UpdateDB

import sqlite3
import mysql.connector as con

class OrderListService(Node):
    def __init__(self):
        super().__init__('order_list_service')
        # 'GenerateOrder' 메세지 타입의 서비스 서버
        self.srv = self.create_service(GenerateOrder, 'generate_order', self.generate_order_callback)
        self.order_list_node = OrderList()

        self.inspection_started = False  # 플래그 변수 초기화
        self.inspection_index = 0  # 검수 진행 중인 아이템 인덱스

        # ???????용도????????
        self.subscription = self.create_subscription(
            DbUpdate,
            'db_update_status',
            self.db_update_callback,
            10)
        self.subscription 

        # 'StartInspection' 메세지 타입의 publisher
        self.publisher_start_inspection = self.create_publisher(StartInspection, 'mfc_start_inspection', 10)

        # 'InspectionComplete' 메세지 타입의 subscriber
        self.subscription_inspection_complete = self.create_subscription(
            InspectionComplete,
            'inspection_complete',
            self.inspection_complete_callback,
            10)
        
        # 'GuiUpdate' 메세지 타입의 publisher
        self.publisher_update_gui = self.create_publisher(GuiUpdate, 'gui_update', 10)        

        # 'AllocatorTask' 메세지 타입의 서비스 클라이언트 
        self.task_allocator_client = self.create_client(AllocatorTask, 'allocate_task')
        while not self.task_allocator_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('allocate_task service not available, waiting again...')
        self.get_logger().info('allocate_task service available.')

        # 'SendAllocationResults' 메세지 타입의 publisher
        self.publisher_allocation_results = self.create_publisher(SendAllocationResults, 'send_allocation_results', 10)

        # 'UpdateDB' 서비스 타입의 클라이언트
        self.client = self.create_client(UpdateDB, 'update_db')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('UpdateDB Service not available, waiting again...')
        self.get_logger().info('UpdateDB Service available, ready to send request.')

        self.updateDB_client()

    def updateDB_client(self):
        if not self.client:
            self.get_logger().error('Client not initialized')
            return
    
        request = UpdateDB.Request()

        # 'UpdateDB' 서비스 Request 메세지 타입: Robot_Name
        request.robot_name = "Robo1"                      # 디버깅용
        future = self.client.call_async(request)       
        future.add_done_callback(self.callback_response)  # 응답 콜백 설정

    def callback_response(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Received response: \n{response.robot_name}, {response.status}, {response.battery_status} ')
        except Exception as e:
            self.get_logger().error(f'Failed to receive response: {e}')

    def generate_order_callback(self, request, response):
        random_items = self.order_list_node.get_random_order_list()  # 랜덤 주문 리스트 생성

        response.item_ids = [str(item.item_id) for item in random_items]
        response.names = [item.name for item in random_items]
        response.quantities = [item.quantity for item in random_items]
        response.warehouses = ["A구역" for _ in random_items]  # 임의로 Warehouse 설정
        response.racks = ["A-1" for _ in random_items]  # 임의로 Rack 설정
        response.cells = ["2" for _ in random_items]  # 임의로 Cell 설정
        response.statuses = ["입하완료" for _ in random_items]  # 임의로 Status 설정
        
        self.get_logger().info(f'Received request: {request}')
        self.get_logger().info(f'Sending response: {response}')
        
        return response

    def db_update_callback(self, msg):
        self.get_logger().info(f'Received DB update status: {msg.status}')
        if msg.status == "DB Update Completed" and not self.inspection_started:
            self.inspection_started = True
            self.get_first_item_from_db()
            
    def send_signal_start_inspection_to_mfc(self, product):
        self.inspection_started = False  # 신호 전송 후 플래그 설정
        msg = StartInspection()
        msg.product_code = product["Product_Code"]
        msg.product_name = product["Product_Name"]
        self.publisher_start_inspection.publish(msg)
        self.get_logger().info(f'Sending inspection start signal for {product["Product_Name"]}')

    
    def get_first_item_from_db(self):
        # DB에서 첫 번째 항목 가져오기
        db_connection = Connect("team4", "0444")
        cursor = db_connection.cursor
        cursor.execute("SELECT * FROM Inbound_Manager WHERE Status = '입하완료' ORDER BY No LIMIT 1")
        row = cursor.fetchone()
        db_connection.disConnection()
        
        if row:
            self.get_logger().info(f"Fetched row from DB: {row}")  # 디버깅을 위해 추가
            product = {
                "No": row[0],
                "Product_Code": row[1],
                "Product_Name": row[2],
                "Warehouse": row[3],
                "Rack": row[4],
                "Cell": row[5],
                "Receiving_Quant": row[6],
                "Status": row[7]
            }
            self.get_logger().info(f"First row in Inbound List: {product}")
            self.send_signal_start_inspection_to_mfc(product)
        else:
            self.inspection_started = False
            self.get_logger().info('No items to inspect.')


    def inspection_complete_callback(self, msg):
        self.get_logger().info(f'Inspection complete for product: {msg.product_code}')
        self.update_status_in_db(msg.product_code, '검수완료')
        self.send_update_signal_to_gui(msg.product_code,'검수완료')
        self.send_task_allocation_request(msg.product_code,"입고")

        
    def update_status_in_db(self, product_code, status):
        db_connection = Connect("team4", "0444")
        cursor = db_connection.cursor
        cursor.execute("UPDATE Inbound_Manager SET Status = %s WHERE Product_Code = %s", (status, product_code))
        db_connection.conn.commit()
        db_connection.disConnection()
        self.get_logger().info(f'Status for product {product_code} updated to {status} in DB')


    def send_update_signal_to_gui(self, product_code, status):
        msg = GuiUpdate()
        msg.product_code = product_code
        msg.status = status
        msg.message = f"Product {product_code} status updated to {status}"
        self.publisher_update_gui.publish(msg)
        self.get_logger().info(f'Sent GUI update signal for product {product_code} with status {status}')


    def send_task_allocation_request(self, product_code,task_type):
        request = AllocatorTask.Request()
        request.product_code = product_code
        request.task_type = task_type
        self.future = self.task_allocator_client.call_async(request)
        self.get_logger().info(f'Sending task allocation request for product_code: {product_code} with task_type: {task_type}')
        self.future.add_done_callback(self.handle_task_allocation_response)

    
    def handle_task_allocation_response(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Robot Name: {response.robot_name}')
            self.get_logger().info(f'Goal Location: {response.goal_location}')
            self.get_logger().info(f'Task Assignment: {response.task_assignment}')
            self.send_task_allocation_results(response.robot_name,response.goal_location,response.task_assignment)

        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

    def send_task_allocation_results(self, robot_name,goal_location,task_assignment):
        allocation_msg = SendAllocationResults()
        allocation_msg.robot_name = robot_name
        allocation_msg.goal_location = goal_location
        allocation_msg.task_assignment = task_assignment
        self.publisher_allocation_results.publish(allocation_msg)
        
        self.get_logger().info(f'Published task assignment for robot: {robot_name}')


class Connect():
    def __init__(self, User, Password):
        self.conn = con.connect(
            host='database-1.cdigc6umyoh0.ap-northeast-2.rds.amazonaws.com',
            user=User,
            password=Password,
            database='DFC_system_db'
        )
        self.cursor = self.conn.cursor(buffered=True)

    def disConnection(self):
        if self.conn:
            print('!!!!!!DB SHUT DOWN!!!!!!')
            self.conn.close()
            self.cursor.close()
            self.conn = None

def main(args=None):
    rclpy.init(args=args)
    order_list_service = OrderListService()

    rclpy.spin(order_list_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
