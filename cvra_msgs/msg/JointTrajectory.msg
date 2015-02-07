# Series of points that the joint needs to follow
# Along with PID gains optimised for the trajectory set
std_msgs/Header header

cvra_msgs/PID pid
cvra_msgs/JointTrajectoryPoint[] points
