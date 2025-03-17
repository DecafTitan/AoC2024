import math

f = open('data.txt', 'r')
content = f.read()
data = content.split('\n')
# close file now that we are done with it
f.close()

f = open('rules.txt', 'r')
rulesContent = f.read()
rules = rulesContent.split('\n')
# close file now that we are done with it
f.close()

rulesDict = {}

for rule in rules:
    print(rule)
    splitter = rule.split('|')
    if splitter[0] in rulesDict:
        rulesDict[splitter[0]][splitter[1]] = ''
    else:
        # New dict in rulesDict will contain values that come after the number according to the rules
        rulesDict[splitter[0]] = {}

midNumData: int = 0

for line in data:
    numbers: list[str] = line.split(',')
    isBad: bool = False
    # Start by going through each number in the line
    for x in range(0, len(numbers)):
        # Then compare each number with every other numbr
        for y in range(x + 1, len(numbers)):
            # If num y is in rulesDict then there is a list of rules for what should come after
            if numbers[y] in rulesDict:
                # print(numbers[y] + ' is in rulesDict ', rulesDict[numbers[y]])
                # If number x is found in y rulesDict then
                # num x is in violation of rule num y so it should not count this line
                if numbers[x] in rulesDict[numbers[y]]:
                    isBad = True
                    break
        if isBad:
            break
    if not isBad:
        midIndex: int = math.floor(len(numbers) / 2)
        midNumData += int(numbers[midIndex])

print(midNumData)
