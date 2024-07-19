from setuptools import find_packages, setup

package_name = 'aruco_detector_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/calib_data', ['calib_data/MultiMatrix.npz']),
        ('share/' + package_name + '/launch', ['launch/aruco_cmd_vel_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mk',
    maintainer_email='mk@todo.todo',
    description='Package for detecting ArUco markers and estimating robot pose.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'aruco_pose_estimate = aruco_detector_pkg.aruco_pose_estimate:main',
            'pose_to_goal = aruco_detector_pkg.pose_to_goal:main',
            'cmd_vel_relay = aruco_detector_pkg.cmd_vel_relay:main',
        ],
    },
)
