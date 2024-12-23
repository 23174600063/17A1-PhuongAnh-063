import pandas as pd

# Input
ser1 = pd.Series([1, 2, 3, 4, 2])  # Series 1
ser2 = pd.Series([4, 5, 6, 7, 8])  # Series 2

# Yêu cầu 1: Từ ser1, xóa các mục có mặt trong ser2
ser1_removed = ser1[~ser1.isin(ser2)]  # Dùng isin() để kiểm tra phần tử trùng

# Yêu cầu 2: Tìm tất cả các mục của ser1 và ser2 nhưng không nằm chung trong cả hai
ser_union = pd.concat([ser1, ser2])  # Kết hợp cả hai series
ser_unique = ser_union[~ser_union.duplicated(keep=False)]  # Giữ các phần tử không trùng lặp

# In kết quả
print("Ser1 ban đầu:\n", ser1)
print("\nSer2 ban đầu:\n", ser2)
print("\nKết quả 1: Ser1 sau khi xóa các mục có mặt trong Ser2:\n", ser1_removed)
print("\nKết quả 2: Các mục của Ser1 và Ser2 nhưng không nằm chung:\n", ser_unique)