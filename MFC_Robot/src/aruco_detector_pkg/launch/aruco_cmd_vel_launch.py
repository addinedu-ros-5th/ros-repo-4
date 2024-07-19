import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='aruco_detector_pkg',
            executable='aruco_pose_estimate',
            name='aruco_pose_estimate_node',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='aruco_detector_pkg',
            executable='cmd_vel_relay',
            name='cmd_vel_relay_node',
            output='screen'
        ),
    ])
