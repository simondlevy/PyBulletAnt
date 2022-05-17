#!/usr/bin/env python3
'''
Make a simulated ant "wiggle it just a little bit"

Dependencies: gym, numpy, pybullet

MIT License
'''
import pybullet_envs
import gym
import numpy as np
from time import time

env = gym.make('AntBulletEnv-v0')

# Note: Unlike ordinary gym, pybullet requires you to call render() just once, at the start
# See: https://github.com/benelot/pybullet-gym/issues/25
env.render()

env.reset()

start = time()

action = np.zeros(8)

JOINT = 0

angle = 0

while True:

    try:

        env.step(action)

        # Allow a second for ant to hit the floor
        if time() - start > 1:

            value = np.sin(angle)

            action[JOINT] = value

            angle += .01


    except KeyboardInterrupt:
        break;

