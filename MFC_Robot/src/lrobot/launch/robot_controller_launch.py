# import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # map_dir = os.path.join(get_package_share_directory('lrobot'), 'maps')

    return LaunchDescription([
        Node(
            package='lrobot',
            executable='robot_control',
            name='robot_control',
            output='screen',
            parameters=[{
                'use_sim_time': True 
            }]
        )
    ])
