#!/bin/bash

# 첫 번째 명령 실행
echo "로봇을 시작합니다..."
cd ~/final_project/ros-repo-4/MFC_Robot/
source install/local_setup.bash
ros2 launch minibot_bringup bringup_robot.launch.py
# echo "로봇이 성공적으로 시작되었습니다."

# # 두 번째 명령 실행
# echo "Navigation2 맵을 시작합니다..."
# cd ~/final_project/ros-repo-4/MFC_Robot/
# source install/local_setup.bash
# cd ~/final_project/maps/
# ros2 launch minibot_navigation2 bringup_launch.py map:=mfc_map.yaml
# echo "Navigation2 맵이 성공적으로 실행되었습니다."
