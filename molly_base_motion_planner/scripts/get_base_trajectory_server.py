#!/usr/bin/env python2
from molly.Settings import Settings, STAIRS
from molly.Pathplanner import get_path
from molly.Vec2D import Vec2D
from molly.Circle import Circle
from molly.Tangent import Tangent
from molly.Polygon import Polygon

import rospy
from math import cos, sin, sqrt, atan2
from cvra_msgs.msg import BaseTrajectory, BaseTrajectoryPoint
from cvra_msgs.srv import GetBaseTrajectory, GetBaseTrajectoryResponse

def convert_from_molly(traj, sampling_period):
    "Convert trajectory from molly to ROS message structure"
    res = BaseTrajectory()
    point = BaseTrajectoryPoint()
    length = 0

    now = rospy.Time.now()
    res.start_time.data.secs = now.secs
    res.start_time.data.nsecs = now.nsecs
    res.sampling_period = sampling_period

    for t in traj:
        pos, spd, acc, ts = t

        # Equation 8 of tracy's paper
        speed = sqrt(spd.pos_x ** 2 + spd.pos_y ** 2)
        if speed > 1e-3:
            omega = (spd.pos_x * acc.pos_y - spd.pos_y * acc.pos_x)
            omega = omega / speed ** 2
        else:
            omega = 0

        point.pose.x = pos.pos_x
        point.pose.y = pos.pos_y
        point.pose.theta = atan2(spd.pos_y, spd.pos_x)
        point.velocity.x = speed
        point.velocity.y = 0
        point.velocity.theta = omega

        now = rospy.Time.now()
        res.header.stamp.secs = now.secs
        res.header.stamp.nsecs = now.nsecs
        res.points.append(point)

        length += 1

    return res, length+1

def get_base_trajectory(req):
    # Initialise settings for molly
    map_settings = Settings(max_acc=1.5,
                            max_v=1.0,
                            time_resolution=req.sampling_period,
                            static_poly_obs=[STAIRS],
                            static_circ_obs=[],
                            obs_min_r=0.05,
                            playground_dim=(3.0, 2.0))
    # Compute path
    path = get_path(settings = map_settings,
                    polygons = [],
                    circles = [],
                    start_pos = Vec2D(req.start_pose.x,
                                      req.start_pose.y),
                    start_heading = Vec2D(cos(req.start_pose.theta),
                                          sin(req.start_pose.theta)),
                    start_v = req.start_velocity.x*cos(req.start_pose.theta)
                              + req.start_velocity.y*sin(req.start_pose.theta),
                    target_pos = Vec2D(req.target_pose.x,
                                       req.target_pose.y))
    # Pack path
    trajectory, length = convert_from_molly(path, req.sampling_period)

    return GetBaseTrajectoryResponse(trajectory, length)

def base_motion_planning_server():
    rospy.init_node('molly_base_motion_planner', anonymous=True)
    s = rospy.Service('get_base_trajectory', GetBaseTrajectory, get_base_trajectory)
    print "Molly is ready to compute base trajectories."
    rospy.spin()

if __name__ == '__main__':
    base_motion_planning_server()
