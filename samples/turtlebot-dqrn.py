import gym
#1;2802;0cimport gym_ros

env = gym.make('ROSEnv-v0')
env.reset()

for _ in range(1000):
    env.render()
    ob, reward, done =  env.step(env.action_space.sample())
    print "reward:", reward
    
