from .helping import *
def mean_variance(x,epsilon=0.00001):
    mean=np.mean(x)
    var=np.var(x)
    if abs(mean-var)<=epsilon:
        return 'poisoon'
    elif mean>var:
        return 'binomial'
    else:
        return 'negative binomial'
    
def slope_method(data):
    # Create sample data
    x = pd.DataFrame(data,columns=['num_pols'])
    x['num_acc']=np.arange(len(x))
    res=(x['num_pols']/x['num_pols'].shift(1)*x['num_acc'])
    print(res)
    plt.scatter(res.index,res)