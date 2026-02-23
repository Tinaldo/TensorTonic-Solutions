import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """

    def binomial_pmf(n,p,i):
        """Compute binomial PMF"""
        return comb(n,i)*(p**i)*(1-p)**(n-i)

    pmf = binomial_pmf(n, p, k)
    cdf = np.sum([binomial_pmf(n,p,i) for i in range(k+1)])
    return (pmf, cdf)