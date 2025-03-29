# Use the official ROS2 Humble image (ensure it supports your ARM architecture)
FROM ros:humble-ros-base

# Optional: Set environment variables (e.g., for ROS_DOMAIN_ID if needed)
ENV ROS_DOMAIN_ID=0

# Set a working directory
WORKDIR /workspace

# The default command will source ROS2 and start a bash shell
CMD ["bash", "-c", "source /opt/ros/humble/setup.bash && bash"]