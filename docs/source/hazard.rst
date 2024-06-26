.. raw:: latex

    \newpage

Scenario Cyclone Hazard Analysis
======================================

The scenario cyclone-hazard estimates peak gust wind intensity at sites using a wind field model that includes
    surface pressure field and a system translated speed (Vickery and Wadhera 2008). The wind field model estimates the spatial variation of the wind speed over a large area (Salman and Li 2018). 
  
  
Among existing wind field models available (i.e., Russell 1969; Holland 1980; Batts 1984; Vickery et al. 2000; Snaiki and Wu 2017), Holland (1980)’s wind field model allows estimating spatially distributed wind speeds of a hurricane (Vickery and Wadhera 2008). Holland parameter is widely used in past studies and used in this study for estimating the peak wind speed for buildings at any given time during a cyclone. A scenario cyclone is used to estimate spatial variation of peak wind intensities at sites. Scenario-cyclone characteristics can be obtained from historical data or simulating a synthetic model. The appropriate scenario event for a particular region can be selected based on the frequency of hazard occurrence and the community's risk perspective (Lin and Wang 2016). The HURDAT2 database used in this study provides past hurricane track location, time of occurrence, maximum wind speed, landfall location, storm category, central pressure at a 6-hr of interval. This data can be further linearly interpolated to obtain a more refined record (Salman and Li 2018). The strongest hurricane wind occurs at the eye wall, and wind intensity decays as the location moves away from the hurricane center (Xu and Brown 2008). Gradient wind speed at building location is estimated using the radial wind profile model provided by Holland (1980) as::

    V_G=[(R_max/r)^B∙((B∆p∙exp[-(R_max/r)^B ])/ρ)+(r^2 f^2)/4]^(1/2)-rf/2

where Rmax is the radius of the maximum wind speed, r is the distance from hurricane eye to the building site, B is the Holland pressure profile parameter, ∆p is the central pressure difference estimated subtracting central pressure from atmospheric pressure of 1013 millibars (Xu and Brown 2008), ρ is the air density, and f is the Coriolis parameter. The radius of the maximum wind is estimated using the model provided by FEMA (2012), as below::

    ln⁡〖R_max 〗=2.556-0.000050255〖∆p〗^2+0.042243032ψ

where ψ is the storm latitude and ∆p is the central pressure difference. Holland pressure profile parameter is estimated using the model developed by Powell et al. (2005), as follows::

    B=1.881-0.00557R_max-0.01097ψ

The Coriolis parameter is determined by the following expression (Xu and Brown)::

    f=2Ω∙sinφ

where φ is the local latitude and Ω is the earth’s angular velocity (7.292x10E-5 rad/s).

Building performance analysis requires converting gradient wind speed to surface wind speed. A conversion factor that ranges from 0.8 to 0.86 depending on weaker to strong hurricanes is used to convert gradient wind speed to surface wind speed (Vickery et al. 2000; 2009). Structural damage during a hurricane is generally associated with the peak gust wind speed. Hence, the surface wind speed is further converted to 3-s gust wind speed, multiplying surface wind speed by a gust wind factor of 1.287 with a standard deviation of 0.02 (Xu and Brown 2008; Salman and Li 2018).


.. literalinclude:: ../examples/Tnet1_valve_closure.py
   :lines: 5
   
The following code can be used to compute peak ground acceleration, peak ground velocity, and repair rate:

.. literalinclude:: ../examples/Tnet1_valve_closure.py
   :lines: 10-17



This module requires cyclone input track.  

.. table:: cyclone input track.

   ==============================  ===================================================================================================================
   Column Title                    Description
   ==============================  ===================================================================================================================
   sl                              Row number
   Time                            Time of cyclone (time step - i)
   Lat                             Latitute of cyclone eye
   Long                            Longitude of cyclone eye
   CP                              Central Pressure Difference
   ==============================  ===================================================================================================================

.. table:: building input data.

   ==============================  ===================================================================================================================
   Column Title                    Description
   ==============================  ===================================================================================================================
   id                              Building unique identifier
   Lat                             Latitute of building
   Long                            Longitude of building
   Floor                           No of storey
   Area                            Area of the building
   type                            Structural archetype
   Occupancy                       Building use

   ==============================  ===================================================================================================================

Run hazard module to estimate the cyclone parameters and intensity at buildings::

    hurricane_parameters = HurricaneParameters(track_df)
    df_track = hurricane_parameters.estimate_parameters()
    df_bdg_wind, VG = hurricane_parameters.calculate_wind_speeds(df_track, blg)
