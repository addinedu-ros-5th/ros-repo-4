# import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # map_dir = os.path.join(get_package_share_directory('lrobot'), 'maps')

    return LaunchDescription([
        # Node(
        #     package='lrobot',
        #     executable='robot_controller',
        #     name='robot_controller',
        #     output='screen',
        #     parameters=[{'map_yaml_path': os.path.join(map_dir, 'main.yaml')}],
        #     arguments=['--ros-args', '--log-level', 'debug']
        # ),
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
