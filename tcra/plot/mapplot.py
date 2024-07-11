"""
The tcra DamageProbabilityCalculator class estimates probabilites of damage states.

"""

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

def plot_interactive_map(node, node_attribute=None, node_size=5, node_cmap_bins='cut', node_cmap=None, link_cmap=None):
    """ 
    this function allows user to plot results interactively on OpenStreetMap.
    -------------------
    inp_file_name: building invetory with result.
    """
    if node_cmap is None:
        node_cmap = ['cornflowerblue', 'forestgreen', 'gold', 'firebrick']
    if link_cmap is None:
        link_cmap = ['cornflowerblue', 'forestgreen', 'gold', 'firebrick']
    
    if node_attribute is not None:
        if isinstance(node_attribute, list):
            node_cmap = ['red']
        else:
            node_attribute = pd.Series(node_attribute)
            if node_cmap_bins == 'cut':
                node_colors, _ = pd.cut(node_attribute, len(node_cmap), labels=node_cmap, retbins=True)
            elif node_cmap_bins == 'qcut':
                node_colors, _ = pd.qcut(node_attribute, len(node_cmap), labels=node_cmap, retbins=True)

    m = folium.Map(location=[node.y.mean(), node.x.mean()], zoom_start=12)
    folium.TileLayer('cartodbpositron').add_to(m)
    folium.TileLayer('Stamen Toner').add_to(m)
    folium.TileLayer('stamenwatercolor').add_to(m)
    folium.TileLayer('openstreetmap').add_to(m)

    if node_size > 0:
        for index, row in node.iterrows():    
            loc = (row['y'], row['x'])
            radius = node_size
            color = 'black'
            if node_attribute is not None and index in node_colors.index:
                color = node_colors[index]
            folium.CircleMarker(loc, color=color, fill=True, fill_color=color, radius=1, fill_opacity=0.7, opacity=0.7).add_to(m)

    folium.LayerControl().add_to(m)

    return m
