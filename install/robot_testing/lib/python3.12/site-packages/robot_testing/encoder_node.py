# Author : Tony Willett
# Date :   31st March 2026
# Description : Experimental ROS2 node to publish encoder readings from a microcontroller.
#               MicroROS failed to produce encoder readings at a suitable frequency on ESP32.
#
#

import serial
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

# configure the serial port
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
time.sleep(2)
# print("\nEncoder Test ....\n")

#while(1):
    # read the response from Arduino
    #response = ser.readline().decode().strip()
    #print("Response from Arduino: " + response)

class EncoderPublisher(Node):
    
    def __init__(self):
        super().__init__('encoder_publisher')
        self.publisher_ = self.create_publisher(Int64, 'Left_encoder', 1)
        timer_period = 0.05 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
    
    def timer_callback(self):
        latest = None

        while ser.in_waiting > 0:
            try:
                latest = ser.readline().decode().strip()
            except:
                pass

        if latest is not None:
            try:
                msg = Int64()
                msg.data = int(latest)
                self.publisher_.publish(msg)
            except:
                pass

        

def main(args = None):
    rclpy.init(args = args)
    
    encoder_publisher = EncoderPublisher()
    
    rclpy.spin(encoder_publisher)
    
    encoder_publisher.destroy_node()
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()
