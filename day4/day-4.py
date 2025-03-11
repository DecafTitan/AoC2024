f = open('data.txt', 'r')
content = f.read()
lines = content.split('\n')
# close file now that we are done with it
f.close()

# String to search for wordsearch
searchStr = 'XMAS'

# All lines are the same length so storing line length globally
lineLength = len(lines[0])
totalNumLines = len(lines)
print('total lines: ' + str(totalNumLines) + ' line length: ' + str(lineLength))
matches = 0

def forwardsIndexCheck(index: int) -> bool:
    # Need to do searchStr - 1 to correct for len giving 1 based index and `index` being 0 based
    return (index + (len(searchStr) - 1)) < lineLength

def backwardsIndexCheck(index: int) -> bool:
    # Need to do searchStr - 1 to correct for len giving 1 based index and `index` being 0 based
    return index - (len(searchStr) - 1) > -1

def upCheck(lineIndex: int) -> bool:
    return backwardsIndexCheck(lineIndex)

def downCheck(index: int) -> bool:
    # Need to do searchStr - 1 to correct for len giving 1 based index and `index` being 0 based
    return (index + (len(searchStr) - 1)) < totalNumLines

def forwardCheck(line: str, index: int) -> bool:
    # Check if there is enough of the remaining line to contain the entire `searchStr`
    if forwardsIndexCheck(index):
        # If so, loop through each letter
        for z in range(0, len(searchStr)):
            if line[index + z] != searchStr[z]:
                return False
        return True
    return False

def backwardCheck(line: str, index: int) -> bool:
    # Check if there is enough of the line before to contain `searchStr` backwards
    if backwardsIndexCheck(index):
        #If so, loop through previous letters in line
        for z in range(0, len(searchStr)):
            if line[index - z] != searchStr[z]:
                return False
        return True
    return False

def upwardCheck(lineIndex: int, index: int) -> bool:
    if upCheck(lineIndex):
        for z in range(0, len(searchStr)):
            if lines[lineIndex - z][index] != searchStr[z]:
                return False
        return True
    return False

def downwardCheck(lineIndex: int, index: int) -> bool:
    if downCheck(lineIndex):
        for z in range(0, len(searchStr)):
            if lines[lineIndex + z][index] != searchStr[z]:
                return False
        return True
    return False

def upLeftCheck(lineIndex: int, index: int) -> int:
    if upCheck(lineIndex) and backwardsIndexCheck(index):
        for z in range(0, len(searchStr)):
            if lines[lineIndex - z][index - z] != searchStr[z]:
                return False
        return True
    return False

def upRightCheck(lineIndex: int, index: int) -> int:
    if upCheck(lineIndex) and forwardsIndexCheck(index):
        for z in range(0, len(searchStr)):
            if lines[lineIndex - z][index + z] != searchStr[z]:
                return False
        return True
    return False

def downLeftCheck(lineIndex: int, index: int) -> bool:
    if downCheck(lineIndex) and backwardsIndexCheck(index):
        for z in range(0, len(searchStr)):
            if lines[lineIndex + z][index - z] != searchStr[z]:
                return False
        return True
    return False

def downRightCheck(lineIndex: int, index: int) -> bool:
    if downCheck(lineIndex) and forwardsIndexCheck(index):
        for z in range(0, len(searchStr)):
            if lines[lineIndex + z][index + z] != searchStr[z]:
                return False
        return True
    return False

# Loop through each line
for x in range(0, len(lines)):
    line = lines[x]
    forwardMatches = 0
    backwardMatches = 0
    upwardMatches = 0
    downwardMatches = 0
    upLeftMatches = 0
    upRightMatches = 0
    downLeftMatches = 0
    downRightMatches = 0
    # Loop through each letter in each line
    for y in range(0, len(line)):
        letter = line[y]
        
        # Start checks if current letter is start of `searchStr` (i.e. 'X')
        if letter == searchStr[0]:
            forwardMatches += forwardCheck(line, y)
            backwardMatches += backwardCheck(line, y)
            upwardMatches += upwardCheck(x, y)
            downwardMatches += downwardCheck(x, y)
            
            upLeftMatches += upLeftCheck(x, y)
            upRightMatches += upRightCheck(x, y)
            downLeftMatches += downLeftCheck(x, y)
            downRightMatches += downRightCheck(x, y)
    matches = matches + forwardMatches + backwardMatches + upwardMatches + downwardMatches + upLeftMatches + upRightMatches + downLeftMatches + downRightMatches
    print('Matches after line ' + str(x) + ' - forwardMatches:' + str(forwardMatches) + ' backwardMatches: ' + str(backwardMatches) + ' upMatches: ' + str(upwardMatches) + ' downwardMatches: ' + str(downwardMatches) + ' upLeftMatches: ' + str(upLeftMatches) + ' upRightMatches: ' + str(upRightMatches) + ' downLeftMatches: ' + str(downLeftMatches) + ' downRightMatches: ' + str(downRightMatches))
print('Total matches: ' + str(matches))

