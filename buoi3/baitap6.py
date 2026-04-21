import re

# Nhập dữ liệu
S = input("Nhập chuỗi S: ")
word = input("Nhập từ cần đếm: ")

# Chuẩn hóa: về chữ thường
S = S.lower()
word = word.lower()

# Tách từ (loại bỏ dấu câu)
words = re.findall(r'\b\w+\b', S)

# Đếm
count = words.count(word)

print(f"Số từ '{word}' là: {count}")