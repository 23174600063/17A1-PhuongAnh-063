import pandas as pd
import numpy as np

ser = pd.Series(np.random.randint(1,10,7))

# tìm vị tri là bội của 3
boi = ser [ser % 3 == 0].index

print("series ban đầu:",ser)
print("\n Vị trí của các số bội 3 :", boi)