### Damage Simulation

#Assign random seed
seed=1234
np.random.seed(seed)

#Building invetory dataframe
node = BlgW


# Function to estimate damage probabilities for all buildings
def estimate_damage(building_data):
    results = []
    for index, row in building_data.iterrows():
        building = row['id']
        building_type = row['type']
#         building_lat = row['Latitude']
#         building_lon = row['Longitude']
#         epicenter_distance = calculate_distance(epicenter_lat, epicenter_lon, building_lat, building_lon)
        # Define earthquake intensity based on magnitude and epicenter distance
        intensity = row['mph']

        # Calculate damage probabilities for the building
        fragility_curves_building = fragility_curves[building_type]
        building_probabilities = {}
        for damage_state, fragility_params in fragility_curves_building.items():
            fragility_curve = generate_fragility_curve(fragility_params['mu'], fragility_params['sigma'], intensity)
            building_probabilities[damage_state] = fragility_curve
#             building_probabilities[damage_state] = calculate_damage_probabilities(fragility_curve, intensity)

        results.append({**building_probabilities})
    return pd.DataFrame(results)


def sample_damage_state(Pr):
    p = pd.Series(data = np.random.uniform(size=Pr.shape[0]), index=Pr.index)

    damage_state = pd.Series(data=[None]* Pr.shape[0], index=Pr.index)

    for DS_names in Pr.columns:
        damage_state[p < Pr[DS_names]] = DS_names

    return damage_state


# Damage State Mapping
DamageStateMap = {None:0, 'Slight': 1, 'Moderate': 2, 'Extensive':3, 'Complete': 4}
damage_state.map(DamageStateMap)
