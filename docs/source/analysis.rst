====================
Analysis
====================

Example 1
-----------------------------

This example shows how to simulate the closure of a
TSNet package:



Summary Damage
-------------------------------
.. figure:: figures/damage.png
   :scale: 25%
   :alt: Logo

.. code-block:: console

   import folium
   import matplotlib.pyplot as plt
   from matplotlib.colors import ListedColormap
   
   def plot_scatter(plot_data, x_col, y_col, color_col, figsize=(4, 3), color_map=None, s=0.5, xlabel='longitude', ylabel='latitude', colorbar_label='pf', save_path=None):
       """
       Plots a scatter plot from the given DataFrame with specified x, y, and color columns.
   
       Parameters:
       plot_data (pd.DataFrame): DataFrame containing the data
       x_col (str): Column name for x coordinates
       y_col (str): Column name for y coordinates
       color_col (str): Column name for coloring the scatter points
       figsize (tuple): Size of the figure (width, height)
       color_map: Colormap to use for the scatter plot (default is a predefined colormap)
       s (float): Marker size
       xlabel (str): Label for the x-axis
       ylabel (str): Label for the y-axis
       colorbar_label (str): Label for the color bar
       save_path (str): Path to save the figure (default is None, meaning not saving the figure)
       """
       if color_map is None:
           color_map = ListedColormap(['blue', 'green', 'yellow', 'orange', 'red'])
   
       fig = plt.figure(figsize=figsize)
       scatter = plt.scatter(plot_data[x_col], plot_data[y_col], c=plot_data[color_col], cmap=color_map, s=s)
       cbar = plt.colorbar(scatter)
       cbar.set_label(colorbar_label)
       plt.xlabel(xlabel)
       plt.ylabel(ylabel)
       if save_path:
           plt.savefig(save_path,bbox_inches='tight', dpi=300)
       plt.show()


