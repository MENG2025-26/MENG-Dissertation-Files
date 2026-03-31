# Author : Tony Willett
# Date :   31st March 2026
# Description : Experimental ROS2 node to publish encoder readings from a microcontroller.
#               MicroROS failed to produce encoder readings at a suitable frequency on ESP32.
#
#

import serial
import time

import rclp
from rclpy.node import Node
from std_msgs.msg import Int32

# configure the serial port
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
time.sleep(2)
print("\nEncoder Test ....\n")

while(1):
    # read the response from Arduino
    response = ser.readline().decode().strip()
    print("Response from Arduino: " + response)

class EncoderPublisher(Node);
    
    def __init__(self)
        super().__init__('encoder_publisher')
        self.publisher_ = self.create_publisher(Int32, 'Left_encoder', 10)
        timer_period = 0.1 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
    
    def timer_callback(self)
        msg = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)
        self.publisher_.publish(msg)
        self.get_logger().info('publishing; "%s"' %msg.data)
        

def main(args = None):
    rclpy.init(args = args)
    
    encoder_publisher = EncoderPublisher()
    
    rclpy.spin(encoder_publisher)
    
    encoder_publisherdestro_node()
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()
