import numpy as np

def mean_variance(x,epsilon=0.00001):
    mean=np.mean(x)
    var=np.var(x)
    if abs(mean-var)<=epsilon:
        return 'poisoon'
    elif mean>var:
        return 'binomial'
    else:
        return 'negative binomial'