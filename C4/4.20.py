import pandas as pd

# Đọc dữ liệu từ file CSV
eurol2 = pd.read_csv('D:/17a1dhkl/lập trình nâng cao/chuong 4/btap c4/euro2012.csv')

# In thông tin cơ bản của DataFrame
print("Thông tin về Euro 12:")
print("Type:", type(eurol2))
print("Shape:", eurol2.shape)
print("Danh sách các cột:", eurol2.columns.tolist())

# In giá trị cột Goals
print("Giá trị cột Goals:")
print(eurol2['Goals'])

# Số lượng đội tham gia Euro 2012
num_teams = len(eurol2)
print("\nSố đội tham gia Euro 2012:", num_teams)

# In toàn bộ thông tin của Euro 2012
print("\nThông tin Euro 2012:",eurol2)

# Tạo DataFrame mới chỉ với các cột 'Team', 'Yellow Cards', 'Red Cards'
discipline = eurol2[['Team', 'Yellow Cards', 'Red Cards']]
print("\nDataFrame discipline:",discipline)


# Sắp xếp discipline giảm dần theo 2 cột 'Red Cards' và 'Yellow Cards'
discipline_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=[False, False])
print("\nDataFrame discipline đã sắp xếp:",discipline_sorted)


# Tính trung bình số 'Yellow Cards'
average_yellow_cards = discipline['Yellow Cards'].mean()
print("\nTrung bình Yellow Cards:", average_yellow_cards)

# Lọc các đội ghi hơn 6 bàn thắng
teams_more_than_6_goals = eurol2[eurol2['Goals'] > 6]
print("\nCác đội ghi hơn 6 bàn thắng:",teams_more_than_6_goals)

# Lọc các đội có tên bắt đầu bằng 'G'
teams_start_with_G = eurol2[eurol2['Team'].str.startswith('G')]
print("\nCác đội tên bắt đầu bằng 'G':",teams_start_with_G)

# In 7 cột đầu tiên của DataFrame
print("\n7 cột đầu tiên:")
print(eurol2.iloc[:, :7])

# In tất cả các cột, trừ 3 cột cuối
print("\nTất cả các cột, trừ 3 cột cuối:")
print(eurol2.iloc[:, :-3])

# In các cột 'Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards'
print("\nCác cột Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards:")
print(eurol2[['Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards']])

# In các cột 'Team', 'Shooting Accuracy' của các đội: 'England', 'Italy', 'Russia'
teams_selected = eurol2[eurol2['Team'].isin(['England', 'Italy', 'Russia'])][['Team', 'Shooting Accuracy']]
print("\nThông tin Shooting Accuracy của các đội England, Italy, Russia:",teams_selected)
