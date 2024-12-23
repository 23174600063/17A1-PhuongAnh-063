import pandas as pd

ser = pd.Series([1,3,6,10,15,21,27,35])

# số hiệu giữa các số liên tiếp 
hieu_so = ser.diff()

# hiệu số của số hiệu
hieu_so_cua_so_hieu = hieu_so.diff()

print("Hiệu số cảu số hiệu giữa các số liên tiếp là:",hieu_so_cua_so_hieu)