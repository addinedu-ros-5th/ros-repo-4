#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


from task_manager.msg import DbUpdate, GuiUpdate
from task_manager.msg import StartInspection, InspectionComplete, SendAllocationResults
from task_manager.srv import GenerateOrder, AllocatorTask
from modules.order_grouping import group_items
from modules.order_list import OrderList  
from robot_state.srv import UpdateDB

import mysql.connector as con

class OrderListService(Node):
    def __init__(self):

        super().__init__('order_list_service')
        # 'GenerateOrder' 메세지 타입의 서비스 서버
        self.srv = self.create_service(GenerateOrder, 'generate_order', self.generate_order_callback)
        self.order_list_node = OrderList()
        self.grouped_items = []

        self.inspection_started = False  # 플래그 변수 초기화
        self.inspection_index = 0  # 검수 진행 중인 아이템 인덱스
        self.total_items_to_inspect = 0
        self.inspected_items_count = 0
        self.current_task_code = None # 현재 그룹의 task_code를 저장할 변수 추가
        self.product_code_list = []  # 현재 그룹의 product_code 리스트를 저장할 변수 추가



        # list gui가 db에 저장완료했다고 신호받고 첫행 꺼내오기
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

        # 아이템 ID 리스트 생성
        order_list = [item.item_id for item in random_items]

        # 그룹핑된 아이템 목록 생성
        grouped_items = group_items(order_list)

        task_code = 1
        for group in grouped_items:
            for product_code in group:
                self.grouped_items.append((task_code,product_code))
            task_code += 1

        # 그룹핑된 아이템 목록 출력 (디버깅용)
        for i, (task,item) in enumerate(self.grouped_items):
            print(f"Task_{task}: {item}")

        product_to_location = {
            "P01": "R_A1", "P02": "R_A2", "P03": "R_A3",
            "P04": "R_B1", "P05": "R_B2", "P06": "R_B3",
            "P07": "R_C1", "P08": "R_C2", "P09": "R_C3",
            "P10": "R_D1", "P11": "R_D2", "P12": "R_D3",
            "P13": "R_E1", "P14": "R_E2", "P15": "R_E3",
            "P16": "R_F1", "P17": "R_F2", "P18": "R_F3",
        }

        warehouses = []
        racks = []
        cells = []

        for item in random_items:
            location = product_to_location.get(item.item_id, "R_A1")  # 기본값으로 "R_A1" 설정
            warehouse, rack, cell = location.split("_")[1][0], location.split("_")[1], location.split("_")[1][1]
            
            warehouses.append(f"{warehouse}구역")
            racks.append(rack)
            cells.append(cell)
        
        response.item_ids = [str(item.item_id) for item in random_items]
        response.names = [item.name for item in random_items]
        response.quantities = [item.quantity for item in random_items]
        response.warehouses = warehouses
        response.racks = racks
        response.cells = cells
        response.statuses = ["입하완료" for _ in random_items]  # 임의로 Status 설정
        
        # self.get_logger().info(f'Received request: {request}')
        # self.get_logger().info(f'Sending response: {response}')
   
        return response



    def db_update_callback(self, msg):
        self.get_logger().info(f'Received DB update status: {msg.status}')
        if msg.status == "DB Update Completed" and not self.inspection_started:
            self.inspection_started = True
            self.get_items_to_inspect()
            self.process_next_item()
            
    def send_signal_start_inspection_to_mfc(self, product):
        self.inspection_started = False  # 신호 전송 후 플래그 설정
        msg = StartInspection()
        msg.product_code = product["Product_Code"]
        msg.product_name = product["Product_Name"]
        self.publisher_start_inspection.publish(msg)
        self.get_logger().info(f'Sending inspection start signal for {product["Product_Name"]}')

    
    def get_items_to_inspect(self):
        db_connection = Connect("team4", "0444")
        cursor = db_connection.cursor
        cursor.execute("SELECT COUNT(*) FROM Inbound_Manager WHERE Status = '입하완료'")
        self.total_items_to_inspect = cursor.fetchone()[0]
        self.get_logger().info(f"Total item at index { self.total_items_to_inspect}")
        db_connection.disConnection()

    def process_next_item(self):
        if self.inspection_index < len(self.grouped_items):
            task_code, item_id = self.grouped_items[self.inspection_index]
            if self.current_task_code != task_code:
                self.current_task_code = task_code
                self.product_code_list = []
            self.product_code_list.append(item_id)
            product = self.get_item_from_db(item_id)
            if product:
                self.send_signal_start_inspection_to_mfc(product)
                self.inspection_index += 1
        else:
            self.inspection_started = False
            self.get_logger().info('No more items to inspect.')

    def get_item_from_db(self, item_id):
        db_connection = Connect("team4", "0444")
        cursor = db_connection.cursor
        cursor.execute("SELECT * FROM Inbound_Manager WHERE Product_Code = %s", (item_id,))
        row = cursor.fetchone()
        self.get_logger().info(f"Fetched row from DB for Product_Code {item_id}: {row}")
        db_connection.disConnection()
        
        if row:
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
            return product
        return None
    

    def inspection_complete_callback(self, msg):
        self.get_logger().info(f'Inspection complete for product: {msg.product_code}')
        self.update_status_in_db(msg.product_code, '검수완료')
        self.send_update_signal_to_gui(msg.product_code, '검수완료')

        self.inspected_items_count += 1

        # 다음 인덱스가 현재 작업 코드와 다를 경우
        if (self.inspection_index < len(self.grouped_items) and self.grouped_items[self.inspection_index][0] != self.current_task_code):
            self.send_task_allocation_request(self.current_task_code, self.product_code_list,"입고")
            self.product_code_list = [] #list초기화

        # 모든 검수가 완료되었을 경우
        if self.inspected_items_count == self.total_items_to_inspect:
            self.get_logger().info('All inspections complete. Sending task allocation requests.')
            self.send_task_allocation_request(self.current_task_code, self.product_code_list,"입고")

        # else:
        self.process_next_item()


        
    def update_status_in_db(self, product_code, status):        
        db_connection = Connect("team4", "0444")
        if not db_connection.conn or not db_connection.cursor:
            self.get_logger().error("Failed to connect to the database")
            return

        try:
            cursor = db_connection.cursor
            cursor.execute("UPDATE Inbound_Manager SET Status = %s WHERE Product_Code = %s", (status, product_code))
            db_connection.conn.commit()
            self.get_logger().info(f'Status for product {product_code} updated to {status} in DB')
        except con.Error as err:
            self.get_logger().error(f"Error: {err}")
        finally:
            db_connection.disConnection()


    def send_update_signal_to_gui(self, product_code, status):
        msg = GuiUpdate()
        msg.product_code = product_code
        msg.status = status
        msg.message = f"Product {product_code} status updated to {status}"
        self.publisher_update_gui.publish(msg)
        self.get_logger().info(f'Sent GUI update signal for product {product_code} with status {status}')


    def send_task_allocation_request(self,  task_code, product_code_list,task_type):
        request = AllocatorTask.Request()
        request.task_code = f"Task_{task_code}"
        request.product_code_list = product_code_list
        request.task_type = task_type
        self.future = self.task_allocator_client.call_async(request)
        self.get_logger().info(f'Sending task allocation request for task_code: task_{task_code} with product_code_list: {product_code_list}')
        self.future.add_done_callback(self.handle_task_allocation_response)

    
    def handle_task_allocation_response(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Robot Name: {response.robot_name}')
            self.get_logger().info(f'Task Code: {response.task_code}')
            self.get_logger().info(f'Goal Location: {response.rack_list}')
            self.get_logger().info(f'Task Assignment: {response.task_assignment}')
            self.send_task_allocation_results(response.robot_name,response.task_code,response.rack_list,response.task_assignment)

        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

    def send_task_allocation_results(self, robot_name,task_code,rack_list,task_assignment):
        allocation_msg = SendAllocationResults()
        allocation_msg.robot_name = robot_name
        allocation_msg.task_code = task_code
        allocation_msg.rack_list= rack_list
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