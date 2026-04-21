import re

def chuan_hoa_chuoi(s):
    # 1. Xóa khoảng trắng đầu/cuối mỗi dòng
    lines = s.split('\n')
    lines = [line.strip() for line in lines]

    # 2. Xử lý từng dòng
    new_lines = []
    for line in lines:
        # 2.1 Xóa nhiều khoảng trắng → 1 khoảng trắng
        line = re.sub(r'\s+', ' ', line)

        # 2.2 Xóa khoảng trắng trước dấu , .
        line = re.sub(r'\s+([,.])', r'\1', line)

        new_lines.append(line)

    # 3. Ghép lại thành chuỗi
    return '\n'.join(new_lines)


# Nhập dữ liệu
s = input("Nhập chuỗi:\n")

# Xuất kết quả
print("\nChuỗi sau khi chuẩn hóa:")
print(chuan_hoa_chuoi(s))