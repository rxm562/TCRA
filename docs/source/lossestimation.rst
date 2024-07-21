.. raw:: latex

    \newpage

Loss Analysis: Buildings Repair Cost
======================================
Moneytary loss ($) due to buildings physical damage is estimated based on the unit cost of buildings, building footprint area, no. of story, and damage ratio. The replacement value of the building is estimated by knowing building area multiplying by no. of story and unit cost of buildings. Unit cost of buildings for a specific structural type can be estimated based on using construction cost guidelines (using local construction cost values). The total repair cost is estimated based on the structural damage ratio as a function of building replacement cost.


**Following is an example of loss estimation**::

    # Apply the cost mapping function and calculate replacement cost of individual building, 
    # map_cost: estimates unit cost and replacement cost, blg: building invetory
      
    df_cost = map_cost(blg)

    # Merging cost and damage outputs (df_ds: building damage states)
    df_cost_dmg=pd.merge(df_cost, df_ds, on='id')

    # Generating Damage Ratio for each building
    Loss = damage_ratio(df_cost_dmg)
    
    # Estimating Physical Damage Repair Cost ($) for each building
    Loss['PhyLoss']=Loss['RCost']*Loss['DRatio']
      
    # Project Total Loss due to Physical Damage in $USD
    TotalLoss=Loss.PhyLoss.sum()
    TotalPhyLoss=Loss.PhyLoss.sum()
    print(f"{TotalLoss / 1000000:.1f} Million USD")
