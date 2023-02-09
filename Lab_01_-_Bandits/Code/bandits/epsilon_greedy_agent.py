'''
Created on 14 Jan 2022

@author: ucacsjj
'''

import numpy as np

from .agent import Agent

class EpsilonGreedyAgent(Agent):
    
    def __init__(self, environment, epsilon):
        super().__init__(environment)
        self._epsilon = epsilon

    # Q5a:
    # Change the implementation to use the epsilon greedy algorithm
    def _choose_action(self):
        action = 0
        action_space = self._environment.action_space
        p = np.random.random()
        if p < self._epsilon:
            # explore
            action = action_space.sample()
        else:
            average_q = np.divide(self.total_reward, self.number_of_pulls)
            best_action = np.where(average_q == np.amax(average_q))[0]
            action = best_action[0]

        return action
            
        
