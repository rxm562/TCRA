import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def rep(data, N):
    params = {
        'CERBL':  {4: 720, 3: 360, 2: 120, 1: 5,   0: 0},
        'MLRM1':  {4: 240, 3: 120, 2: 20,  1: 5,   0: 0},
        'MHPHUD': {4: 960, 3: 480, 2: 120, 1: 10,  0: 0},
        'MMUH1':  {4: 360, 3: 270, 2: 90,  1: 10,  0: 0},
        'CERBM':  {4: 360, 3: 270, 2: 90,  1: 10,  0: 0},
        'CECBM':  {4: 480, 3: 360, 2: 90,  1: 20,  0: 0},
        'MLRM2':  {4: 720, 3: 540, 2: 135, 1: 20,  0: 0},
        'MMUH2':  {4: 360, 3: 240, 2: 90,  1: 10,  0: 0},
        'MSF1':   {4: 360, 3: 240, 2: 90,  1: 10,  0: 0},
        'CECBL':  {4: 480, 3: 360, 2: 90,  1: 10,  0: 0},
        'MSF2':   {4: 360, 3: 270, 2: 60,  1: 10,  0: 0},
        'MLRI':   {4: 360, 3: 270, 2: 60,  1: 10,  0: 0},
        'MMUH3':  {4: 360, 3: 270, 2: 60,  1: 10,  0: 0},
        'SPMBS':  {4: 360, 3: 270, 2: 60,  1: 10,  0: 0},
    }

    recovery = []
    for _, row in data.iterrows():
        mean_val = params.get(row['type'], {}).get(row['dmg'], 0)
        f1 = np.random.normal(mean_val, 0.3 * mean_val) if mean_val > 0 else 0
        recovery.append(f1)
        
    return recovery

def monte_carlo_simulation(data, num_simulations, N):
    all_simulations = []

    for _ in range(num_simulations):
        recovery_time = rep(data, N)
        data['RT'] = list(recovery_time)

        bb = []
        tt = list(range(0, 900, 5))
        for T in tt:
            bb.append(data[data.RT < T].shape[0])

        all_simulations.append(bb)

    # Convert to numpy array for easy averaging
    all_simulations = np.array(all_simulations)
    mean_simulation = np.mean(all_simulations, axis=0)
    min_simulation = np.min(all_simulations, axis=0)
    max_simulation = np.max(all_simulations, axis=0)

    return tt, all_simulations, mean_simulation, min_simulation, max_simulation