"""
The tcra functionality analysis module contains function to perform
social impacts analysis by connecting physical damage to social system.

"""


def calculate_fs(df, dmg_col, dmg_epn_col):
    """ this function estimates replacement cost by archetype using unit replacement cost per unit area. 
    cost_dict is required to be updated based on the local construction cost.
    
    Parameters
    ----------
    inp_file_name: 
        unit replacement cost, building footprint area, no. of story/floor.
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
