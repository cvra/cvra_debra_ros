#!/usr/bin/env python3
from pickit.Datatypes import *
from pickit.DebraArm import DebraArm

import sys
import rospy
from cvra_msgs.msg import JointTrajectory, JointTrajectoryPoint, Tool
from cvra_msgs.srv import GetArmTrajectory, GetArmTrajectoryResponse

def convert_from_pickit(traj, sampling_period):
    "Convert trajectory from pickit to ROS message structure"
    res = JointTrajectory()
    point = JointTrajectoryPoint()
    length = 0

    now = rospy.Time.now()
    res.header.stamp.secs = now.secs
    res.header.stamp.nsecs = now.nsecs
    res.start_time.data.secs = now.secs
    res.start_time.data.nsecs = now.nsecs
    res.sampling_period = sampling_period

    for t in traj:
        time, pos, vel, acc = t

        point.position = pos
        point.velocity = vel
        point.acceleration = acc

        res.points.append(point)

        length += 1

    return res, length+1

def get_arm_trajectory(req, time_resolution):
    global arm

    # Compute path
    pth1, pth2, pz, pth3 = arm.get_path_xyz(start_pos = req.start_pos,
                                            start_vel = req.start_vel,
                                            target_pos = req.target_pos,
                                            target_vel = req.target_vel,
                                            time_resolution,
                                            'joint')
    # Pack path
    traj_th1, length = convert_from_pickit(pth1, time_resolution)
    traj_th2, length = convert_from_pickit(pth2, time_resolution)
    traj_th3, length = convert_from_pickit(pth3, time_resolution)
    traj_z, length = convert_from_pickit(pz, time_resolution)

    return GetBaseTrajectoryResponse(traj_th1, traj_th2, traj_th3, traj_z, length)

def arm_planning_server():
    rospy.init_node('arm_planner', anonymous=True)
    s = rospy.Service('get_arm_trajectory', GetArmTrajectory, get_arm_trajectory)
    print "PickIt is ready to pick it."
    rospy.spin()

def arm_planning_server_start(arm_orientation):
    global arm

    if arm_orientation == 'left':
        arm_name = 'left_arm'
    else:
        arm_name = 'right_arm'

    time_resolution = rospy.get_param("time_resolution")
    l1 = rospy.get_param("right_arm/arm_length")
    l2 = rospy.get_param("right_arm/forearm_length")

    origin = Vector3D(rospy.get_param("right_arm/origin/x"),
                      rospy.get_param("right_arm/origin/y"),
                      rospy.get_param("right_arm/origin/z"))

    theta1_constraints = JointMinMaxConstraint(
                            rospy.get_param("right_arm/shoulder/pos_range")[0],
                            rospy.get_param("right_arm/shoulder/pos_range")[1],
                            rospy.get_param("right_arm/shoulder/vel_range")[0],
                            rospy.get_param("right_arm/shoulder/vel_range")[1],
                            rospy.get_param("right_arm/shoulder/acc_range")[0],
                            rospy.get_param("right_arm/shoulder/acc_range")[1])
    theta2_constraints = JointMinMaxConstraint(
                            rospy.get_param("right_arm/elbow/pos_range")[0],
                            rospy.get_param("right_arm/elbow/pos_range")[1],
                            rospy.get_param("right_arm/elbow/vel_range")[0],
                            rospy.get_param("right_arm/elbow/vel_range")[1],
                            rospy.get_param("right_arm/elbow/acc_range")[0],
                            rospy.get_param("right_arm/elbow/acc_range")[1])
    theta3_constraints = JointMinMaxConstraint(
                            rospy.get_param("right_arm/wrist/pos_range")[0],
                            rospy.get_param("right_arm/wrist/pos_range")[1],
                            rospy.get_param("right_arm/wrist/vel_range")[0],
                            rospy.get_param("right_arm/wrist/vel_range")[1],
                            rospy.get_param("right_arm/wrist/acc_range")[0],
                            rospy.get_param("right_arm/wrist/acc_range")[1])
    z_constraints = JointMinMaxConstraint(
                            rospy.get_param("right_arm/z/pos_range")[0],
                            rospy.get_param("right_arm/z/pos_range")[1],
                            rospy.get_param("right_arm/z/vel_range")[0],
                            rospy.get_param("right_arm/z/vel_range")[1],
                            rospy.get_param("right_arm/z/acc_range")[0],
                            rospy.get_param("right_arm/z/acc_range")[1])

    initial_joints = JointSpacePoint(rospy.get_param("right_arm/shoulder/initial"),
                                     rospy.get_param("right_arm/elbow/initial"),
                                     rospy.get_param("right_arm/z/initial"),
                                     rospy.get_param("right_arm/wrist/initial"))

    arm = DebraArm.DebraArm(l1,
                            l2,
                            theta1_constraints,
                            theta2_constraints,
                            theta3_constraints,
                            z_constraints,
                            initial_joints,
                            origin,
                            flip_x = FLIP_RIGHT_HAND)

    arm_planning_server()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: get_arm_trajectory_server.py arm_orientation")
    else:
        arm_planning_server_start(sys.argv[1])
