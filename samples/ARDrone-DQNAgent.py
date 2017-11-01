import gym
import universe
import gym_ros
from tqdm import tqdm
import numpy as np
from keras.models import Sequential, load_model
from keras.initializations import normal
from keras import optimizers
from keras.optimizers import RMSprop
from keras.layers import Convolution2D, Flatten, ZeroPadding2D
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.pooling import MaxPooling2D
from keras.regularizers import l2
from keras.optimizers import SGD , Adam
import memory
import cv2

env = gym.make('ROSEnv-v0')
env.reset()

__iter = 100000
pbar = tqdm(total=__iter)

print "training in SIGVerse Environment"

total = 0.0

for _ in range(100000):
    env.render()
    pbar.update(1)
    ob, reward, done, _ =   env.step(env.action_space.sample())
    total += reward
    if done:
        print "Game Over!!"
        total = 0.0
        env.reset()
        
    if ob is not None:        
        cv2.imshow("observations", ob)
        cv2.waitKey(1)

    pbar.set_description("Total reward : {0}".format(str(total)))

cv2.destroyAllWindows()
