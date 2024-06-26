"""
The tcra fragility_rehab module contains function to perform
the workflow of read, discretize, initial, and transient
simulation for the given .inp file.

"""

def damage_ratio(data):
    d_ratio = []
    for _, row in data.iterrows():
        mean_val = params.get(row['Occupancy'], {}).get(row['dmg'], 0)
        d_ratio.append(mean_val)
    
    data['DRatio'] = d_ratio
    return data
