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
    global publishers, joints

    if type == 'current':
        node_id, current, current_setpt, voltage = tuple(args)

        joints[node_id].node_id = node_id
        joints[node_id].current.measured = current
        joints[node_id].current.setpoint = current_setpt
        joints[node_id].voltage = voltage

    elif type == 'velocity':
        node_id, velocity, velocity_setpt = tuple(args)

        joints[node_id].node_id = node_id
        joints[node_id].velocity.measured = velocity
        joints[node_id].velocity.setpoint = velocity_setpt

    elif type == 'position':
        node_id, position, position_setpt = tuple(args)

        joints[node_id].node_id = node_id
        joints[node_id].position.measured = position
        joints[node_id].position.setpoint = position_setpt

    elif type == 'index':
        node_id, index = tuple(args)

        joints[node_id].node_id = node_id
        joints[node_id].index = index
        joints[node_id].position.measured = index

    elif type == 'motor_encoder':
        node_id, raw_encoder = tuple(args)

        joints[node_id].node_id = node_id
        joints[node_id].raw_encoder_value = raw_encoder

    elif type == 'motor_position':
        node_id, position, velocity = tuple(args)

        joints[node_id].node_id = node_id
        joints[node_id].position.measured = position
        joints[node_id].velocity.measured = velocity

    elif type == 'motor_torque':
        node_id, torque, position = tuple(args)

        joints[node_id].node_id = node_id
        joints[node_id].torque = position
        joints[node_id].position.measured = position

    publishers[node_id].publish(joints[node_id])

if __name__ == '__main__':
    global publishers, joints

    pub_left_wheel = rospy.Publisher('left_wheel', JointDebug, queue_size=0)
    pub_right_wheel = rospy.Publisher('right_wheel', JointDebug, queue_size=0)
    pub_left_wrist = rospy.Publisher('left_wrist', JointDebug, queue_size=0)
    rospy.init_node('feedback_stream', anonymous=True)
    left_wheel = JointDebug()
    right_wheel = JointDebug()
    left_wrist = JointDebug()

    publishers = {'left-wheel': pub_left_wheel, \
                  'right-wheel': pub_right_wheel, \
                  'left-wrist': pub_left_wrist}
    joints = {'left-wheel': left_wheel, \
              'right-wheel': right_wheel, \
              'left-wrist': left_wrist}

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
