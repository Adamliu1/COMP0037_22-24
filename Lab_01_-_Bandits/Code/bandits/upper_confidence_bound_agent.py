'''
Created on 14 Jan 2022

@author: ucacsjj
'''

import math

import numpy as np

from .agent import Agent

class UpperConfidenceBoundAgent(Agent):

    def __init__(self, environment, c):
        super().__init__(environment)
        self._c = c

    # Q6a:
    # Implement UCB
    def _choose_action(self):
        # TODO: ask 
        # average_q = np.divide(self.total_reward, self.number_of_pulls)
        # best_action = np.where(average_q == np.amax(average_q))[0]
        # action = best_action[0]

        # # c term

        # upcv = self.c * np.sqrt(np.log(self.number_of_pulls)/N)
        action = 0
        return action
