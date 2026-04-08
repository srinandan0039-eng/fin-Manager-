import random

class FinEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.balance = random.randint(3000, 8000)
        self.income = random.randint(1500, 4000)
        self.expenses = random.randint(1000, 5000)
        self.savings = random.randint(500, 3000)
        self.risk = random.randint(1, 5)
        return self._get_state()

    def step(self, action):
        reward = 0

        # Random event
        event = random.choice(["none", "loss", "profit"])
        if event == "loss":
            self.balance -= 300
        elif event == "profit":
            self.balance += 300

        # Actions
        if action == "cut_expenses":
            self.expenses = max(0, self.expenses - 200)
            reward += 1

        elif action == "increase_income":
            self.income += 300
            reward += 1

        elif action == "save_money":
            if self.balance > 500:
                self.balance -= 300
                self.savings += 300
                reward += 1
            else:
                reward -= 1

        elif action == "invest_money":
            if self.balance > 500:
                if random.random() > 0.5:
                    self.balance += 500
                    reward += 2
                else:
                    self.balance -= 400
                    reward -= 1
            else:
                reward -= 1

        else:
            reward -= 1

        # Monthly update
        self.balance += self.income - self.expenses

        # Risk logic
        if self.expenses > self.income:
            self.risk += 1
            reward -= 1
        else:
            self.risk = max(1, self.risk - 1)

        done = self.balance <= 0 or self.savings >= 10000

        return self._get_state(), reward, done

    def _get_state(self):
        return {
            "balance": self.balance,
            "income": self.income,
            "expenses": self.expenses,
            "savings": self.savings,
            "risk": self.risk
        }
