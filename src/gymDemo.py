import gymnasium as gym
import random


class Agent():
    def __init__(self, env):
        self.action_size = env.action_space.n
        print("Action size:", self.action_size)

    def get_action(self, state):
        #         action = random.choice(range(self.action_size))
        pole_angle = state[2]
        action = 0 if pole_angle < 0 else 1
        return action

def demoGym():
    env_name = "CartPole-v1"
    env = gym.make(env_name, render_mode="human")
    print("Observation space:", env.observation_space)
    print("Action space:", env.action_space)
    agent = Agent(env)
    state = env.reset()[0]

    for _ in range(1000):
        #     action = env.action_space.sample()
        action = agent.get_action(state)
        state, reward, done, info, ds = env.step(action)
        env.render()
        if(done):
            break

if __name__ == '__main__':
    demoGym()