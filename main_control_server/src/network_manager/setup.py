from setuptools import setup

package_name = 'network_manager'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='min',
    maintainer_email='6648kmk@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'communication_robot_node = network_manager.communication_robot_node:main',
            'communication_MFC_arduino = network_manager.communication_MFC_arduino:main',
        ],
    },
)
