.. raw:: latex

    \newpage

Interactive Result Plotting
======================================

Interactive Folium map graphics can be generated using the 
function :func:`plot_interactive_map`. 
This function produces an interactive map using Folium, an open-source Python library for generating Leaflet maps. More information on Folium can be found at https://python-visualization.github.io/folium/.  
The map generated will overlay the node data onto a Leaflet map.


The following example demonstrates how to plot node damage data:

.. doctest::

    >>> import pandas as pd
    >>> from folium import Map
    >>> # Load or prepare node data
    >>> result_bldg = pd.DataFrame({
    ...     'x': [-106.6851, -106.5073, -106.6123],
    ...     'y': [35.1344, 35.0713, 35.0844],
    ...     'dmg': [0.1, 0.5, 0.9]
    ... })
    >>> # Extract node coordinates and damage attributes
    >>> node = result_bldg.loc[:, 'x':'y']
    >>> node_dmg = result_bldg.loc[:, 'dmg']
    >>> # Plot damage map
    >>> map = plot_interactive_map(node, node_dmg, node_size=5, node_cmap_bins='cut')
    >>> map.save('interactive_plot.png')
   
   Interactive Folium map graphic.
   
.. raw:: html
    
    The interactive Leaflet network graphic is included below.
    
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="_static/interactive_plot.html" frameborder="0" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>


**Fig 6.** Interactive Map on OpenStreetMap.
