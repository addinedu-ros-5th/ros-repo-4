from launch import LaunchDescription
# from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # use_sim_time = LaunchConfiguration('use_sim_time')
    
    return LaunchDescription([
        Node(
            package='lrobot',
            executable='path_server',
            name='path_server',
            output='screen',
            parameters=[
                {
                    'use_sim_time': False
                }
            ]
        )
    ])
