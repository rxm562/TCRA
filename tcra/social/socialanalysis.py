"""
The tcra social analysis module contains function to perform
social impacts analysis by connecting physical damage to social system.

"""

def categorize_area(area):
    
    """ this function estimates replacement cost by archetype using unit replacement cost per unit area. 
    cost_dict is required to be updated based on the local construction cost.
    
    Parameters
    ----------
    inp_file_name: 
        area, building footprint area, no. of story/floor.
    """
    
    if area < 110:
        return 1
    elif area <= 195:
        return 2
    elif area <= 300:
        return 3
    else:
        return 4

def categorize_areas(df):
    """ this function estimates replacement cost by archetype using unit replacement cost per unit area. 
    cost_dict is required to be updated based on the local construction cost.
    
    Parameters
    ----------
    inp_file_name: 
        unit replacement cost, building footprint area, no. of story/floor.
    """
    return [categorize_area(area) for area in df['area']]
