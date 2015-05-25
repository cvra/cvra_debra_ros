#!/usr/bin/env python3
import threading
import rospy
from cvra_msgs.msg import Pose2D, JointInfo
from cvra_rpc.message import *

RIGHT_WHEEL_ID = 11
LEFT_WHEEL_ID = 10

def odometry_raw_cb(args):
    global pub_odometry
    pose = Pose2D()

    x, y, theta = tuple(args)
    pose.x = x
    pose.y = y
    pose.theta = theta

    pub_odometry.publish(pose)

if __name__ == '__main__':
    global pub_odometry
    pub_odometry = rospy.Publisher('odometry', Pose2D, queue_size=0)
    rospy.init_node('master_bridge', anonymous=True)

    TARGET = ('0.0.0.0', 20000)
    callbacks = {'odometry_raw': odometry_raw_cb}

    RequestHandler = create_request_handler(callbacks)
    server = socketserver.UDPServer(TARGET, RequestHandler)
    server.serve_forever()
