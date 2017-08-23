from gym.envs.registration import register

register(
    id="ROSEnv-v0",
    entry_point="gym_ros.envs:ROSEnv",
)
