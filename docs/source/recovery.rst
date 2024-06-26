.. raw:: latex

    \newpage

Recovery Simulation
======================================

Using the damage states results, and expected recovery time from Appendix A, Monte Carlo Simulation is performed to estimate recovery of buildings::

  output_building=result
  output_building.pf[output_building.pf>0.39].shape[0]/output_building.pf.shape[0]
  
  result_dp=result.drop(columns=['dmg_bldg', 'dmg_pole', 'F_blg', 'Functionality', 'Slight', 'Moderate', 'Extensive', 'Complete',
   'x','y', 'mph', 'type', 'Occupancy', 'LS1', 'LS2', 'LS3', 'LS4', 'DS0','DS1', 'DS2', 'DS3', 'DS4', 
   'dmg', 'RT_bdg', 'RT_EPN', 'RT','DRatio', 'PhyLoss'])
  
  rr_values = [1.0, 1.1, 1.2, 1.4, 1.5]  # Example values, you can adjust as needed
  
  # Initialize list to store TotalLoss for each rr_value
  ds=[]
  total_loss_list = []
  
  pf_threshold=0.39
  
  # Define a range of rr_values
  
  # Iterate over each rr_value
  for rr_value in rr_values:
      # Assuming the following code block is within the loop:
      rr_value
      output_building=result
      df=output_building
      df['ntype'] = df.apply(lambda row: f"{row['type']}{'_R'}" if row['pf'] >pf_threshold else row['type'], axis=1)
      df=df.drop(columns=['type'])
      df.rename(columns={'ntype': 'type'}, inplace=True)
      fragility_curves_rehab = rehab_fragility_curves(rr_value)
      DStates=['Slight','Moderate','Extensive', 'Complete']
      fra= FragilityAnalysis(fragility_curves_rehab)
      Pr_rehab = fra.estimate_damage(df)
      damage_state_rehab = fra.sample_damage_state(Pr_rehab, DStates,101)
      # Damage State Mapping
      DamageStateMap = {None:0, 'Slight': 1, 'Moderate': 2, 'Extensive':3, 'Complete': 4}
      damage_state_rehab=damage_state_rehab.map(DamageStateMap)
      # Adding columns to the probability DataFrame
      DS_Prob=Pr_rehab
      DS_Prob['LS1'] = DS_Prob['Slight']
      DS_Prob['LS2'] = DS_Prob['Moderate']
      DS_Prob['LS3'] = DS_Prob['Extensive']
      DS_Prob['LS4'] = DS_Prob['Complete']
      DS_Prob['DS0'] = 1 - DS_Prob['Slight']
      DS_Prob['DS1'] = DS_Prob['Slight'] - DS_Prob['Moderate']
      DS_Prob['DS2'] = DS_Prob['Moderate'] - DS_Prob['Extensive']
      DS_Prob['DS3'] = DS_Prob['Extensive'] - DS_Prob['Complete']
      DS_Prob['DS4'] = DS_Prob['Complete']
      s = pd.Series(damage_state_rehab,name='dmg')
      blg_dmg_rehab= DS_Prob.join(s)
      ## Cost Info
      blg_dmg_rehab=pd.merge(blg_dmg_rehab, result_dp, on='id')
      result_p = damage_ratio(blg_dmg_rehab)
      result_p['PhyLoss']=result_p['RCost']*result_p['DRatio']
      TotalLoss=result_p.PhyLoss.sum()
      ds.append(damage_state_rehab.value_counts())
      total_loss_list.append(TotalLoss)
