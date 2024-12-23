import pandas as pd

ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])

# Tìm vị trí các mục của ser2 trong ser1
vi_tri = [ser1[ser1 == value].index.tolist() for value in ser2]
print(vi_tri)