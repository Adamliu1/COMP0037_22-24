#!/usr/bin/env python3

'''
Created on 13 Jan 2022

@author: ucacsjj
'''

import matplotlib.pyplot as plt
import numpy as np

from bandits.bandit import Bandit

if __name__ == '__main__':
    
    # Q1b:
    # Vary the number of times the agent gets fired to see what you find out
    '''
    Findings, 
    num_of_step = 1000
        batch_q=0.9616797992835828, batch_sigma=2.0874313888904754
        cumulative_q=0.9616797992835837
        recursive_q=1.3208796171236368
    num_of_step = 10000
        batch_q=1.0016782776652455, batch_sigma=1.9989560064111458
        cumulative_q=1.0016782776652415
        recursive_q=-5.036776049828063
    NOTE: the larger the number of iterations, the more closer the mean and s.d 
    of the pulled data is to the distribution set by the Bandit instance.
    '''
    number_of_steps = 1000

    # Array to store the reward
    rewards = np.zeros(number_of_steps)

    # Q1a:    
    # Create a bandit object here with the right mean and covariance
    # and use the pull_arm method to query the reward a large number
    # of times. We use this iterative one sample-at-a-time approach
    # because this is used later for the different learning frameworks
    # we will encounter.
    bandit = None
    bandit = Bandit(mean=1.0, sigma=2.0)
    for s in range(0, number_of_steps):
        cur_reward = bandit.pull_arm()
        rewards[s] = cur_reward


    # Generate the plots below. Please note that we use labels, titles and
    # captions. We expect you to do this in any material you submit,
    # because labelling graphs is fundamental to presenting and analysing
    # results.
        
    # Generate the reward plot
    plt.xlabel('Sample number')
    plt.ylabel('Reward')
    plt.plot(rewards, color = 'red', label = 'Reward')
    
    # Generate the histogram of the reward plot
    plt.figure()    
    n, bins, patches = plt.hist(rewards, 50, density=True, facecolor='g', alpha=0.75)
    plt.xlabel('Rewards')
    plt.ylabel('Probability')
    plt.title('Reward Histogram')
    plt.grid(True)

    print(f'batch_q={np.mean(rewards)}, batch_sigma={np.std(rewards)}')    

    cumulative_q = np.cumsum(rewards)[-1] / number_of_steps
    print(f'cumulative_q={cumulative_q}')
    
    # Q1c:
    # Change the way the mean reward is computed to use the
    # iterative expression instead of storing an array of all rewards
    # and computing the mean at the end. We use the recursive form
    # because other algorithms later rely upon it.
    recursive_q = rewards[0]
    for i in range(number_of_steps):
        recursive_q = recursive_q + (rewards[i]-recursive_q)/(i+1)

    print(f'recursive_q={recursive_q}')

    # Do not block on the individual plots. Instead, wait for key
    # press. A small pause is needed in some systems to stop blocking.
    plt.ion()
    plt.show()
    plt.pause(0.001)
    input()
