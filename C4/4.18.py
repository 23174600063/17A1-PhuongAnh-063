import pandas as pd

# Dữ liệu đầu vào
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])

# Tạo một danh sách trống để lưu các email hợp lệ
valid_emails = []

# Kiểm tra từng phần tử trong Series
for email in emails:
    if '@' in email and '.' in email:  
        valid_emails.append(email)

# Chuyển thành Series
valid_emails_series = pd.Series(valid_emails)

print(valid_emails_series)