"""
The tcra functionality analysis module contains function to estimate functionality
of buildings by connecting performance of building and electrical system.

"""


def calculate_fs(df, dmg_col, dmg_epn_col):
    """ 
    this function estimates functionality of buildings.
            
    Parameters
    ----------
    dmg_col : building inventory with damage state of building
       
    dmg_epn_col : electrical system inventory with failure state

    Returns
    -------
    FS : functionality of building
        
    """
    def determine_fs(row):
        if row[dmg_col] <= 2 and row[dmg_epn_col] == 0:
            return 2
        elif row[dmg_col] <= 2 and row[dmg_epn_col] == 1:
            return 1
        else:
            return 0

    df['FS'] = df.apply(determine_fs, axis=1)
    return df
