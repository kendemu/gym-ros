import gym
import universe
import gym_ros

env = gym.make('ROSEnv-v0')
env.reset()

for _ in range(1000):
    env.render()
    ob, reward, done, _ =   env.step(env.action_space.sample())
    print "reward:", reward
    
