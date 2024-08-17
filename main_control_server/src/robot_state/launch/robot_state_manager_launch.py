from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_state',
            executable='robot_state_manager_node.py',
            name='robot_state_manager_node',
            output='screen'
        ),
    ])
