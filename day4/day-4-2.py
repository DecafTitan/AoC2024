f = open('data.txt', 'r')
content = f.read()
lines = content.split('\n')
# close file now that we are done with it
f.close()

# String to search for wordsearch
searchStr = 'MAS'

# All lines are the same length so storing line length globally
lineLength = len(lines[0])
totalNumLines = len(lines)
print('total lines: ' + str(totalNumLines) + ' line length: ' + str(lineLength))
matches = 0

def upLeftCheck(lineIndex: int, index: int) -> bool:
    if lines[lineIndex - 1][index - 1] == 'M' and lines[lineIndex + 1][index + 1] == 'S':
        return True
    if lines[lineIndex - 1][index - 1] == 'S' and lines[lineIndex + 1][index + 1] == 'M':
        return True
    return False

def upRightCheck(lineIndex: int, index: int) -> bool:
    if lines[lineIndex - 1][index + 1] == 'M' and lines[lineIndex + 1][index - 1] == 'S':
        return True
    if lines[lineIndex - 1][index + 1] == 'S' and lines[lineIndex + 1][index - 1] == 'M':
        return True
    return False

# Loop through each line starting at the second line since the first 2 cannot have an X-MAS
for x in range(1, len(lines) - 1):
    line = lines[x]
    # Loop through each letter in each line
    # but skip the first and last since it won't match the X-MAS shape
    for y in range(1, len(line) - 1):
        letter = line[y]
        # Start checks if current letter is the middle letter of the search string (i.e. 'A')
        if letter == searchStr[1]:
            if upLeftCheck(x, y) and upRightCheck(x, y):
                matches += 1
                        
print('Total matches: ' + str(matches))

