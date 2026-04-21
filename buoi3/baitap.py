from datetime import datetime, timedelta

# i. Thông tin hiện tại
now = datetime.now()

print("Năm hiện tại:", now.year)
print("Tháng hiện tại bằng chữ:", now.strftime("%B"))
print("Tuần thứ mấy trong năm:", now.strftime("%U"))
print("Tuần thứ mấy trong tháng:", (now.day - 1) // 7 + 1)
print("Ngày thứ mấy trong năm:", now.strftime("%j"))
print("Ngày trong tháng:", now.day)
print("Thứ:", now.strftime("%A"))
print("Giờ phút giây:", now.strftime("%H:%M:%S"))

print("\n---")

# ii. Tính số ngày giữa 2 ngày
d1 = input("Nhập ngày 1 (dd/mm/yyyy): ")
d2 = input("Nhập ngày 2 (dd/mm/yyyy): ")

date1 = datetime.strptime(d1, "%d/%m/%Y")
date2 = datetime.strptime(d2, "%d/%m/%Y")

diff = abs((date2 - date1).days)
print("Số ngày cách nhau:", diff)

print("\n---")

# iii. Chuyển chuỗi sang datetime
s = input("Nhập chuỗi ngày (vd: Sep 18 2019 2:43PM): ")

date_obj = datetime.strptime(s, "%b %d %Y %I:%M%p")
print("Datetime:", date_obj)

print("\n---")

# iv. Cộng thêm 5 giây
new_time = now + timedelta(seconds=5)
print("Sau khi cộng 5 giây:", new_time.strftime("%H:%M:%S"))