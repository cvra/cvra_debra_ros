#!/usr/bin/env python2
import rospy
from geometry_msgs.msg import Twist
from cvra_rpc.message import *

def callback(data):
    send(('192.168.2.20', 20000), 'vel', [int(data.linear.x * 1000), int(data.angular.z * 1000)])
    print(int(data.linear.x * 1000), int(data.angular.z * 1000))

def listener():
    rospy.init_node('vel', anonymous=True)
    rospy.Subscriber("/debra/cmd_vel", Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
