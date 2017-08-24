# gym-ros  
A gym environment for ROS.  

# Installation  
```sudo pip install --upgrade .```  

## Supported Robots  
1. Turtlebot 2  
Using RGB camera for observations, cmd_vel for actions.
LIDAR, RGB-D sensor support will be on future release.
Will support Drones, Pepper, and Happy Mini on future release.

## What you need to support your robot
1. Define the reward.   
What is your reward? On default, I set the reward as the collision.  
When robot collide something, game over.  
2. Make your Agent.  
Make your agent. DQN, DQRN, CNN, PID Control, Rule-based AI, etc.....  
OpenAI Gym is just a environment for agent system, it doesn't provide A.I. algorithm.  


## Supported Environments  
1. Robot in real life  
2. Gazebo  
Not tested, but it will work because Gazebo is on ROS.
3. SIGVerse  
Tested.

## About the reset functionalities  
1. Robot in real life  
Robot in real life cannot be reset like a game.  
2. SIGVerse  
Resetting in the SIGVerse environment causes 10 seconds to re-establish connections. This problem causes overhead of training. So currently environment reset is not supported. Will be supported on future release.  

## Future
1. Adding multiple environment
Turtlebot, A.R. Drone 2.0, Pepper, Happy Mini  
2. Adding reconfigurable APIs


