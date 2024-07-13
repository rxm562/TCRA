.. raw:: latex

    \newpage

Loss Analysis: Buildings Repair Cost
======================================
Moneytary loss ($) due to buildings physical damage is estimated based on the unit cost of buildings, building footprint area, no. of story, and damage ratio. The replacement value of the building is estimated by knowing building area multiplying by no. of story and unit cost of buildings. Unit cost of buildings for a specific structural type can be estimated based on using construction cost guidelines (using local construction cost values). The total repair cost is estimated based on the structural damage ratio as a function of building replacement cost.


Following is an example of loss estimation::

  
  # Apply the cost mapping function and calculate replacement cost of individual building, 
  # map_cost: estimates unit cost and replacement cost, df_cost: building invetory
  
  df_cost = map_cost(df_cost)
  
  # Generate structural damage ratio in terms of total replacement cost of buildings
  result = damage_ratio(df_cost)
  
  result['PhyLoss']=result['RCost']*result['DRatio']
  
  TotalLoss=result.PhyLoss.sum()
