#!/usr/bin/env python3
import threading
import queue
import rospy
from cvra_msgs.msg import Pose2D
from cvra_rpc.message import *

def odometry_raw_cb(args):
    #print("Odometry raw values")
    #print(args)

    pose = Pose2D()

    x, y, theta = tuple(args)
    pose.x = x
    pose.y = y
    pose.theta = theta

    global pub
    pub.publish(pose)

if __name__ == '__main__':
    global pub
    pub = rospy.Publisher('odometry', Pose2D, queue_size=0)
    rospy.init_node('debra', anonymous=True)
    rate = rospy.Rate(100) # 10hz

    TARGET = ('0.0.0.0', 20000)
    callbacks = {'odometry_raw': odometry_raw_cb}

    RequestHandler = create_request_handler(callbacks)
    server = socketserver.UDPServer(TARGET, RequestHandler)
    server.serve_forever()
