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
Here is a list of the packages contained in this repository:
* **cvra_msgs**: which includes all our custome message structures
* **debra_control**: which handles the joint controllers
* **debra_description**: which provides description files ot model Debra
* **debra_gazebo**: which handles gazebo interactions with ROS & Debra


To do
-----
* Fix the `catkin_make` compilation problem with **debra_control**. Note: this
doesn't affect the operation of the package.
* Fix the operation problems of running roscore in parallel with the packages
of this metapackage.
