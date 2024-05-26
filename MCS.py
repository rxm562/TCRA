### Monte Carlo Simulation

# Preparing Dataset
building_data = df
building_probabilities = estimate_damage(building_data)

building_probabilities['LS1']=building_probabilities['Slight']
building_probabilities['LS2']=building_probabilities['Moderate']
building_probabilities['LS3']=building_probabilities['Extensive']
building_probabilities['LS4']=building_probabilities['Complete']
building_probabilities['DS0']=1-building_probabilities['Slight']
building_probabilities['DS1']=building_probabilities['Slight']-building_probabilities['Moderate']
building_probabilities['DS2']=building_probabilities['Moderate']-building_probabilities['Extensive']
building_probabilities['DS3']=building_probabilities['Extensive']-building_probabilities['Complete']
building_probabilities['DS4']=building_probabilities['Complete']

pf=building_probabilities
s = pd.Series(damage_state.map(DamageStateMap),name='dmg')
df_blg= pf.join(s)

result=building_data.join(df_blg)

result.type.value_counts(normalize=False)


# dmg=pd.read_csv('result.csv')
dmg=result 
damage_interval_keys=["DS0", "DS1", "DS2", "DS3", "DS4"]
failure_state_keys=["DS3", "DS4"]
num_samples=10
seed=101

import collections
import concurrent.futures
import numpy as np
import pandas as pd
from past.builtins import xrange
from typing import List


    def calc_probability_failure_value(ds_sample, failure_state_keys):
        count = 0
        func = {}
        for sample, state in ds_sample.items():
            if state in failure_state_keys:
                func[sample] = "0"
                count += 1
            else:
                func[sample] = "1"
        if len(ds_sample):
            return func, count / len(ds_sample)
        else:
            return func, np.nan

def sample_damage_interval(dmg, damage_interval_keys, num_samples, seed):
    ki = []
    dt = []
    for i in range(1, len(dmg)+1):
        ds = {}
        dmg_row = dmg.iloc[i-1:i]
        random_generator = np.random.RandomState(seed)
        for j in range(num_samples):
            # each sample should have a unique seed
            rnd_num = random_generator.uniform(0, 1)
            prob_val = 0
            flag = True
            for ds_name in damage_interval_keys:
                if rnd_num < prob_val + dmg_row[ds_name].values[0]:
                    ds[f'sample_{j}'] = ds_name
                    flag = False
                    break
                else:
                    prob_val += dmg_row[ds_name].values[0]
            if flag:
                print("Cannot determine MC damage state!")
                break
#         dt[f'damage_state_{i}'] = calc_probability_failure_value(ds, failure_state_keys)
        dt.append(calc_probability_failure_value(ds, failure_state_keys)[1])
        ki.append(dmg_row['id'].iloc[0])
    return dt, ki

# create dataframe based on return values
df = pd.DataFrame({
    'id': ki,
    'pf': dt
})
