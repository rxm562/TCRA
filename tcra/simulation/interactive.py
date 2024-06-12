import pandas as pd
import folium

def plot_interactive_map(node, node_attribute=None, node_size=5, node_cmap_bins='cut', node_cmap=None, link_cmap=None):
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
