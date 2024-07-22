"""
The tcra social analysis module contains function to perform
social impacts analysis by connecting physical damage to social system.

"""

def categorize_area(area):
    
    """ 
    this function defines base function to estimate number of units in a building.
    
    Parameters
    ----------
    area : 
        building footprint area
    Floor :
        no. of story/floor.

    Returns
    -------
    num : returning unit number
    
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
    """ 
    this function assign no of units to building
    
    Parameters
    ----------    
    df :
        inventory 
    area : 
        building footprint area
    Floor :
        no. of story/floor.

    Returns
    -------
    num : returning unit number
    
    """
    return [categorize_area(area) for area in df['area']]
