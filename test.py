print("hello")

import numpy as np

A = np.array([1,2])
print(A)

def update_action(env, state, explore_rate, Q):
        available_actions = [_i for _i, _s in enumerate(state) if _s.isnumeric()]
        if len(available_actions) == 0: # If there are no actions
            return None
        elif len(available_actions) == 1: # If there are only one possible action
            action = available_actions[0]
            return action
        else:
            n = random.uniform(0,1)
            if n < explore_rate: # do a random action, exploration
                action = random.choice(list(action_dict.values()))
                return action
            else: # select action with highest q_value, exploitation
                max_index = np.argmax(Q)
                best_action = available_actions[max_index]
                return best_action
    


    # Q_test[state][action] = ((1-learning_rate)*Q_test[state][action]) + learning_rate*(rew + GAMMA_test*np.max(Q_test[new_state]))
    Q_test=update_q_table(Q_test, state, action, learning_rate, new_state)
    #Q_test[state, action] = Q_test[state, action] + learning_rate * (rew + GAMMA_test * max_future_q - Q_table[state, action])

