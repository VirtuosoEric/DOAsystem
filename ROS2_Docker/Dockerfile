# Use the official ROS2 Humble base image.
FROM ros:humble-ros-base

# Set the working directory in the container.
WORKDIR /workspace

# Copy the publisher script from the host into the container.
COPY ./app/publisher.py /workspace/publisher.py

# Install pip and the 'requests' library.
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install requests

# Make the script executable.
RUN chmod +x publisher.py

# When the container starts, source the ROS2 setup and run the publisher.
CMD ["bash", "-c", "source /opt/ros/humble/setup.bash && python3 publisher.py"]
