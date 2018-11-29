#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 8:44 PM
# @Author  : ben
# @Site    :
# @File    : hill_climbing_agent.py.py
# @Software: PyCharm

"""
definite agent using definite rules to solve cart-pole v0
"""

import numpy as np
import sys
sys.path.append('../')
np.random.seed(10)
from .base_agent import base_agent

class definite_agent(base_agent):
    def __init__(self, dic):
        self.dic = dic

    def act(self, state, **kwargs):
        angle = -state[2]
        if angle > 0:
            return 'left'
        else:
            return 'right'

    def learn(self,**kwargs):
        pass
