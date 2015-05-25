#!/usr/bin/env python3
import sys
import rospy
from cvra_msgs.srv import GetBaseTrajectory
from cvra_msgs.msg import Pose2D, Velocity2D

def get_base_trajectory_client(start_pose,
                               start_velocity,
                               target_pose,
                               sampling_period):
    rospy.wait_for_service('get_base_trajectory')
    try:
        get_base_traj = rospy.ServiceProxy('get_base_trajectory', GetBaseTrajectory)
        response = get_base_traj(start_pose,
                                 start_velocity,
                                 target_pose,
                                 sampling_period)
        return response.base_trajectory, response.length
    except rospy.ServiceException, e:
        print("Service call failed: %s"%e)

def print_usage():
    print("%s start_x start_y start_theta target_x target_y target_theta"%sys.argv[0])

if __name__ == "__main__":
    start_pose = Pose2D()
    start_velocity = Velocity2D()
    target_pose = Pose2D()
    sampling_period = 0.01

    if len(sys.argv) == 7:
        start_pose.x = float(sys.argv[1])
        start_pose.y = float(sys.argv[2])
        start_pose.theta = float(sys.argv[3])
        target_pose.x = float(sys.argv[4])
        target_pose.y = float(sys.argv[5])
        target_pose.theta = float(sys.argv[6])
    else:
        print_usage()
        sys.exit(1)

    start_velocity.x = 0
    start_velocity.y = 0
    start_velocity.theta = 0

    print("Start at %s, %s, %s"%(start_pose.x, start_pose.y, start_pose.theta))
    print("Go to %s, %s, %s"%(target_pose.x, target_pose.y, target_pose.theta))

    traj, length = get_base_trajectory_client(start_pose, start_velocity, target_pose, sampling_period)
    if length > 0:
        print("Got a trajectory: ", traj)
    else:
        print("No solution found")
