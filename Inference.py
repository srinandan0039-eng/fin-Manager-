from openenv import FinEnv

def run():
    env = FinEnv()
    state = env.reset()
    total_reward = 0

    for _ in range(20):
        # Decision logic
        if state["expenses"] > state["income"]:
            action = "cut_expenses"
        elif state["balance"] > 4000:
            action = "invest_money"
        elif state["savings"] < 2000:
            action = "save_money"
        else:
            action = "increase_income"

        state, reward, done = env.step(action)
        total_reward += reward

        if done:
            break

    return {
        "final_state": state,
        "total_reward": total_reward
    }

if __name__ == "__main__":
    print(run())
