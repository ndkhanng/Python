# (1) Giam dung luong file van ban
# (2) Doc file da giam va khoi phuc lai noi dung ban dau

# Doc file goc
f = open("fileName.txt", "r", encoding="utf-8")
text = f.read()
f.close()

# Tach thanh cac tu
words = text.split()

# Tao tu dien ma hoa
dictionary = {}
compressed = []

index = 0

for w in words:
    if w not in dictionary:
        dictionary[w] = index
        index += 1

    compressed.append(str(dictionary[w]))

# Luu file da nen
f = open("compressed.txt", "w", encoding="utf-8")

# Luu bang tu dien
for key, value in dictionary.items():
    f.write(str(value) + ":" + key + "\n")

f.write("===\n")

# Luu noi dung da ma hoa
f.write(" ".join(compressed))

f.close()

print("Da tao file compressed.txt")

# ------------------------------------------------

# Doc file da nen va khoi phuc
f = open("compressed.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

reverse_dict = {}
content = []
start = False

for line in lines:

    line = line.strip()

    if line == "===":
        start = True
        continue

    if start == False:
        code, word = line.split(":")
        reverse_dict[code] = word
    else:
        content = line.split()

# Giai nen
result = []

for c in content:
    result.append(reverse_dict[c])

# Ghi file khoi phuc
f = open("restore.txt", "w", encoding="utf-8")
f.write(" ".join(result))
f.close()

print("Da khoi phuc file restore.txt")