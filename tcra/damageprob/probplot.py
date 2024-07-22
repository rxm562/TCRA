# plotting lognormal distribution of pf
def plot_lognormal_distribution(result_bldg):
    """ 
    this function plots probability distribution functions for fitted lognormal probability of failure data.
    
    Parameters
    ----------
    pf : 
        probability of failure estimated - Monte Carlo simulation
    df : 
        building inventory dataframe with damage state
    dmg :
        damage state

    Returns
    -------
    pdf : 
        probability density function
    cdf : 
        cumulative distribution function
    """
    
    # Prepare data
    df = pd.DataFrame(result_bldg.pf)
    epsilon = 1e-10
    values = df['pf'] + epsilon

    # Fit lognormal distribution
    shape, loc, scale = lognorm.fit(values, floc=0)

    # Create range for plotting
    x = np.linspace(min(values), max(values), 100)

    # Calculate PDF and CDF
    pdf = lognorm.pdf(x, shape, loc=loc, scale=scale)
    cdf = lognorm.cdf(x, shape, loc=loc, scale=scale)

    # Plot
    fig, (ax1, ax2) = plt.subplots(2, 1, layout='constrained')
    ax1.plot(x, pdf, label='Fitted Lognormal Pf', color='blue')
    ax1.set_xlabel('Value')
    ax1.set_ylabel('Frequency')
    ax1.legend()

    ax2.plot(x, cdf, label='Fitted Lognormal Pf', color='blue')
    ax2.set_xlabel('Value')
    ax2.set_ylabel('% Cumulative')
    ax2.legend()

    plt.show()
