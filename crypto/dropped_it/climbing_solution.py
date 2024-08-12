
file = open('flag.txt', 'r')
data = file.readlines()
file.close()

char_list = []
index = 0

for line in data:
    num = int(line.strip('\n'))
    num += index
    character = chr(num)
    char_list.append(character)
    index += 1

result = ''.join(char_list)

print(result)

file = open('result.txt', 'w')
file.writelines(result)
file.close()
