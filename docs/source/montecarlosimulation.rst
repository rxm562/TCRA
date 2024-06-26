
.. raw:: latex

    \newpage

Monte Carlo Simulation
======================================
Monte Carlo Simulation is performed to estimate the probability of failure of buildings::

  bldg_result=result_blg_damage 
  damage_interval_keys=['DS0', 'DS1', 'DS2', 'DS3', 'DS4']
  failure_state_keys=['DS3', 'DS4']
  num_samples=10
  seed=101
  
  
  
  calculator = DamageProbabilityCalculator(failure_state_keys)
  dt, ki = calculator.sample_damage_interval(bldg_result, damage_interval_keys, num_samples, seed)



Fitting Failure Probabilities to Lognormal Distribution::

  df = pd.DataFrame(result_bldg.pf)
  # Lognormal fitting requires strictly positive values. Add a small constant to avoid log(0)
  epsilon = 1e-10
  values = df['pf'] + epsilon
  
  # Fit the lognormal distribution to the data
  shape, loc, scale = lognorm.fit(values, floc=0)
  
  # Print the parameters
  print(f"Shape: {shape}")
  print(f"Location: {loc}")
  print(f"Scale: {scale}")
  
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
  df = pd.DataFrame(result_bldg.pf)
  epsilon = 1e-10
  values = df['pf'] + epsilon
  
  # Fit lognormal distribution
  shape, loc, scale = lognorm.fit(values, floc=0)
  
  # Create range for plotting
  x = np.linspace(min(values), max(values), 100)
  
  # Calculate PDF and CDF
  pdf = lognorm.pdf(x, shape, loc=loc, scale=scale)
  cdf = lognorm.cdf(x, shape, loc=loc, scale=scale)
  
  # Plot
  fig, (ax1, ax2) = plt.subplots(2, 1, layout='constrained')
  ax1.plot(x, pdf, label='Fitted Lognormal Pf', color='blue')
  ax1.set_xlabel('Value')
  ax1.set_ylabel('frequency')
  # ax1.set_title('Probability Density Function')
  ax1.legend()
  
  ax2.plot(x, cdf, label='Fitted Lognormal Pf', color='blue')
  ax2.set_xlabel('Value')
  ax2.set_ylabel('% Cumulative')
  # ax2.set_title('Cumulative Distribution Function')
  ax2.legend()
  
  plt.show()


.. figure:: source/figures/mcs.png
   :scale: 50%
   :alt: Logo
