'''
Created on 17 Feb 2021

@author: thomasgumbricht
'''

# Standard library imports

# Third party imports

import numba

import numpy as np

#from math import sqrt
 
# Package application imports

@numba.jit(nopython=True)
def InterpolateLinearNaNNumba(arr):
    
    #lastitem = arr.shape[0]
    
    for i in range(1,arr.shape[0]):  
    
        if np.isnan(arr[i]):   
      
            postIndexArray = arr[i+1:]
            
            postIndex = np.where(~np.isnan(postIndexArray))
            
            arr[i] = (arr[i-1]+(postIndexArray[postIndex[0][0]]/(postIndex[0][0]+1.0) )) / ( 1.0+ (1.0/(postIndex[0][0]+1.0) ) )
    
    return arr
