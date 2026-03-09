import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    l=[]
    arr=np.array(x)*-1.0
    arr2=np.exp(arr)+1
    arr=1/arr2
  
    # Write code here
    return arr
    pass