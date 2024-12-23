import pandas as pd
import numpy as np

# Tạo Series
ser = pd.Series(np.random.normal(10, 5, 25))  # 25 giá trị ngẫu nhiên từ phân phối chuẩn

# 1. Giá trị tối thiểu
minimum = ser.min()

# 2. Phân vị thứ 25 (25th percentile)
sorted_ser = ser.sort_values()  # Sắp xếp tăng dần
index_25 = int(0.25 * len(sorted_ser))  # Vị trí của phần tử 25%
percentile_25 = sorted_ser.iloc[index_25]  # Lấy giá trị tại vị trí đó

# 3. Trung vị
median = ser.median()  # Hoặc: sorted_ser.iloc[len(sorted_ser) // 2]

# 4. Phân vị thứ 75 (75th percentile)
index_75 = int(0.75 * len(sorted_ser))  # Vị trí của phần tử 75%
percentile_75 = sorted_ser.iloc[index_75]  # Lấy giá trị tại vị trí đó

# 5. Giá trị tối đa
maximum = ser.max()

# In kết quả
print("Giá trị tối thiểu:", minimum)
print("Phân vị thứ 25:", percentile_25)
print("Trung vị:", median)
print("Phân vị thứ 75:", percentile_75)
print("Giá trị tối đa:", maximum)