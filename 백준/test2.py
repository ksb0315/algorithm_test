import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(15).reshape(5,3))
print(df.iloc[1:3])