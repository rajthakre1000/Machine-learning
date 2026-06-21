# Feacher engineering
# Feacher engineering is the process of using domain knowledge to extract features
# from raw data. These feachers can be used to improve the performance of machine learning algoriths.
# data prepration: Data processing> FEACHER extraction& Engineering > Feacher scaling & Selection

# Feachere Engineering:
#           Feacher Transformation (missing value, handling catagorical feature, Outlier detection, Feacher scaling)
#           Feacher Construction
#           Feacher Selection (giving selected feacher(column) to model)
#           Feacher Extraction (from given feacher, extract new feachers (programmatacally, by algorithm))
#  why is that the graphics
# 1. Missing values:
# ex: replacing missing age by > avg of age
# removing missing value rows (only when the data is too large and missing values are very less)
    # because sklearn library doesnt work when there is missing values

# 2. Handling Catagorical Feature
# 3. Removing outlier: some data points which are way diffrent from data and can cause while training model so they must be removed before training
# 4: Scaling data: eg: the age column lies btw 20-80 and the salary column vary from 10000 to 2000000 so the salary column can dominate over age so its better to scale both column btw 0-1
# some common types of scaling: minmax scaling , StandardScaler, maxabs_scale, minmax_scale
# 5: Feacher construction: ex: in Titanic datset: SibSp(sibling) , Parch(parent) can be represented by one column- family,known example of feacher construction
# 6: Feacher selection: selection of important feacher for ML model
