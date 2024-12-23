import pandas as pd
import numpy as np

ser  = pd.Series(np.random.randint(1,10,35))

# pd.Series : chuyển dan sách thành một series
# np.random.randint(1,10,35) : sinh ra 35 số nguyên trong khoảng từ 1 dến 9, giới hạn la 10 nên không bao gồm số 10.

# Định hình lại Series thành DataFrame 7 hàng, 5 cột
df = pd.DataFrame(ser.values.reshape(7, 5))

# Kết quả
print("Series ban đầu:",ser)
print("\nDataFrame sau khi định hình lại:",df)
