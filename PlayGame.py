import torch
import numpy as np

from DeepNeuralNetworkPolicy import DeepNeuralNetworkPolicy
from KniffelEnv import KniffelEnv

# returns game result and trajectory as logarithmic probability
def play_game(env: KniffelEnv, policy: DeepNeuralNetworkPolicy, train: bool = True, doPrint: bool = False):
    state, info = env.reset()
    if doPrint:
        print(f"info = {info}")
    done = False
    log_probs = []
    total_reward = 0
    action_list = [i for i in range(policy.act_space)]
    while not done:
        action_probs = policy(state)
        if train:
            action = np.random.choice(action_list, p=action_probs.detach().numpy())
        else:
            action = torch.argmax(action_probs).item()
        state, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        done = terminated or truncated
        log_probs.append(torch.log(action_probs[action]))
        if doPrint:
            print(f"action = {action}, info = {info}")

    return total_reward, log_probs

if __name__ == '__main__':
    env = KniffelEnv()
    policy = DeepNeuralNetworkPolicy(env)
    policy.load_state_dict(torch.load("KniffelPolicy.nn", weights_only=True))
    with torch.no_grad():
        reward, _ = play_game(env, policy, train=False, doPrint=True)
        print(f"total reward = {reward}")
