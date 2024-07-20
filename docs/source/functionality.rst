====================
Functionality Analysis
====================

Functionality Analysis of Buildings is performed by combining the physical damage outcomes of buildings and electrical serviceability. Following steps are needed.

1. Estimate physical damage to buildings: 
   0: Damage State ['None','Slight', 'Moderate'] is operable
   1: Damage State ['Extensive','Complete'] is non-operable
2. Estimate damage to electrical poles:
   0: Non Failure
   1: Failure
3. Identify the serviceability area of the electrical network using Voronoi polygons. This process requires geospatial analysis using Geographic Information Systems (GIS). Voronoi polygons are created to determine the service area of each electrical pole. Buildings fall within a specific Voronoi polygon, receiving electricity from the corresponding pole. Once the damage or serviceability status of an electrical pole is known, geospatial analysis can determine the serviceability (0: No Service, 1: Service Active) of electrical power.

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
Social Impact Estimation
===============

Social impacts are analyzed by connecting damage state outcomes with social characteristics by administrative boundaries. Population census data is a good source to estimate updated social characteristics. The number of household dislocations and the number of educational, governmental, and industrial buildings that are non-operable are estimated by connecting physical damage with household information. The number of housing units in a building in this study was estimated based on the building footprint and the number of floors. A residential building with an area greater than 300 square meters is assumed to have four households. Similarly, residential buildings with areas of 110, 195, and 300 square meters are assumed to have 1, 2, and 3 housing units, respectively.


