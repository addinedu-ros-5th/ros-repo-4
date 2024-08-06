from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='lrobot',
            executable='robot_drive',
            name='robot_drive',
            output='screen',
            parameters=[{
                'use_sim_time': False 
            }]
        )
    ])
