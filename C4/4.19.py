import pandas as pd
import numpy as np

# Dữ liệu đầu vào
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))

# Tạo DataFrame để dễ dàng xử lý
df = pd.DataFrame({'fruit': fruit, 'weight': weights})

# Tính khối lượng trung bình theo từng loại quả
khoi_luong_trung_binh = df.groupby('fruit')['weight'].mean()

# In kết quả
print(khoi_luong_trung_binh)