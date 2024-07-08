.. raw:: latex

    \newpage

Scenario Cyclone Hazard Analysis
======================================
.. include:: <isonum.txt>

**TCRA Scenario Hazard Analysis Basis**:

 
    The scenario cyclone-hazard estimates peak gust wind intensity at sites using a wind field model that includes surface pressure field and a system translated speed (Vickery and Wadhera 2008). The wind field model estimates the spatial variation of the wind speed over a large study area (Salman and Li 2018). 
    
    Holland (1980)’s wind field model used to estimate wind speeds of a hurricane. The appropriate scenario event for a particular region can be selected based on the frequency of hazard occurrence and the community's risk perspective. The HURDAT2 database is a good source that used in this study to obtain recorded past hurricane tracks chracteristics (i.e., location, time of occurrence, maximum wind speed, landfall location, storm category, central pressure). The strongest hurricane wind occurs at the eye wall, and wind intensity decays as the location moves away from the hurricane center (Xu and Brown 2008). Gradient wind speed at building location is estimated using the radial wind profile model provided by Holland (1980)


**Scenario Hazard Analysis Inputs**:

This module requires (1) cyclone input track, and (2) targeted structural inventory (i.e., buildings) location to estimate gust wind speed at structural inventory sites. Following table shows input characteristics of cyclone input track and buildings.

.. table :: cyclone input track.

   ==============================  ===================================================================================================================
   Column Title                    Description
   ==============================  ===================================================================================================================
   sl                              Row number
   Time                            Time of cyclone (time step - i)
   Lat                             Latitute of cyclone eye
   Long                            Longitude of cyclone eye
   CP                              Central Pressure Difference
   ==============================  ===================================================================================================================

.. table :: building input data.

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

**Running Hazard Analysis**:

    1. **HurricaneParameters**: this model computes cyclone hazard
    2. **estimate_parameters**: this function estimates parameters for input track
    3. **calculate_wind_speeds**: this function estimates wind speed at sites

Following is an example of running hazard module to estimate the cyclone parameters and intensity at buildings::

    # track_df: hurricane track input dataframe (see table - cyclone input track), df_track: estimated hazard parameters, 
    # and blg: buildings inventory (see table - building input data), df_bdg_wind: estimated wind speed, VG: gust wind speed.
    hurricane_parameters = HurricaneParameters(track_df)
    df_track = hurricane_parameters.estimate_parameters()
    df_bdg_wind, VG = hurricane_parameters.calculate_wind_speeds(df_track, blg)
