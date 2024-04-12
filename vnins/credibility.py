from scipy.stats import norm

def z_score(probability):
    z_score = norm.ppf(probability)
    return z_score

def number_exposures(p,k,sigma,mu):
    z=z_score((1+p)/2)
    ne=(z/k)**2*(sigma**2/mu**2)
    return ne