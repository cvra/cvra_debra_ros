#!/usr/bin/env python3
import threading
import rospy
from cvra_msgs.msg import JointDebug
import cvra_rpc.service_call
from cvra_rpc.message import *

def current_pid_cb(args):
    joint_publisher(args, 'current')

def velocity_pid_cb(args):
    joint_publisher(args, 'velocity')

def position_pid_cb(args):
    joint_publisher(args, 'position')

def joint_publisher(args, type):
    global pub_joint, joint

    if type == 'current':
        node_id, current, current_setpt, voltage = tuple(args)

        joint.node_id = node_id
        joint.current.measured = current
        joint.current.setpoint = current_setpt
        joint.voltage = voltage

    elif type == 'velocity':
        node_id, velocity, velocity_setpt = tuple(args)

        joint.node_id = node_id
        joint.velocity.measured = velocity
        joint.velocity.setpoint = velocity_setpt

    elif type == 'position':
        node_id, position, position_setpt = tuple(args)

        joint.node_id = node_id
        joint.position.measured = position
        joint.position.setpoint = position_setpt

    pub_joint.publish(joint)

if __name__ == '__main__':
    global pub_joint, joint
    pub_joint = rospy.Publisher('joint_debug', JointDebug, queue_size=0)
    rospy.init_node('feedback_stream', anonymous=True)
    joint = JointDebug()

    TARGET = ('0.0.0.0', 20042)
    callbacks = {'current_pid': current_pid_cb, \
                 'velocity_pid': velocity_pid_cb, \
                 'position_pid': position_pid_cb}

    RequestHandler = create_request_handler(callbacks)
    server = socketserver.UDPServer(TARGET, RequestHandler)
    server.serve_forever()
