from gym.envs.registration import register

print "__init__.py called"
register(
    id="ROSEnv-v0",
    entry_point="gym_ros.envs:ROSEnv",
    timestep_limit=1000,
    reward_threshold=-1.0,
    nondeterministic=True
)
