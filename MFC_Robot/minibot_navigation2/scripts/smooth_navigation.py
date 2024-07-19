import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Quaternion
from visualization_msgs.msg import Marker, MarkerArray
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
import math

class SmoothNavigation(Node):
    def __init__(self):
        super().__init__('smooth_navigation')
        self.navigation_client = ActionClient(self, NavigateToPose, '/navigate_to_pose')
        self.marker_publisher = self.create_publisher(MarkerArray, '/waypoint_markers', 10)
        self.current_goal = None

    def send_goal(self, x, y, theta):
        goal_msg = PoseStamped()
        goal_msg.header.frame_id = 'map'
        goal_msg.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.position.x = x
        goal_msg.pose.position.y = y
        goal_q = quaternion_from_euler(0, 0, theta)
        goal_msg.pose.orientation = Quaternion(x=goal_q[0], y=goal_q[1], z=goal_q[2], w=goal_q[3])

        goal_pose = NavigateToPose.Goal()
        goal_pose.pose = goal_msg

        self.navigation_client.wait_for_server()
        send_goal_future = self.navigation_client.send_goal_async(goal_pose)
        send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')
        self.current_goal = goal_handle
        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        if result:
            self.get_logger().info('Goal succeeded!')
        else:
            self.get_logger().info('Goal failed :(')
        self.current_goal = None
        self.get_logger().info('Navigating to the next waypoint...')

    def follow_waypoints(self, waypoints):
        marker_array = MarkerArray()
        for i, waypoint in enumerate(waypoints):
            marker = Marker()
            marker.header.frame_id = 'map'
            marker.header.stamp = self.get_clock().now().to_msg()
            marker.ns = 'waypoints'
            marker.id = i
            marker.type = Marker.SPHERE
            marker.action = Marker.ADD
            marker.pose.position.x = waypoint[0]
            marker.pose.position.y = waypoint[1]
            marker.pose.position.z = 0.0
            marker.pose.orientation.w = 1.0
            marker.scale.x = 0.2
            marker.scale.y = 0.2
            marker.scale.z = 0.2
            marker.color.a = 1.0
            marker.color.r = 1.0
            marker.color.g = 0.0
            marker.color.b = 0.0
            marker_array.markers.append(marker)
        
        self.marker_publisher.publish(marker_array)
        
        for waypoint in waypoints:
            self.send_goal(*waypoint)
            self.get_logger().info(f"Navigating to waypoint: {waypoint}")
            rclpy.spin_until_future_complete(self, self.current_goal.get_result_async())
            if not self.current_goal:
                break

def quaternion_from_euler(roll, pitch, yaw):
    """Convert Euler angles to quaternion."""
    q = [0.0, 0.0, 0.0, 0.0]
    t0 = math.cos(yaw * 0.5)
    t1 = math.sin(yaw * 0.5)
    t2 = math.cos(roll * 0.5)
    t3 = math.sin(roll * 0.5)
    t4 = math.cos(pitch * 0.5)
    t5 = math.sin(pitch * 0.5)

    q[0] = t0 * t2 * t4 + t1 * t3 * t5
    q[1] = t0 * t3 * t4 - t1 * t2 * t5
    q[2] = t0 * t2 * t5 + t1 * t3 * t4
    q[3] = t1 * t2 * t4 - t0 * t3 * t5

    return q

def main(args=None):
    rclpy.init(args=args)
    navigator = SmoothNavigation()

    # 절대 좌표로 웨이포인트 설정 (x, y, theta)
    waypoints = [
        (1.0, 1.0, 0.0),
        (2.0, 1.0, 0.0),
        (2.0, 2.0, math.pi/2),
        (1.0, 2.0, math.pi)
    ]

    navigator.follow_waypoints(waypoints)
    rclpy.spin(navigator)

    navigator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
