"""
The tsnet.simulation.main module contains function to perform
the workflow of read, discretize, initial, and transient
simulation for the given .inp file.

"""


        """Calculate the probability of failure given a sample of damage states.
        Parameters
        ----------
        ki : float or int or list, optional
            If given as float or int, set the value as wavespeed
            for all pipe; If given as list set the corresponding
            value to each pipe, by default 1200.
        dt : str or list, optional
            The list of pipe to define wavespeed,
            by default all pipe in the network.
        """
fragility_curves_epn = {
    'PW': {
        'Fail': {'mu': 130.139, 'sigma': 0.1213}
    },
    'PS': {
        'Fail': {'mu': 130.504, 'sigma': 0.1352}
    }
}
