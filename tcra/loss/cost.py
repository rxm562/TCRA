"""
The tcra cost module estimates building replacement cost that required for loss estimation.

"""

# Dictionary to map building types and numerical floors to cost in USD
cost_dict = {
    'MSF1': {1: 488},
    'MSF2': {2: 1343, 3: 2072},
    'MMUH1': {1: 451},
    'MMUH2': {2: 1522},
    'MMUH3': {3: 1144, 4: 1439},
    'MLRM1': {1: 780, 2: 866},
    'MLRM2': {3: 1225},
    'MLRI': {1: 512, 2: 800},
    'CERBL': {1: 569, 2: 921, 3: 1278},
    'CERBM': {4: 1614, 5: 1979, 6: 2348, 7: 2715},
    'CERBH': {8: 3082, 9: 3447, 10: 3814, 11: 4182, 12: 4549, 13: 4917, 14: 5285, 15: 5650, 16: 6017},
    'CECBL': {1: 537, 2: 865, 3: 1198},
    'CECBM': {4: 1535, 5: 1875, 6: 2219, 7: 2561},
    'CECBH': {8: 2903, 9: 3245, 10: 3589, 11: 3936, 12: 4283, 13: 4630, 14: 4976, 15: 5320, 16: 5664},
    'SPMBS': {1: 797, 2: 1290, 3: 1789},
    'MHPHUD': {1: 501}
}

# Function to map the cost and calculate FCost
def map_cost(data):
    """ this function estimates replacement cost by archetype using unit replacement cost per unit area. 
    cost_dict is required to be updated based on the local construction cost.
    -------------------
    inp_file_name: unit replacement cost, building footprint area, no. of story/floor.
    """
    
    costs = []
    for _, row in data.iterrows():
        archetype = row['type']
        try:
            floor = int(row['FLOOR'])  # Ensure 'FLOOR' is converted to integer
        except (ValueError, TypeError):
            costs.append(None)
            continue
        cost = cost_dict.get(archetype, {}).get(floor, None)
        costs.append(cost)
    data['UC'] = costs
    data['RCost'] = data['UC'] * data['area']
    return data
