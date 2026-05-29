import torch
from DeepNeuralNetworkPolicy import DeepNeuralNetworkPolicy
from KniffelEnv import KniffelEnv
from PlayGame import play_game

def evaluate_policy(env: KniffelEnv, policy: DeepNeuralNetworkPolicy) -> float:
    sum = 0
    cnt = 500
    for i in range(cnt):
        reward, _ = play_game(env, policy, train=False, doPrint=False)
        sum += reward
    return sum / cnt

if __name__ == '__main__':
    env = KniffelEnv()
    policy = DeepNeuralNetworkPolicy(env)
    policy.load_state_dict(torch.load("KniffelPolicy.nn", weights_only=True))
    with torch.no_grad():
        avg_score = evaluate_policy(env, policy)
        print(f"Average Score: {avg_score}")



