from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='network_manager',
            executable='communication_robot_node.py',
            name='communication_robot_node',
            output='screen'
        ),
    ])