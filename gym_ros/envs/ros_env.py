import subprocess, signal
import os
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
import gym
from gym import error, spaces, utils
from gym.utils import seeding
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

class ROSEnv(gym.Env):
    metadata= {'render.modes' : ['human']}

    def __init__(self):
        ##establish connection to ROS.
        rospy.init_node("gym-ros")
        self.vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.img_sub = rospy.Subscriber("/ardrone/front/image_raw", Image, self.imgCb)
        self.collide_sub = rospy.Subscriber("/collided", Bool, self.collideCb)
        self.image = None
        self.bridge = CvBridge()
        self.isCollided = False
        self.viewer = None
        self.colliderLoaded = False
        
        #TODO : setup observation dementions and action space demention via parameter server
        self.max_speed = 2.0
        self.width = 640
        self.height = 480

        self.observations = np.zeros((self.width, self.height, 3))

        
        #self.observations = spaces.Box(low=0, high=255, shape=(self.width, self.height))
        self.action_space = spaces.Box(low=-self.max_speed, high=self.max_speed, shape=(6,))

        
    def imgCb(self, msg):
        #convert Image to numpy array
        try:
            self.image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as e:
            print e


    def collideCb(self, msg):
        self.colliderLoaded = True
        self.isCollided = msg.data
        rospy.sleep(0.033)
        
    def _step(self, action):
        while self.colliderLoaded is not True:
            rospy.sleep(1)

        cmd_vel = Twist()
        print action
        cmd_vel.linear.x = action[0]
        cmd_vel.linear.y = action[1]
        cmd_vel.linear.z  =action[2]
        cmd_vel.angular.x = action[3]
        cmd_vel.angular.y = action[4]
        cmd_vel.angular.z = action[5]
        self.vel_pub.publish(cmd_vel)        
        reward = self._get_reward()
        if self.image is not None:
            self.observations = self.image
            
            
        done = True if self.isCollided else False
        rospy.sleep(0.033)
        return (self.observations, reward, done, {})

    def _reset(self):
        if self.viewer is None:
            self.viewer = subprocess.Popen(["%s/gym-ros/Bin/SIGVerse-DRONE.x86_64"%(os.environ["HOME"])], shell=False)
        else:
            os.kill(self.viewer.pid, signal.SIGKILL)
            self.viewer = subprocess.Popen(["%s/gym-ros/Bin/SIGVerse-DRONE.x86_64"%(os.environ["HOME"])], shell=False)

        self.colliderLoaded = False

            
            
    def _get_reward(self):
        #Reward is given for obstacle avoidance
        if self.isCollided:
            return -1.0
        else:
            return 0.03


    def _render(self, mode='human', close=False):
        if self.viewer is None:
            self._reset()
