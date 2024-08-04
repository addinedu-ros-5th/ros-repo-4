#!/bin/bash

# 첫 번째 명령 실행
echo "로봇을 시작합니다..."
cd ~/final_project/ros-repo-4/MFC_Robot/
source install/local_setup.bash
ros2 launch minibot_bringup bringup_robot.launch.py