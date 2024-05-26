# Plot output data interactively
node=pd.DataFrame(result.drop(['id', 'LAYER', 'type', 'Slight', 'Moderate', 'Extensive',
       'Complete', 'dmg'], axis = 1))


dt = pd.DataFrame(result.drop(['id', 'x', 'y', 'LAYER', 'type', 'Slight', 'Moderate', 'Extensive',
       'Complete'], axis = 1))




dt=dt.transpose()


node_attribute=dt.iloc[0,:]


node['xx']=node.x
node_size=5
node_range=[None,None]
node_cmap_bins = 'cut'
node_cmap=['cornflowerblue', 'forestgreen', 'gold', 'firebrick'] 
link_cmap=['cornflowerblue', 'forestgreen', 'gold', 'firebrick']


if node_attribute is not None:
    if isinstance(node_attribute, list):
        node_cmap=['red']
    node_attribute = node_attribute
    node_attribute = pd.Series(node_attribute)
    if node_range[0] is not None:
        node_attribute[node_attribute < node_range[0]] = node_range[0]
    if node_range[1] is not None:
        node_attribute[node_attribute > node_range[1]] = node_range[1]
    if node_cmap_bins == 'cut':
        node_colors, node_bins = pd.cut(node_attribute, len(node_cmap), 
                                            labels=node_cmap, retbins =True)
    elif node_cmap_bins == 'qcut':
        node_colors, node_bins = pd.qcut(node_attribute, len(node_cmap), 
                                             labels=node_cmap, retbins =True)

#     center = pd.DataFrame(pos).mean(axis=1)
m = folium.Map(location=[node.y.mean(), node.xx.mean()], zoom_start=10)
folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('cartodbpositron').add_to(m)
folium.TileLayer('Stamen Toner').add_to(m)
folium.TileLayer('stamenterrain').add_to(m)
folium.TileLayer('stamenwatercolor').add_to(m)
folium.TileLayer('cartodbdark_matter').add_to(m)

if node_size > 0:
    for index, row in node.iterrows():    
        loc = (row['y'], row['xx'])
        radius = node_size
        color = 'black'       
        if node_attribute is not None:
            if index in node_attribute:
                color = node_colors[index]
            else:
                radius = 0.1
        folium.CircleMarker(loc, color=color, fill=True,fill_color=color, radius=1, fill_opacity=0.7, opacity=0.7).add_to(m)

folium.LayerControl().add_to(m)

m
