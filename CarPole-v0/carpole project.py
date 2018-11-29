import gym
import sys
import time

sys.path.append('../')
from agents.hill_climbing_agent import hill_climbing_agent
from agents.definite_agent import definite_agent

env = gym.make('CartPole-v0')
state, reward, done, info = env.reset()
dic = {'left': 0,
       'right': 1}
agent = hill_climbing_agent()
sum_reward = 0
action = 'left'
for i in range(10000):
    env.render()
    state, reward, done, info = env.step(dic[action])
    action = agent.act(state, )
    # print(state,'action=',action)
    sum_reward += reward
    if done:
        agent.learn(reward=sum_reward)
        print(state, reward, sum_reward, done, info)
        sum_reward = 0
        env.reset()
        agent.reset()
env.close()
