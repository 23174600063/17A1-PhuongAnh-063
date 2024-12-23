import pandas as pd
import numpy as np

# Tạo Series ngẫu nhiên với 20 phần tử
ser = pd.Series(np.random.random(20))

# Sắp xếp chỉ số để xác định vị trí từng phần tử sau khi sắp xếp
sorted_ser = ser.sort_values().reset_index(drop=True)

# Tính số phần tử mỗi nhóm (mỗi decile)
n = len(ser) // 10

# Tạo danh sách tên phân vị
labels = [f"Decile {i+1}" for i in range(10)]

# Gán nhãn cho từng phần tử
decile_labels = []
for i in range(len(ser)):
    decile_labels.append(labels[i // n])  # Chia nhóm dựa trên chỉ số

# Tạo Series mới với nhãn phân vị
deciles = pd.Series(decile_labels, index=sorted_ser.index)

# Kết quả
print("Dữ liệu ban đầu:")
print(ser)

print("\nPhân vị tương ứng:")
print(deciles.sort_index())  # Sắp xếp lại để khớp với dữ liệu ban đầu