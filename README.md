# gym-ros  
A gym environment for ROS.  

# Installation  
```sudo pip install --upgrade .```  

## Supported Robots  
1. Turtlebot 2  
Using RGB camera for observations, cmd_vel for actions.
LIDAR, RGB-D sensor support will be on future release.
Will support Drones, Pepper, and Happy Mini on future release.

## Usage  
```import gym```  
```import gym_ros```  
  
## Supported Types  
1. sensor_msgs/Image <-> 3D tensor numpy array  
2. geometry_msgs/Twist <-> SE(3) numpy array  
3. std_msgs/Bool <-> 0 - 1 fuzzy set value(float)  

## What you need to support your robot
1. Define the reward.   
What is your reward? On default, I set the reward as the collision.  
When robot collide something, game over.  
Also, you need something to detect the reward. If you can't observe the reward, you have to make your algorithm to POMDP.  
2. Make your Agent.  
Make your agent. DQN, DQRN, CNN, PID Control, Rule-based AI, etc.....  
OpenAI Gym is just a environment for agent system, it doesn't provide A.I. algorithm.  


## Supported Environments  
1. Robot in real life  
2. Gazebo  
Not tested, but it will work because Gazebo is on ROS.
3. SIGVerse  
Tested.
  
## How to run SIGVerse  
1. roscore  
2. roslaunch rosbridge_server rosbridge_websocket.launch  
3. rosrun sigverse_ros_bridge sigverse_ros_bridge  
4. execute your python program using gym.  
Go to SIGVerse Wiki to get sigverse_ros_bridge program.  

## About the reset functionalities  
1. Robot in real life  
Robot in real life cannot be reset like a game.  
2. SIGVerse  
Resetting in the SIGVerse environment causes 10 seconds to re-establish connections. This problem causes overhead of training. So currently environment reset is not supported. Will be supported on future release.  

## Future
1. Adding multiple environment
Turtlebot, A.R. Drone 2.0, Pepper, Happy Mini  
2. Adding reconfigurable APIs

