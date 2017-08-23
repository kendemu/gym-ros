import gym
import universe
import gym_ros
import numpy as np
import cv2

env = gym.make('ROSEnv-v0')
env.reset()

for _ in range(100000):
    env.render()
    ob, reward, done, _ =   env.step(env.action_space.sample())
    if done:
        print "Game Over!!"
        env.step(np.array([[0, 0, 0],[0, 0, 0]]))
        break
    if ob is not None:
        cv2.imshow("observations", ob)
        cv2.waitKey(1)
        print "observations received"
        
    print "reward:", reward

cv2.destroyAllWindows()
