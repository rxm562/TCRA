import warnings
import time
import numpy as np
import pandas as pd
import fc
import folium
import matplotlib
import matplotlib.pylab as plt
import matplotlib.patches as mpatches
from scipy.spatial import distance
from scipy.stats import expon, lognorm
from matplotlib.colors import ListedColormap
from fc.Fragility import Fragility
from pyproj import Proj
from pyproj import Proj, transform


# Import Scenario Hurricane Track
data=pd.read_csv('InputTracks/Hur_91.csv')

Lat1=list()          #Latitute
Long1=list()         #Longitude
CP1=list()           #Central Pressure (millibar)
Δp1=list()           #Central Pressure Difference (millibar)
Rmax1=list()         #Radius to max wind speed (km)
B1=list()            #Holland Parameter
ρ1=list()            #Air depnsity
Ω1=list()            #Earth's angular velocty (rad/s)
for index, row in data.iterrows():
        Lat = row['Lat']
        Long = row['Long']
        CP = row['CP']
        Time= row['Time']
        Δp=1013-CP
        Rmax=np.exp(2.556-0.000050255*(float(Δp)**2)+0.042243032*float(Lat))
        B=1.881-0.00557*Rmax-0.01097*float(Lat)
        Lat1.append(Lat)
        Long1.append(Long)
        CP1.append(CP)
        Δp1.append(Δp)
        Rmax1.append(Rmax)
        B1.append(B)
        ρ=1.15
        Ω=0.00007292
        ρ1.append(ρ)
        Ω1.append(Ω)

Lat=list(Lat1)
Long= list(Long1)
CP= list(CP1)
Δp= list(Δp1)
Rmax=list(Rmax1)
B=list(B1)
ρ= list(ρ1)
Ω= list(Ω1)
pf = {'Lat':Lat,'Long':Long, 'CP':CP,'Δp':Δp,'Rmax':Rmax,'B':B,'ρ':ρ, 'Ω':Ω}
n=pd.DataFrame(pf)

# scenario - hurricane characteristics (e.g., CP: Central Pressure, R: Radius of max wind, B: Holland Parameter)
n.head()

