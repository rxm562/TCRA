import pandas as pd

def categorize_area(area):
    if area < 110:
        return 1
    elif area <= 195:
        return 2
    elif area <= 300:
        return 3
    else:
        return 4

def categorize_areas(df):
    return [categorize_area(area) for area in df['area']]
