# coding: utf8

import numpy as np
import gym
import time

def get_action(weights, observation):
    wxb = np.dot(weights[:4], observation) + weights[4]
    if wxb >= 0:
        return 1
    else:
        return 0

def get_sum_reward_by_weights(env, weights):
    observation = env.reset()
    sum_reward = 0
    for t in range(1000):
        # time.sleep(0.01)
        # env.render()
        action = get_action(weights, observation)
        observation, reward, done, info = env.step(action)
        sum_reward += reward
        # print(sum_reward, action, observation, reward, done, info)
        if done:
            break
    return sum_reward


def get_weights_by_random_guess():
    return np.random.rand(5)

def get_weights_by_hill_climbing(best_weights):
    return best_weights + np.random.normal(0, 0.1, 5)

def get_best_result(algo="random_guess"):
    env = gym.make("CartPole-v0")
    np.random.seed(10)
    best_reward = 0
    best_weights = np.random.rand(5)

    for iter in range(10000):
        cur_weights = None

        if algo == "hill_climbing":
            # print(best_weights)
            cur_weights = get_weights_by_hill_climbing(best_weights)
        else:
            cur_weights = get_weights_by_random_guess()

        cur_sum_reward = get_sum_reward_by_weights(env, cur_weights)

        # print(cur_sum_reward, cur_weights)
        if cur_sum_reward > best_reward:
            best_reward = cur_sum_reward
            best_weights = cur_weights

        if best_reward >= 200:
            break

    print(iter, best_reward, best_weights)
    return best_reward, best_weights

print(get_best_result("hill_climbing"))

# env = gym.make("CartPole-v0")
# get_sum_reward_by_weights(env, [0.22479665, 0.19806286, 0.76053071, 0.16911084, 0.08833981])
