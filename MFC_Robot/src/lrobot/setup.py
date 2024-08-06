import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'lrobot'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.py')),
        (os.path.join('share', package_name, 'msg'), glob('msgs/*.msg')),
        ('share/' + package_name + '/maps', glob('maps/*')),
    ],
    install_requires=['setuptools', 'robot_state'],
    zip_safe=True,
    maintainer='ys',
    maintainer_email='ysu0415@gmail.com',
    description='lrobot package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_drive = lrobot.robot_drive:main',
            'robot_state_action_client_node = lrobot.robot_state_action_client:main',
            'robot_control = lrobot.robot_control:main',
            'path_server = lrobot.path_server:main',
        ],
    },
)
