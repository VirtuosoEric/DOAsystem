#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import requests

class WebPublisher(Node):
    def __init__(self):
        super().__init__('direction_publisher')
        # Create a publisher for the 'web_value' topic.
        self.publisher_ = self.create_publisher(Int32, 'DOA', 10)
        # Fetch and publish every 5 seconds.
        timer_period = 1.0  
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        try:
            # Replace the URL with your web server's endpoint.
            response = requests.get("http://127.0.0.1:5000/update")
            response.raise_for_status()
            # Parse the JSON response.
            json_data = response.json()
            # Extract the integer value from the JSON using the appropriate key.
            value = int(json_data["data"])
            msg = Int32()
            msg.data = value
            self.publisher_.publish(msg)
            self.get_logger().info(f"Published: {value}")
        except Exception as e:
            self.get_logger().error(f"Error fetching or publishing data: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = WebPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
