import pandas as pd
import numpy as np

# dữ liệu dầu vào
truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)

# sai số bình phương trung bình 
sai_so = ((truth + pred) ** 2).mean()

print("Sai số bình phương trung bình:", sai_so)
