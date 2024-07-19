# Use the official ROS 2 Humble base image
FROM ros:humble

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-opencv \
    python3-colcon-common-extensions \
    python3-rosdep \
    ros-humble-cv-bridge \
    && rm -rf /var/lib/apt/lists/*

# Install ultralytics (YOLOv5)
RUN pip3 install ultralytics

# Initialize rosdep if not already initialized
RUN if [ ! -f /etc/ros/rosdep/sources.list.d/20-default.list ]; then \
        rosdep init; \
    fi && \
    rosdep update

# Copy the ROS 2 package to the Docker image
COPY ai_server /ros2_ws/src/ai_server

# Install ROS 2 dependencies and build the workspace
RUN . /opt/ros/humble/setup.sh && \
    cd /ros2_ws && \
    rosdep install --from-paths src --ignore-src -r -y --skip-keys="ultralytics" && \
    colcon build

# Source the ROS 2 setup script
RUN echo ". /opt/ros/humble/setup.sh" >> ~/.bashrc
RUN echo ". /ros2_ws/install/setup.bash" >> ~/.bashrc

# Set the entrypoint
# ENTRYPOINT ["ros2", "launch", "ai_server", "detection_launch.py"]
