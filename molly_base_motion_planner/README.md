molly base motion planner
=========================
ROS bindings to molly the motion planner

Quick usage
-----------
To use this package, you first need to run the server:
```sh
rosrun molly_base_motion_planner get_base_trajectory_server.py
```
Then you can try requesting a trajectory to the server (from (0,0,0) to (1,1,0):
```sh
rosrun molly_base_motion_planner get_base_trajectory_client.py 0 0 0 1 1 0
```

It should return the solution found, or tell you if there is no solution.
