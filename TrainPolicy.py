import os
import pickle
import time

import torch
import numpy as np

from DeepNeuralNetworkPolicy import DeepNeuralNetworkPolicy
from EvaluatePolicy import evaluate_policy
from KniffelEnv import KniffelEnv
from PlayGame import play_game

def train_epoch(env: KniffelEnv, policy: DeepNeuralNetworkPolicy, num_episodes: int = 100, games_per_episode: int = 100, learning_rate: float = 0.001):
    optimizer = torch.optim.Adam(policy.parameters(), lr=learning_rate)
    avg_rewards = []

    for episode in range(num_episodes):
        optimizer.zero_grad()
        loss = torch.tensor(0.0, dtype=torch.float)
        rewards = []
        result_data = []

        for i in range(games_per_episode):
            reward, log_probs = play_game(env, policy, doPrint=False)
            result_data.append((reward, log_probs))
            rewards.append(reward)

        avg_reward = np.mean(rewards).item()
        stddev_reward = np.std(rewards).item()

        for reward, log_probs in result_data:
            for log_prob in log_probs:
                norm_reward = (reward - avg_reward) / stddev_reward
                loss += (-norm_reward) * log_prob

        if episode % 10 == 0:
            print(f"episode = {episode}, train reward mean = {avg_reward} stddev = {stddev_reward}")
        avg_rewards.append(avg_reward)
        loss.backward()
        optimizer.step()

    return avg_rewards

def train_policy():
    env = KniffelEnv()
    policy = DeepNeuralNetworkPolicy(env)
    param_cnt = 0
    for p in policy.parameters():
        param_cnt += p.size().numel()
    print(policy)
    print(f"Parameter count = {param_cnt}")
    # load policy and rewards from last run
    rewards = []
    if os.path.exists("KniffelPolicy.nn") and os.path.exists("rewards.pkl"):
        policy.load_state_dict(torch.load("KniffelPolicy.nn", weights_only=True))
        with open("rewards.pkl", "rb") as file:
            rewards = pickle.load(file)
    # training loop, it can be interrupted and restarted later
    while len(rewards) < 400: # 400 epoches * 20 episodes * 100 games = 800.000 games
        start_time = time.time()
        train_epoch(env, policy, num_episodes=20, games_per_episode=100, learning_rate=0.001)
        reward = evaluate_policy(env, policy)
        end_time = time.time()
        rewards.append(reward)
        print(f"epoch = {len(rewards)}, duration = {end_time - start_time}s, avg score = {reward}")
        state_dict = policy.state_dict()
        torch.save(state_dict, "KniffelPolicy.nn")
        with open("rewards.pkl", "wb") as file:
            pickle.dump(rewards, file)

if __name__ == '__main__':
    train_policy()
