from launch import LaunchDescription
# from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # use_sim_time = LaunchConfiguration('use_sim_time')

    return LaunchDescription([
        Node(
            package='lrobot',
            executable='robot_drive',
            name='robot_drive',
            output='screen',
            parameters=[{
                'use_sim_time': False,
                'queue_size': 100 
            }]
        )
    ])
