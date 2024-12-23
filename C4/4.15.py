import pandas as pd

# dữ liệu vào
ser = pd.Series(['how','to','kick','ass?'])

# chuyển đổi ký tự đầu tiên của mỗi phần tử
ser_viet_hoa = ser.str.capitalize()

print(ser_viet_hoa)