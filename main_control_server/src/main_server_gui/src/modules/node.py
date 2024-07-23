import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from task_manager.srv import GenerateOrder
from task_manager.msg import DbUpdate, GuiUpdate


from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot


from modules.robotstatewindow import *
from modules.mainwindow import *

class InboundNode(Node):
    def __init__(self, main_window):
        super().__init__('inbound_node')
        self.client = self.create_client(GenerateOrder, 'generate_order')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.get_logger().info('Service available, ready to send request.')

        self.publisher = self.create_publisher(DbUpdate, 'db_update_status', 10)

        self.subscription_update = self.create_subscription(
            GuiUpdate,
            'gui_update',
            self.gui_update_callback,
            10)

        self.main_window = main_window

        # 8시가 되면은 종이 울린다~
        self.main_window.schedule_signal.connect(self.request_inbound_list)
        self.main_window.db_update_signal.connect(self.notify_db_update_complete)  # GUI에서 신호 연결


    def request_inbound_list(self):
        if not self.client:
            self.get_logger().error('Client not initialized')
            return
        request = GenerateOrder.Request()
        try:
            future = self.client.call_async(request)
            future.add_done_callback(self.inbound_list_callback)
            self.get_logger().info('Async request sent')
        except Exception as e:
            self.get_logger().error(f'Failed to send async request: {e}')

    def inbound_list_callback(self, future):
        self.get_logger().info('inbound_list_callback called')
        try:
            response = future.result()
            self.get_logger().info(f'Received response: {response}')
            inbound_list = [{
                "item_id": response.item_ids[i],
                "name": response.names[i],
                "quantity": response.quantities[i],
                "warehouse": response.warehouses[i],
                "rack": response.racks[i],
                "cell": response.cells[i],
                "status": response.statuses[i]
            } for i in range(len(response.item_ids))]
            
            self.get_logger().info(f'Parsed inbound list: {inbound_list}')
            # GUI로 signal 발행
            self.main_window.inbound_list_signal.emit(inbound_list)
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

    def notify_db_update_complete(self, status_message):
        msg = DbUpdate()
        msg.status = status_message
        self.publisher.publish(msg)
        self.get_logger().info('Published DB update status')

    def gui_update_callback(self, msg):
        self.get_logger().info(f'GUI Update signal received for product {msg.product_code} with status {msg.status}')
        self.main_window.inbound_status_db_update_signal.emit()


    


class AmclSubscriber(Node):
    def __init__(self, robot_state_window):
        super().__init__('amcl_subscriber')
        self.robot_state_window = robot_state_window
        self.pose1_sub = self.create_subscription(PoseWithCovarianceStamped, 'amcl_pose', self.amcl_callback1, 10)

    def amcl_callback1(self, amcl):
        global amcl_1
        amcl_1 = amcl
        print(amcl_1)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        self.robot_state_window.update_amcl_pose(amcl) #예시??
