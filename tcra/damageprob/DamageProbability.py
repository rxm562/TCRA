import folium
import matplotlib.patches as mpatches
from scipy.spatial import distance
import collections
import concurrent.futures
from past.builtins import xrange
from typing import List



class DamageProbabilityCalculator:
    def __init__(self, failure_state_keys):
        self.failure_state_keys = failure_state_keys

    def calc_probability_failure_value(self, ds_sample):
        """Calculate the probability of failure given a sample of damage states."""
        count = 0
        func = {}
        for sample, state in ds_sample.items():
            if state in self.failure_state_keys:
                func[sample] = "0"
                count += 1
            else:
                func[sample] = "1"
        if len(ds_sample):
            return func, count / len(ds_sample)
        else:
            return func, np.nan

    def sample_damage_interval(self, bldg_result, damage_interval_keys, num_samples, seed):
        """Sample damage intervals for the given building results."""
        ki = []
        dt = []
        for i in range(len(bldg_result)):
            ds = {}
            dmg_row = bldg_result.iloc[i:i+1]
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
            dt.append(self.calc_probability_failure_value(ds)[1])
            ki.append(dmg_row['id'].iloc[0])
        return dt, ki
