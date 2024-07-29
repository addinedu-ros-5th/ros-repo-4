cmake_minimum_required(VERSION 3.8)
project(robot_state)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(rosidl_default_generators REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)                  # new
find_package(network_manager REQUIRED)                # new
find_package(robot_state REQUIRED)                    # new
find_package(task_manager REQUIRED)                   # new

# Install Python modules
#ament_python_install_package(${PROJECT_NAME})

# Install Python executables
install(
  PROGRAMS src/robotgoal_test.py
  PROGRAMS src/robotgoal.py
  PROGRAMS src/test_amcl_subscriber.py
  PROGRAMS src/robot_state_manager_node.py 
  PROGRAMS src/robot_task_server.py                  # new    
  PROGRAMS src/robot_task_client.py                  # new              
  DESTINATION lib/${PROJECT_NAME}
  PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
              GROUP_EXECUTE GROUP_READ
              WORLD_EXECUTE WORLD_READ
)

# Add the service files
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/UpdateDB.srv"
  "action/RobotTask.action"                          # new
  "msg/RobotState.msg"                               # new
)

# Install Python modules
install(
  DIRECTORY src/data
  DESTINATION lib/${PROJECT_NAME}
  FILES_MATCHING PATTERN "*.py"
)

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# Install Python modules
install(
  DIRECTORY src/modules
  DESTINATION lib/${PROJECT_NAME}
  FILES_MATCHING PATTERN "*.py"
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
