cipher = input("Nhap cipher text: ")

plain = ""
i = 0

while i < len(cipher):
    if cipher[i] == '#':
        so_lan = int(cipher[i + 1])
        ky_tu = cipher[i + 2]
        plain += ky_tu * so_lan
        i += 3
    else:
        plain += cipher[i]
        i += 1

print("Plain text:", plain)
