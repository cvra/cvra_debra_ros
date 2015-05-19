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

def index_cb(args):
    joint_publisher(args, 'index')

def motor_encoder_cb(args):
    joint_publisher(args, 'motor_encoder')

def motor_position_cb(args):
    joint_publisher(args, 'motor_position')

def motor_torque_cb(args):
    joint_publisher(args, 'motor_torque')

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

    elif type == 'index':
        node_id, index = tuple(args)

        joint.node_id = node_id
        joint.index = index
        joint.position.measured = index

    elif type == 'motor_encoder':
        node_id, raw_encoder = tuple(args)

        joint.node_id = node_id
        joint.raw_encoder_value = raw_encoder

    elif type == 'motor_position':
        node_id, position, velocity = tuple(args)

        joint.node_id = node_id
        joint.position.measured = position
        joint.velocity.measured = velocity

    elif type == 'motor_torque':
        node_id, torque, position = tuple(args)

        joint.node_id = node_id
        joint.torque = position
        joint.position.measured = position

    pub_joint.publish(joint)

if __name__ == '__main__':
    global pub_joint, joint
    pub_joint = rospy.Publisher('joint_debug', JointDebug, queue_size=0)
    rospy.init_node('feedback_stream', anonymous=True)
    joint = JointDebug()

    TARGET = ('0.0.0.0', 20042)
    callbacks = {'current_pid': current_pid_cb, \
                 'velocity_pid': velocity_pid_cb, \
                 'position_pid': position_pid_cb, \
                 'index': index_cb, \
                 'motor_encoder': motor_encoder_cb, \
                 'motor_position': motor_position_cb, \
                 'motor_torque': motor_torque_cb}

    RequestHandler = create_request_handler(callbacks)
    server = socketserver.UDPServer(TARGET, RequestHandler)
    server.serve_forever()
