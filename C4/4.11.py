import pandas as pd

ser = pd.Series(list('abedefghijklmnoqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

# Trích xuất các phần tử tại các vị trí trong pos
result = ser[pos]

print("Series ban đầu:",ser)
print("\nCác mục tại các vị trí trong danh sách pos:",result)
