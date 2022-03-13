# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:53:43 2020

@author: User
"""

import gym
import random

env = gym.make("CartPole-v1")
env.reset()

class Agent:
    def __init__(self,env):
        self.action_size = env.action_space.n
        print("Action Size=",self.action_size)
        
    def get_action(self):
        action = random.choice(range(self.action_size))
        return(action)
        
agent = Agent(env)

for _ in range(200):
    action = agent.get_action()
    done = env.step(action)
    env.render()
    
if done:
    observation = env.reset()
env.close()