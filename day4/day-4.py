f = open('data.txt', 'r')
content = f.read()
lines = content.split('\n')
# close file now that we are done with it
f.close()

searchStr = 'XMAS'
print(lines)


def forwardCheck(line, index):
    # Check if there is enough of the remaining line to contain the entire `searchStr`
    if (index + len(searchStr)) < len(line):
        # If so, loop through each letter
        for z in range(0, len(searchStr)):
            if not line[index + z] is searchStr[index]:
                return False
        return True
    return False

def BackwardCheck(line, index):
    # Check if there is enough of the line before to contain `searchStr` backwards
    if(index - len(searchStr) > -1):
        #If so, loop through previous letters in line
        for z in range(index, index - len(searchStr), -1):
            if line[z] is searchStr[0]:
                return False
            return True
        return False

# Loop through each line
for x in range(0, len(lines)):
    line = lines[x]
    # Loop through each letter in each line
    for y in range(0, len(line)):
        letter = line[y]
        # Start checks if current letter is start of `searchStr` (i.e. 'X')
        if letter is searchStr[0]:
            forwardCheck(line, y)

