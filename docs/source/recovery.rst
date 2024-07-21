.. raw:: latex

    \newpage

Recovery Simulation
======================================

Recovery (repair time) is sumulated for damaged buildings based on the level of damaged sustained by the buildings, building occupancy type and recovery time recommended by FEMA. [R1]_ FEMA (2020) guideline provides expected mean repair time by building occupancy type for various damage states. To account the uncertainity in recovery time, a COV was assumed for correspond to mean recovery time. More information on the initializer can be found in the API documentation, under :class:`~tcra.recovery.recovery` section.

**Following as an example of recovery simulation**::

    # recovery of building, data: building invetory with damage state and occupancy type.
    building_dmg= pd.merge(blg, df_ds, on='id')

    # Simulating Recovery Time of Buildings (RT_bldg: recovery time of building)
    recovery_time = rep(result_blg_dmg)
    result_blg_dmg['RT_bdg'] = list(recovery_time)

    # Recovery Analysis - Multiple Recovery Scenarios using Monte Carlo Simulation 
    # (x: time steps, all, mean, min, and max of recovery curves from silumations)
    x, all_simulations, mean, minimum, maximum = recovery_monte_carlo_simulation(result_blg_dmg, num_simulations=100000)
    
    # Recovery of electrical pole, epn_data: epn invetory with failure state
    df_recovery_epn=rep_EPN(epn_data)

.. figure:: figures/recovery_example.png
   :scale: 40%
   :alt: Logo

**Fig 4.** Example Recovery Curves.
