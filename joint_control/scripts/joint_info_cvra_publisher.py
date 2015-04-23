#!/usr/bin/env python2
import threading
import rospy
from cvra_msgs.msg import JointInfo
from cvra_rpc.message import *

RIGHT_WHEEL_ID = 11
LEFT_WHEEL_ID = 10

def odometry_raw_cb(args):
    pass

def joint_info_cb(args):
    global pub_right, pub_left
    joint = JointInfo()

    node_id, pos, speed = tuple(args)

    if(node_id == RIGHT_WHEEL_ID):
        joint.nodeID = str(node_id)
        joint.position = pos
        joint.velocity = speed
        pub_right.publish(joint)
    elif(node_id == LEFT_WHEEL_ID):
        joint.nodeID = str(node_id)
        joint.position = pos
        joint.velocity = speed
        pub_left.publish(joint)

if __name__ == '__main__':
    global pub_right, pub_left
    pub_right = rospy.Publisher('joint_right', JointInfo, queue_size=0)
    pub_left = rospy.Publisher('joint_left', JointInfo, queue_size=0)
    rospy.init_node('motor_node', anonymous=True)
    rate = rospy.Rate(100) # 100hz

    TARGET = ('0.0.0.0', 20000)
    callbacks = {'pos': joint_info_cb}

    RequestHandler = create_request_handler(callbacks)
    server = socketserver.UDPServer(TARGET, RequestHandler)
    server.serve_forever()
