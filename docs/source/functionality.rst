====================
Functionality Analysis and Social Impacts
====================

Functionality Analysis of Buildings is performed by combining the physical damage outcomes of buildings and electrical serviceability. Following steps are needed.

1. Estimate physical damage to buildings: 
   0: Damage State ['None','Slight', 'Moderate'] is operable
   1: Damage State ['Extensive','Complete'] is non-operable
2. Estimate damage to electrical poles:
   0: Non Failure
   1: Failure
3. Identify the serviceability area of the electrical network using Voronoi polygons. This process requires geospatial analysis using Geographic Information Systems (GIS). Voronoi polygons are created through geospatial analysis to determine the service area of each electrical pole. Buildings fall within a specific Voronoi polygon depending on the electricity from the corresponding polygon. Once the damage or serviceability status of an electrical pole is known, geospatial analysis can determine the serviceability (0: No Service, 1: Service Active) of electrical power.
4. Combine operability of buildings and serviceability of electrical poles to determine the functionality of buildings.
   Fully Functional: Building is operable (1) and electrical service is active (1)
   Partially Functional: Building is operable (1) but no electrical service (0)
   Non Functional: Building is non-operable (0) and [lectrical service is active (1) or no electrical service (0)]

Summary Damage
-------------------------------
.. figure:: figures/functionality.png
   :scale: 25%
   :alt: Logo

**Fig 7.** Functionality Analysis.


===============
Social Impacts
===============

Social impacts are analyzed by connecting damage states outcomes with social characteristics by administrative boudaries. Population Census Data is a good source to estimate updated social characteristics.
