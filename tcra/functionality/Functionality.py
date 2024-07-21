import pandas as pd

def calculate_fs(df, dmg_col, dmg_epn_col):
    def determine_fs(row):
        if row[dmg_col] <= 2 and row[dmg_epn_col] == 0:
            return 2
        elif row[dmg_col] <= 2 and row[dmg_epn_col] == 1:
            return 1
        else:
            return 0

    df['FS'] = df.apply(determine_fs, axis=1)
    return df
