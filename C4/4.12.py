import pandas as pd

ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

df = pd.DataFrame({'1':ser1,'2':ser2})
df1 = pd.Series(list(ser1) +  list(ser2))
print('\nXếp chồng theo chiều ngang:',df)
print('\nXếp chồng theo chiều dọc:',df1)

