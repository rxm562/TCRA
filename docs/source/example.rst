.. highlight:: shell

============
Illustrative Example
============

TCRA is a Python package designed to perform scenario-based tropical cyclone risk analysis. The software includes capability to:

1. Scenario-hazard estimation: peak gust wind speed at sites
2. Vulnerability analysis using fragility curves
3. Damage Simulation using peak gust wind and fragility curves of structures
4. Monte Carlo Simulation is performed for estimating probability of failure
5. Interactive outputs plotting on openstreetmap


.. code-block:: console

  import warnings
  import numpy as np
  import pandas as pd
  import matplotlib
  import matplotlib.pylab as plt
  from matplotlib.colors import ListedColormap
  from scipy.stats import expon, lognorm
  
  import tcra
  from tcra.Hurricane import HurricaneParameters
  from tcra.fragility_curves import fragility_curves
  from tcra.fragility_curves_epn import fragility_curves_epn
  from tcra.DamageAnalysis import FragilityAnalysis
  from tcra.MonteCarloSimulation import DamageProbabilityCalculator
  from tcra.fragility_rehab import rehab_fragility_curves
  from tcra.Plot import plot_scatter
  from tcra.Interactive import plot_interactive_map


1. Hurricane Track Import, Building Data Import, Estimating Peak Velocity
---------------------

.. code-block:: console

  # Import Hurricane Historical Track
  track_df=pd.read_csv('InputTracks/Hur_91.csv')
  
  # this data includes time, lat, long and central pressure
  track_df.head(2)
  
  # Import Building Data
  blg=pd.read_csv('Buildings_Ctg2.csv')

  blg.head(2)

2. Scenario Hurricane - Wind Speed Simulation
---------------------

.. code-block:: console

  hurricane_parameters = HurricaneParameters(track_df)
  df_track = hurricane_parameters.estimate_parameters()
  df_bdg_wind, VG = hurricane_parameters.calculate_wind_speeds(df_track, blg)
  df_bdg_wind.head(2)
  df_bdg_wind.shape
  df_bdg_wind.head(2)
  df_bdg_wind.drop(['ind'], axis=1, inplace=True)


2. Plotting Peak Gust Wind Speed for All Buildings
---------------------

  .. code-block:: console

  VG.plot.line(legend=None)
  plt.xlabel('Time Steps')
  plt.ylabel('Wind Speed(mph)')
  plt.show()
  # plt.savefig('Cyclone_Hazard.png', dpi=300)

3. Damage Simulation
---------------------

.. code-block:: console

  from tcra.fragility_curves import fragility_curves
  DStates=['Slight','Moderate','Extensive', 'Complete']
  
  # Example usage
  fra= FragilityAnalysis(fragility_curves)
  Pr = fra.estimate_damage(building_data)
  damage_state = fra.sample_damage_state(Pr, DStates)
  
  # Mapping damage states
  DamageStateMap = {None: 0, 'Slight': 1, 'Moderate': 2, 'Extensive': 3, 'Complete': 4}
  damage_state = damage_state.map(DamageStateMap)
  
  DS_Prob=Pr
  
  # Adding columns to the probability DataFrame
  DS_Prob['LS1'] = DS_Prob['Slight']
  DS_Prob['LS2'] = DS_Prob['Moderate']
  DS_Prob['LS3'] = DS_Prob['Extensive']
  DS_Prob['LS4'] = DS_Prob['Complete']
  DS_Prob['DS0'] = 1 - DS_Prob['Slight']
  DS_Prob['DS1'] = DS_Prob['Slight'] - DS_Prob['Moderate']
  DS_Prob['DS2'] = DS_Prob['Moderate'] - DS_Prob['Extensive']
  DS_Prob['DS3'] = DS_Prob['Extensive'] - DS_Prob['Complete']
  DS_Prob['DS4'] = DS_Prob['Complete']
  
  s = pd.Series(damage_state,name='dmg')
  result_blg_damage= DS_Prob.join(s)
  
  result_blg_damage.head(2)

3. Plotting Wind Speed
---------------------

.. code-block:: console

  plot_scatter(result_blg_damage, 'x', 'y', 'mph', save_path='wind_speed.png')
