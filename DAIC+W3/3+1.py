import numpy as np
import pandas as pd
from pandas import Series, DataFrame

d = np.random.randint(10, 99, size=(50, 7))
df = DataFrame(d, columns=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
df.to_csv('3+1.csv', mode='w', header=True, index=False)