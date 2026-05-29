import torch
import torch.nn.functional as F
import gymnasium as gym

class DeepNeuralNetworkPolicy(torch.nn.Module):
    def __init__(self, env: gym.Env, hidden_sizes: list[int] = [5000, 500, 50]):
        super(DeepNeuralNetworkPolicy, self).__init__()
        self.obs_space = env.observation_space.n
        self.act_space = env.action_space.n
        self.hidden_layers = torch.nn.ModuleList()
        input_size = self.obs_space
        for output_size in hidden_sizes:
            fc = torch.nn.Linear(input_size, output_size)
            self.hidden_layers.append(fc)
            input_size = output_size
        self.output_layer = torch.nn.Linear(input_size, self.act_space)

    def forward(self, x):
        for layer in self.hidden_layers:
            x = F.relu(layer(x))
        x = self.output_layer(x)
        x = F.softmax(x, dim=0)
        return x