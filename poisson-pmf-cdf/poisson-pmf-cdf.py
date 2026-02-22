import numpy as np
from math import factorial

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here

    def poisson_pmf(i):
        """
        Compute Poisson PMF
        """
        logfactorial = np.sum(np.log(np.arange(1, i+1)))
        factorial = np.exp(logfactorial)
        
        return np.exp(-lam)*(lam**i)/factorial
                              
    pmf = poisson_pmf(k)
    cdf = np.sum([poisson_pmf(i) for i in range(k+1)])
    return (pmf, cdf)