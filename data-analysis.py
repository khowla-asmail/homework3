import numpy as np 
import pandas as pd
print(np.__version__)
print(pd.__version__)
array1=np.array([[1,2,3],[4,5,6]])
print(array1)
data=[['25','khowla'],['21','reema'],['24','kinda']]
df=pd.DataFrame(data,columns=['age','name'])

print(df)