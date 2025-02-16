import numpy as np

PIZZA = 0
BURGER = 1
HOTDOG = 2
STATES = np.array([PIZZA, BURGER, HOTDOG])

ITERS = 100000

def sim() -> None:
    cur_state = PIZZA
    probs = np.array([[0.0, 0.3, 0.7],
                      [0.6, 0.2, 0.2],
                      [0.0, 0.5, 0.5]])
    
    counts = np.array([0, 0, 0])
    counts[cur_state] += 1
    for _ in range(ITERS):
        cur_state = np.random.choice(STATES, p=probs[cur_state])
        counts[cur_state] += 1
    
    print(f'counts: {counts / ITERS}')


    m = np.array([0, 1, 0])
    for _ in range(ITERS):
        m = np.matmul(m, probs)
        
    print(m)



if __name__ == '__main__':
    sim()