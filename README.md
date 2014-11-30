cvra_debra_ros
==============

ROS metapackage with several ROS packages related to Debra.


Usage
-----

It is assumed you have installed ROS and configured your ROS workspace.

Otherwise, please refer to the [ROS installation tutorial]
(http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment),
it is recommended to do a full install of ROS if you have enough disk space.

Note: the ROS workspace setup is treated in part 4 of the tutorial.

### Initial setup

Run the following commands in a terminal:
```sh
bash
cd ~/catkin_ws/src
git clone https://github.com/cvra/cvra_debra_ros.git
cd ..
catkin_make
source devel/setup.bash
```

The `catkin_make` will build the package for you and the
`source devel/setup.bash` command ensures ROS commands detect newly installed
packages.

Note: we assume your ROS workspace is named `catkin_ws` and is located in the
`home` directory.


Packages
--------

Here is a list of the packages contained in this repository:
* **debra_description**: which provides description files ot model Debra
