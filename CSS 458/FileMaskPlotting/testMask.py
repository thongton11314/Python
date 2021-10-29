import numpy as np
import numpy.ma as ma
arr = np.array([1, 2, 3, np.nan, 5, 6, np.inf, 8])
ma_arr = ma.masked_invalid(arr)
print(ma_arr)
