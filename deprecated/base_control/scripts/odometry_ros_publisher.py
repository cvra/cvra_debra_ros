#!/usr/bin/env python2
import threading
import numpy as np
import rospy
import tf
from nav_msgs.msg import Odometry
from cvra_rpc.message import *

def odometry_raw_cb(args):
    #print("Odometry raw values")
    #print(args)

    odom = Odometry()

    x, y, theta = tuple(args)
    current_time = rospy.get_rostime()

    odom.header.stamp.secs = current_time.secs
    odom.header.stamp.nsecs = current_time.nsecs
    odom.header.frame_id = "map"
    odom.child_frame_id = "base_link"

    odom.pose.pose.position.x = x
    odom.pose.pose.position.y = y
    odom.pose.pose.position.z = 0

    quat = tf.transformations.quaternion_from_euler(0, 0, theta)
    odom.pose.pose.orientation.x = quat[0]
    odom.pose.pose.orientation.y = quat[1]
    odom.pose.pose.orientation.z = quat[2]
    odom.pose.pose.orientation.w = quat[3]

    global pub
    pub.publish(odom)

if __name__ == '__main__':
    global pub
    pub = rospy.Publisher('odometry', Odometry, queue_size=10)
    rospy.init_node('debra', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    TARGET = ('0.0.0.0', 20000)
    callbacks = {'odometry_raw': odometry_raw_cb}

    RequestHandler = create_request_handler(callbacks)
    server = socketserver.UDPServer(TARGET, RequestHandler)
    server.serve_forever()
