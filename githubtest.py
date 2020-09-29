file = open("sample.txt")

line = file.read().replace("\n", " ")
file.close()

print(line)