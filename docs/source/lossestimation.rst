.. raw:: latex

    \newpage

Loss Analysis
======================================
Loss due to physical damage is estimated in $USD::
  
  Cost=pd.read_csv('FinalCost.csv')
  
  Cost['id'] = Cost.index
  
  Cost=Cost.drop(columns=['LANDUSE', 'STRUCUSE', 'FLOOR','STRUCTYPE', 'REMARKS', 'STRUCNAME',
         'LOCALITY', 'BuildUse', 'StrType', 'BuildOcc', 'BuildID', 'type','cost(USD)', 'Total Cost'])
  
  df_cost=pd.merge(func_merge, Cost, on='id')
  
  # Apply the cost mapping function and calculate replacement cost of individual building
  df_cost = map_cost(df_cost)
  
  #DamageRatio Generate for Damaged Buildings
  result = damage_ratio(df_cost)
  
  result['PhyLoss']=result['RCost']*result['DRatio']
  
  TotalLoss=result.PhyLoss.sum()
  TotalLoss
