"""
The tsnet.simulation.main module contains function to perform
the workflow of read, discretize, initial, and transient
simulation for the given .inp file.

"""

fragility_curves_epn = {
    'PW': {
        'Fail': {'mu': 130.139, 'sigma': 0.1213}
    },
    'PS': {
        'Fail': {'mu': 130.504, 'sigma': 0.1352}
    }
}
