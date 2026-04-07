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
        self.pub1 = self.create_publisher(Int64, 'l_enc', 10) # Left wheel encoder
        self.pub2 = self.create_publisher(Int64, 'r_enc', 10) # Right wheel encoder
        self.pub3 = self.create_publisher(Int64, 'a_enc', 10) # Arm encoder
        timer_period = 0.05 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
    
    def timer_callback(self):
        latest = None

        while ser.in_waiting > 0:
            latest = ser.readline().decode().strip()

        if latest:
            try:
                parts = latest.split(',')
                if len(parts) == 3:
                    v1, v2, v3 = [int(p) for p in parts]

                    msg1 = Int64()
                    msg1.data = v1
                    self.pub1.publish(msg1)

                    msg2 = Int64()
                    msg2.data = v2
                    self.pub2.publish(msg2)

                    msg3 = Int64()
                    msg3.data = v3
                    self.pub3.publish(msg3)

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
