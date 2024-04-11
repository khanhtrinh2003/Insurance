import numpy as np

def random_uniform(low=0, high=1, size=None):
    """
    Generate random numbers from a uniform distribution.

    Parameters:
    - low: Lower bound of the distribution (default: 0).
    - high: Upper bound of the distribution (default: 1).
    - size: Output shape (default is None, which returns a single value).

    Returns:
    - Random numbers from the uniform distribution.
    """
    return np.random.uniform(low, high, size)

def random_normal(mean=0, std=1, size=None):
    """
    Generate random numbers from a normal (Gaussian) distribution.

    Parameters:
    - mean: Mean of the distribution (default: 0).
    - std: Standard deviation of the distribution (default: 1).
    - size: Output shape (default is None, which returns a single value).

    Returns:
    - Random numbers from the normal distribution.
    """
    return np.random.normal(mean, std, size)

def random_lognormal(mean=0, sigma=1, size=None):
    """
    Generate random numbers from a lognormal distribution.

    Parameters:
    - mean: Mean of the underlying normal distribution (default: 0).
    - sigma: Standard deviation of the underlying normal distribution (default: 1).
    - size: Output shape (default is None, which returns a single value).

    Returns:
    - Random numbers from the lognormal distribution.
    """
    return np.random.lognormal(mean, sigma, size)

def random_exponential(scale=1, size=None):
    """
    Generate random numbers from an exponential distribution.

    Parameters:
    - scale: Inverse of the rate parameter (default: 1).
    - size: Output shape (default is None, which returns a single value).

    Returns:
    - Random numbers from the exponential distribution.
    """
    return np.random.exponential(scale, size)

def random_gamma(shape, scale=1, size=None):
    """
    Generate random numbers from a gamma distribution.

    Parameters:
    - shape: Shape parameter of the distribution.
    - scale: Scale parameter of the distribution (default: 1).
    - size: Output shape (default is None, which returns a single value).

    Returns:
    - Random numbers from the gamma distribution.
    """
    return np.random.gamma(shape, scale, size)

def random_erlang(shape, scale=1, size=None):
    """
    Generate random numbers from an Erlang distribution.

    Parameters:
    - shape: Shape parameter of the distribution.
    - scale: Scale parameter of the distribution (default: 1).
    - size: Output shape (default is None, which returns a single value).

    Returns:
    - Random numbers from the Erlang distribution.
    """
    return np.random.gamma(shape, scale, size)

def random_pareto(alpha, theta, size=None):
    """
    Generate random numbers from a Pareto distribution.

    Parameters:
    - alpha: Shape parameter of the distribution (alpha > 0).
    - theta: Scale parameter of the distribution (theta > 0).
    - size: Output shape (default is None, which returns a single value).

    Returns:
    - Random numbers from the Pareto distribution.
    """
    return np.random.pareto(alpha, size) * theta

def random_sp_pareto(alpha, theta, size=None):
    """
    Generate random numbers from a shifted Pareto distribution.

    Parameters:
    - alpha: Shape parameter of the distribution (alpha > 0).
    - theta: Location parameter of the distribution (theta > 0).
    - size: Output shape (default is None, which returns a single value).

    Returns:
    - Random numbers from the shifted Pareto distribution.
    """
    # Generate random numbers uniformly between 0 and 1
    u = np.random.uniform(0, 1, size)

    # Inverse transform sampling for shifted Pareto distribution
    x = theta / np.power(u, 1.0 / alpha)

    return x

import numpy as np

def random_binomial(n, p, size=None):
    """
    Generate random numbers from a binomial distribution.

    Parameters:
    - n: Number of trials.
    - p: Probability of success in each trial (0 <= p <= 1).
    - size: Output shape (default is None, which returns a single value).

    Returns:
    - Random numbers from the binomial distribution.
    """
    return np.random.binomial(n, p, size)

def random_geometric(p, size=None):
    """
    Generate random numbers from a geometric distribution.

    Parameters:
    - p: Probability of success in each trial (0 <= p <= 1).
    - size: Output shape (default is None, which returns a single value).

    Returns:
    - Random numbers from the geometric distribution.
    """
    return np.random.geometric(p, size)

def random_negative_binomial(r, p, size=None):
    """
    Generate random numbers from a negative binomial distribution.

    Parameters:
    - r: Number of successes required.
    - p: Probability of success in each trial (0 <= p <= 1).
    - size: Output shape (default is None, which returns a single value).

    Returns:
    - Random numbers from the negative binomial distribution.
    """
    return np.random.negative_binomial(r, p, size)

def random_poisson(lam, size=None):
    """
    Generate random numbers from a Poisson distribution.

    Parameters:
    - lam: Expected number of occurrences in a fixed interval (lam >= 0).
    - size: Output shape (default is None, which returns a single value).

    Returns:
    - Random numbers from the Poisson distribution.
    """
    return np.random.poisson(lam, size)

def random_from_pdf(pdf, xmin, xmax, size=None):
    """
    Generate random numbers from a probability distribution given its PDF.

    Parameters:
    - pdf: Probability density function (callable).
    - xmin: Minimum value of the distribution domain.
    - xmax: Maximum value of the distribution domain.
    - size: Output shape (default is None, which returns a single value).

    Returns:
    - Random numbers from the specified distribution.
    """
    # Generate random numbers uniformly between 0 and 1
    u = np.random.uniform(0, 1, size)

    # Inverse transform sampling
    x = xmin * ((xmax/xmin) ** u)

    # Rejection sampling to handle PDFs with undefined values
    valid = pdf(x) > 0
    while not np.all(valid):
        invalid_indices = np.where(~valid)[0]
        u[invalid_indices] = np.random.uniform(0, 1, size=len(invalid_indices))
        x[invalid_indices] = xmin * ((xmax/xmin) ** u[invalid_indices])
        valid = pdf(x) > 0

    return x

