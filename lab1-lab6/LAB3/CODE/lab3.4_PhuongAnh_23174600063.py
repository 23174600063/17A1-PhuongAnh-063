import pandas as pd
# Đọc dữ liệu từ hai file CSV vào DataFram
stocks1 = pd.read_csv('D:/17a1dhkl/DHKL17A1HN/LAB3/DATA/stocks1.csv')
stocks2 = pd.read_csv('D:/17a1dhkl/DHKL17A1HN/LAB3/DATA/stocks2.csv')

# 2. Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks = pd.concat([stocks1, stocks2])

# Đọc file CSV vào DataFrame companies
companies = pd.read_csv('D:/17a1dhkl/DHKL17A1HN/LAB3/DATA/companies.csv')

# Hiển thị 5 dòng đầu tiên của DataFrame companies
print("5 dòng đầu tiên của companies:")
print(companies.head())

# Kết hợp stocks (đã tạo từ bài 3) và companies dựa trên cột chung là symbol
# Giả sử stocks đã được tạo từ trước và có cột 'symbol'
merged_data = pd.merge(stocks, companies, left_on='symbol', right_on='name')

# Tính giá đóng cửa (close) trung bình cho mỗi công ty
avg_close_per_company = merged_data.groupby('name')['close'].mean()

# Hiển thị kết quả cho 5 công ty đầu tiên
print("\nGiá đóng cửa trung bình cho mỗi công ty (5 công ty đầu tiên):")
print(avg_close_per_company.head())