# Feacher scaling: Normalization
# Normalization is a technique often applied as part of data prepration for ML.
# The goal of normalization is to change the values of numaric columns in the dataset to use a common scale,
# without distorting differences in the ranges of values or losing  information.
# minmaxscale
# mean normalization
# max absolute scaling
# robust scaling 

# 1. minmaxscaling
# Xi' = (Xi - min(X)) / max(X)-min(X)          uses max, min value of the column to find minmaxscaling
# scaling btw [0,1] 

# 2. mean normalization
# Xi' = (Xi - mean(X)) / max(X) - min(X) 
# uses when need centered data > often ppl uses standerdscaler rather than mean normalization

# 3. max absolute value
# Xi' = Xi / |max(X)|       
# uses when there is Sparse data (more number of zeros)

# robust scaling
# Xi' = (Xi - median(X)) / IQR                      IOR = 75%tile - 25%tile
# good on data with outliers

# generallt standerdsacler works fine (but depends upon which algorithm we using)
# for image processing (CNN) > minmaxscale
from sklearn.preprocessing import MaxAbsScaler

