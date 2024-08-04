from setuptools import setup

package_name = 'robot_state'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[
        'robot_state.robotgoal_test',
        'robot_state.robotgoal',
        'robot_state.test_amcl_subscriber',
        'robot_state.robot_state_manager_node'
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='edu',
    maintainer_email='heagon72@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_state_manager_node = robot_state.robot_state_manager_node:main',
            'robot_task_client = robot_state.robot_task_client:main',                #new
            'robot_task_server = robot_state.robot_task_server:main',                #new
        ],
    },
)
