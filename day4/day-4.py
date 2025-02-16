f = open('data.txt', 'r')
content = f.read()
lines = content.split('\n')
# close file now that we are done with it
f.close()

searchStr = 'XMAS'
print(lines)


# def forwardCheck(line, index):
#     if (index + len(searchStr)) < len(line):
        # for z in range(0, len(searchStr)):

for x in range(0, len(lines)):
    line = lines[x]
    for y in range(0, len(line)):
        letter = line[y]
        if letter is searchStr[0]:
            print(letter)

