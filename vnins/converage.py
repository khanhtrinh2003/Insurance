from .helping import *

def insurer_policy_limit(X,u):
    """
    X ^ u
    """
    return np.where(X<u,X,u)

def ilf(X,u,b):
    """
    Increased Limit Factor
    """
    return np.mean(insurer_policy_limit(X,u))/np.mean(insurer_policy_limit(X,b))

def policyholder_ordinary_deductibles(X,d):
    """
    X ^ d
    """
    return np.where(X<d,X,d)

def insurer_ordinary_deductibles(X,d):
    """
    (X - d)+
    """
    return np.where(X<=d,0,X-d)

def ler(X,d):
    """
    Loss Elimination Ratio
    - The loss elimination ratio (LER) measures how much the insurer saves by imposing an ordinary deductible.
    """
    return np.mean(policyholder_ordinary_deductibles(X,d))/np.mean(X)

def payment_per_loss(X,d):
    yL=insurer_ordinary_deductibles(X,d)
    return yL

def payment_per_payment(X,d):
    yL=insurer_ordinary_deductibles(X,d)
    yP=yL[yL>0]
    return yP
def expected_payment_per_loss(X,d):
    return np.mean(payment_per_loss(X,d))

def expected_payment_per_payment(X,d):
    return np.mean(payment_per_payment(X,d))

def insurer_franchise_deductibles(X,d):
    return np.where(X<=d,0,X)
    
def insurer_coinsurance(X,alpha):
    return X*alpha


def insurer_payment(X,deductible=None,coinsurance=None,coinsurance_first=False):
    if deductible==None:
        if coinsurance==None:
            return X
        else:
            return insurer_coinsurance(X,coinsurance)
    else:
        if coinsurance_first:
            return insurer_ordinary_deductibles(insurer_coinsurance(X,coinsurance),
                                    deductible)    
        else:
            return insurer_coinsurance(insurer_ordinary_deductibles(X,deductible),
                                    coinsurance)    
        
def maximum_covered_loss(policy_limit,coinsurance,deductible):
    """
    The maximum covered loss is the loss amount above which the insurer pays the policy limit
    """
    return policy_limit/coinsurance+deductible