#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 8:44 PM
# @Author  : ben
# @Site    : 
# @File    : hill_climbing_agent.py.py
# @Software: PyCharm


"""
angent obect to solve cartpole project with hill climbing algorythm

"""
import numpy as np
import sys
sys.path.append('.')
np.random.seed(10)
from .base_agent import base_agent


class hill_climbing_agent(base_agent):
    def __init__(self):
        self.max_r = 0
        self.best_w = np.random.rand(5)
        self.cur_w = np.random.rand(5)

    def get_w_by_hill_climbing(self):
        return self.best_w + np.random.normal(0, 0.1, 5)

    def learn(self, reward=None, **kwargs):
        if reward > self.max_r :
            # print("wupdated ", self.best_w, self.cur_w)
            self.best_w = self.cur_w
            # print('reward updated', self.max_r, reward)
            self.max_r = reward
        elif reward == 200 and np.abs(self.cur_w - self.best_w).sum() < 0.2:
            self.best_w = self.cur_w
            self.max_r = reward
        else:
            self.cur_w = self.get_w_by_hill_climbing()

    def act(self, state, **kwargs):
        val = np.dot(self.cur_w[:4], state) + self.cur_w[4]
        if val < 0:
            return 'left'
        else:
            return 'right'

    def reset(self):
        self.cur_w = self.get_w_by_hill_climbing()
