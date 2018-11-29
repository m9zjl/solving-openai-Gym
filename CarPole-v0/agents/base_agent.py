#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 8:44 PM
# @Author  : ben
# @Site    :
# @File    : hill_climbing_agent.py.py
# @Software: PyCharm

"""
agent interface
"""
class base_agent:
    def learn(self, state, action, reward, done, info):
        pass

    def act(self,state, action, reward, done, info):
        pass

    def reset(self):
        pass
