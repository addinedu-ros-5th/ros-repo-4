from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='main_server_gui',
            executable='main_server_gui.py',
            name='InboundNode',
            output='screen'
        ),

        Node(
            package='task_manager',
            executable='task_manager_node.py',
            name='OrderListService',
            output='screen'
        ),
        
        Node(
            package='network_manager',
            executable='communication_MFC_arduino.py',
            name='MFCNetworkManager',
            output='screen'
        ),
        Node(
            package='task_allocator',
            executable='task_allocator_node.py',
            name='TaskAllocator',
            output='screen'
        ),
        Node(
            package='robot_state',
            executable='robot_state_manager_node.py',
            name='TellTaskManager',
            output='screen'
        ),

    ])
