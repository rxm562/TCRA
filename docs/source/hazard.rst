.. raw:: latex

    \newpage

Scenario Cyclone Hazard Analysis
======================================

The scenario cyclone-hazard estimates peak gust wind intensity at sites using a wind field model that includes
    surface pressure field and a system translated speed (Vickery and Wadhera 2008). The wind field model estimates the spatial variation of the wind speed over a large area (Salman and Li 2018). 
  
  Among existing wind field models available (i.e., Russell 1969; Holland 1980; Batts 1984; Vickery et al. 2000; Snaiki and Wu 2017), Holland (1980)’s wind field model allows estimating spatially distributed wind speeds of a hurricane (Vickery and Wadhera 2008). Holland parameter is widely used in past studies and used in this study for estimating the peak wind speed for buildings at any given time during a cyclone. A scenario cyclone is used to estimate spatial variation of peak wind intensities at sites. Scenario-cyclone characteristics can be obtained from historical data or simulating a synthetic model. The appropriate scenario event for a particular region can be selected based on the frequency of hazard occurrence and the community's risk perspective (Lin and Wang 2016). The HURDAT2 database used in this study provides past hurricane track location, time of occurrence, maximum wind speed, landfall location, storm category, central pressure at a 6-hr of interval. This data can be further linearly interpolated to obtain a more refined record (Salman and Li 2018). The strongest hurricane wind occurs at the eye wall, and wind intensity decays as the location moves away from the hurricane center (Xu and Brown 2008). Gradient wind speed at building location is estimated using the radial wind profile model provided by Holland (1980) as




.. literalinclude:: ../examples/Tnet1_valve_closure.py
   :lines: 5
   
The following code can be used to compute peak ground acceleration, peak ground velocity, and repair rate:

.. literalinclude:: ../examples/Tnet1_valve_closure.py
   :lines: 10-17
