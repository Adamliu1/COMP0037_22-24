#!/usr/bin/env python3

'''
Created on 13 Jan 2022

@author: ucacsjj
'''
import numpy as np
import gym

from bandits.bandit import Bandit
from bandits.bandit import BanditEnvironment

# Q2b:
# Write a method which takes only takes the bandit environment
# as input, runs all the bandits, and computes the mean and
# covariance. Print out the result for each bandit using the
# form specified below

def run_bandits(environment, number_of_steps):

    num_of_bandit = environment.number_of_bandits()
    for b in range(num_of_bandit):
        cur_bandit = environment.bandit(b)
        rewards = np.zeros(1)
        for i in range(number_of_steps):
            cur_reward = cur_bandit.pull_arm()
            rewards = np.append(rewards, [cur_reward])
        print(f'bandit = {b}, mean = {np.mean(rewards)}, sigma = {np.std(rewards)}')
        
if __name__ == '__main__':
    
    # Q2a:
    # Change to implement four bandits with the mean and
    # covariance specified in the question
    environment = BanditEnvironment(4)

    # Add some bandits
    environment.set_bandit(0, Bandit(1, 1))    
    environment.set_bandit(1, Bandit(1, 2))
    environment.set_bandit(2, Bandit(2, 1))
    environment.set_bandit(3, Bandit(2, 2))
    
    # Q2b:
    # Vary the number of steps if you like to validate your code
    run_bandits(environment, 1000)


        
