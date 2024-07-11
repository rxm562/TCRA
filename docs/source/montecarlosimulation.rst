
.. raw:: latex

    \newpage

Damage Probability Estimation
======================================
Monte Carlo Simulation is performed to estimate the probability of failure of buildings. In a single stochastic realization, damage state is simulted by comparing generated random number on uniform distribution [0,1], fragility curves and wind speed intensity. Through a Monte Carlo simulation, using the same hazard intensity, random number is generated multiple times (say, n-times) and then probability of failure is defined by the number of times structure sustain failure (for building damage states extensive (DS3) or complete (DS4)) out of multiple runs (n-times).


Following is an example of damage probability estimation::

  # bldg_result: building invetory contains damage states result,  

  damage_interval_keys=['DS0', 'DS1', 'DS2', 'DS3', 'DS4']
  failure_state_keys=['DS3', 'DS4']
  num_samples=10
  seed=101

  calculator = DamageProbabilityCalculator(failure_state_keys)
  dt, ki = calculator.sample_damage_interval(bldg_result, damage_interval_keys, num_samples, seed)



Fitting Failure Probabilities to Lognormal Distribution::

  df = pd.DataFrame(result_bldg.pf)
  epsilon = 1e-10 # Lognormal dist requires positive values. Add a small constant to avoid log(0)
  values = df['pf'] + epsilon
  
  # Fitting pf for all buildings to lognormal dist
  shape, loc, scale = lognorm.fit(values, floc=0)
  
  # Generate some samples from the fitted lognormal distribution for comparison
  samples = lognorm.rvs(shape, loc=loc, scale=scale, size=len(df))
  
  # Create a DataFrame to compare original values and generated samples
  comparison_df = pd.DataFrame({
      'Original Values': values,
      'Fitted Lognormal Samples': samples
  })
  
  #comparison_df.head()

PDF and CDF of Failure Probabilites::

  # Prepare data
  plot_lognormal_distribution(result_bldg)

.. figure:: figures/mcs.png
   :scale: 40%
   :alt: Logo
