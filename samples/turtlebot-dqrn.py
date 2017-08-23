import gym
import gym-ros

env = gym.make('RosEnv-v0')
env.reset()

for _ in range(1000):
    env.render()
    ob, reward, done, {} =  env.step(env.action_space.sample())
    print "reward:", reward
    
