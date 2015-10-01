# ROSCVRA

ROS stack of nodes that run on our robots

# Setup

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


# Build

When updating nodes, you need to rebuild the packages:
```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```


# Build Docker image

To run the dev setup, a Docker container is provided under the **docker_cvra_dev**.
You can build it:
```bash
cd ~/catkin_ws/src/roscvra
docker build -t cvra-dev docker_cvra_dev/
```

Then you can see the image has been added in your docker images, run `docker ps`.
To run the dev setup:
```bash
docker run -it \
       --user=$USER \
       --env="DISPLAY" \
       --workdir="/home/$USER" \
       --volume="/home/$USER:/home/$USER" \
       --volume="/etc/group:/etc/group:ro" \
       --volume="/etc/passwd:/etc/passwd:ro" \
       --volume="/etc/shadow:/etc/shadow:ro" \
       --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
       --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
       --env="QT_X11_NO_MITSHM=1" \
       cvra-dev \
       bash
```
This will forward your home directory so you can use the catkin workspace where you developed directly inside the container.
Now you should be able to run the simulation inside the docker container just created.


# Simulation

To launch the robot model in simulation run:
```bash
roslaunch debra_description gazebo.launch
```


# Operations

To launch the ROS stack on Debra (similarly for Caprica, use `caprica.launch` instead), do the following:
```bash
roslaunch cvra_operations debra.launch
```


# Packages

Here is a list of the packages contained in this repository that are actively used/supported:

- **debra_description**: URDF model of debra, also handles the simulation for now
- **master_bridge**: acts as a bridge between the master board and the PC that runs ROS using the simpleRPC interface
- **sick_tim**: driver and parser for the measurements coming from the laser range finder sensor, we use a Sick Tim561 on our robot


# Dependencies

You will need
- [simplerpc](https://github.com/cvra/simplerpc)
(to be able to use them along with python 3, you may want to install them using pip3.
