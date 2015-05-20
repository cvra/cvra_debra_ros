# Series of points that the joint needs to follow
# Along with PID gains optimised for the trajectory set
std_msgs/Header header

std_msgs/Time start_time
float64 sampling_period
cvra_msgs/PID pid
cvra_msgs/JointTrajectoryPoint[] points
