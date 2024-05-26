# Fragility Curves for Buildings

fragility_curves = {
    'MSF1': {
        'Slight': {'mu': 124.474391, 'sigma': 0.1259},
        'Moderate': {'mu': 139.8541, 'sigma': 0.1106},
        'Extensive': {'mu': 144.416, 'sigma': 0.1097},
        'Complete': {'mu': 145.11, 'sigma': 0.1097}
    },
    'MSF2': {
        'Slight': {'mu': 119.0924, 'sigma': 0.1202},
        'Moderate': {'mu': 131.2626, 'sigma': 0.1067},
        'Extensive': {'mu': 134.96, 'sigma': 0.1072},
        'Complete': {'mu': 136.89, 'sigma': 0.1072}
    },
    'MMUH1': {
        'Slight': {'mu':127.345, 'sigma': 0.1522},
        'Moderate': {'mu': 142.408, 'sigma': 0.1433},
        'Extensive': {'mu': 169.355, 'sigma': 0.1288},
        'Complete': {'mu': 182.837, 'sigma': 0.1288}
    },
    'MMUH2': {
        'Slight': {'mu': 113.545, 'sigma': 0.1627},
        'Moderate': {'mu': 127.332, 'sigma': 0.1558},
        'Extensive': {'mu': 156.272, 'sigma': 0.1449},
        'Complete': {'mu': 183.222, 'sigma': 0.1196}
    },
    'MMUH3': {
        'Slight': {'mu': 127.027, 'sigma': 0.1544},
        'Moderate': {'mu': 140, 'sigma': 0.137},
        'Extensive': {'mu': 161.676, 'sigma': 0.1176},
        'Complete': {'mu': 182.6, 'sigma': 0.1176}
    },
    'MLRM1': {
        'Slight': {'mu': 132.6614, 'sigma': 0.1682},
        'Moderate': {'mu': 144.04, 'sigma': 0.1434},
        'Extensive': {'mu': 159.94, 'sigma': 0.1306},
        'Complete': {'mu': 176.708, 'sigma': 0.1306}
    },
    'MLRM2': {
        'Slight': {'mu': 108.72, 'sigma': 0.1609},
        'Moderate': {'mu': 117.707, 'sigma': 0.1532},
        'Extensive': {'mu': 122.107, 'sigma': 0.1576},
        'Complete': {'mu': 128.149, 'sigma': 0.1576}
    },
    'MLRI': {
        'Slight': {'mu': 103.772, 'sigma': 0.1442},
        'Moderate': {'mu': 108.755, 'sigma': 0.1332},
        'Extensive': {'mu': 116.186, 'sigma': 0.1318},
        'Complete': {'mu': 134.303, 'sigma': 0.1318}
    },
    'CERBL': {
        'Slight': {'mu': 135.43, 'sigma': 0.1684},
        'Moderate': {'mu': 150.9125, 'sigma': 0.1501},
        'Extensive': {'mu': 173.382, 'sigma': 0.1513},
        'Complete': {'mu': 358.489, 'sigma': 0.1513}
    },    
    'CERBM': {
        'Slight': {'mu': 98.869, 'sigma': 0.1058},
        'Moderate': {'mu': 106.697, 'sigma': 0.0829},
        'Extensive': {'mu': 124.81, 'sigma': 0.0708},
        'Complete': {'mu': 223.408, 'sigma': 0.0708}
    },
    'CERBH': {
        'Slight': {'mu': 96.3994, 'sigma': 0.1672},
        'Moderate': {'mu': 104.99, 'sigma': 0.1516},
        'Extensive': {'mu': 174.478, 'sigma': 0.0897},
        'Complete': {'mu': 259.874, 'sigma': 0.0897}
    },    
    'CECBL': {
        'Slight': {'mu': 99.176, 'sigma': 0.103},
        'Moderate': {'mu': 105.974, 'sigma': 0.0834},
        'Extensive': {'mu': 115.364, 'sigma': 0.0711},
        'Complete': {'mu': 184.915, 'sigma': 0.0711}
    },
    'CECBM': {
        'Slight': {'mu': 102.95, 'sigma': 0.1161},
        'Moderate': {'mu': 112.11, 'sigma': 0.095},
        'Extensive': {'mu': 133.86, 'sigma': 0.0949},
        'Complete': {'mu': 239.822, 'sigma': 0.0949}
    },
    'CECBH': {
        'Slight': {'mu': 92.73, 'sigma': 0.1368},
        'Moderate': {'mu': 101.038, 'sigma': 0.1153},
        'Extensive': {'mu': 127.281, 'sigma': 0.0939},
        'Complete': {'mu': 170.732, 'sigma': 0.0939}
    },
    'SPMBS': {
        'Slight': {'mu': 168.2078, 'sigma': 0.1297},
        'Moderate': {'mu': 168.2078, 'sigma': 0.1297},
        'Extensive': {'mu': 174.356, 'sigma': 0.1196},
        'Complete': {'mu': 231.25, 'sigma': 0.1196}
    },    
    'MHPHUD': {
        'Slight': {'mu': 128.9339, 'sigma': 0.139},
        'Moderate': {'mu': 136.6742, 'sigma': 0.1369},
        'Extensive': {'mu': 150.508, 'sigma': 0.1427},
        'Complete': {'mu': 231.25, 'sigma': 0.1427}
    }
}


#Fragility Curves for Electrical Poles

fragility_curves = {
    'PW': {
        'Fail': {'mu': 130.139, 'sigma': 0.1213}
    },
    'PS': {
        'Fail': {'mu': 130.504, 'sigma': 0.1352}
    }
}


def generate_fragility_curve(mu, sigma, damage_levels):
    fragility_curve = lognorm.cdf(damage_levels, s=sigma, scale=mu)
#     return fragility_curve / np.trapz(fragility_curve, dx=1e-3)  # Normalize to [0, 1]
    return fragility_curve
