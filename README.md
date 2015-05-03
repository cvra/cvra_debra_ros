roscvra
=======
ROS stack of nodes that run on our robots

Setup
-----
It is assumed you have not installed ROS and configured your ROS workspace yet.
To setup ROS and everything, simply run:
```bash
bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/cvra/roscvra.git
chmod +x setup.bash
sudo ./setup.bash
cd ..
catkin_make
source devel/setup.bash
```

Remember to run these last two lines everything you tweak or change something in the package as they will build the package and ensure ROS commands detect newly installed packages.

Packages
--------
Here is a list of the packages contained in this repository that are actively used/supported:
- **cvra_msgs**: which includes all our custome message structures
- **master_bridge**: acts as a bridge between the master board and the PC that runs ROS using the simpleRPC interface
- **molly_base_motion_planner**: ROS bindings to molly

Dependencies
------------
You will need
- [simplerpc](https://github.com/cvra/simplerpc)
- [serial-datagram](https://github.com/cvra/serial-datagram)
- [molly-the-motion-planner](https://github.com/cvra/molly-the-motion-planner)
(to be able to use them along with python 3, you may want to install them using pip3.
