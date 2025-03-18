import math

f = open("../data.txt", "r")
content = f.read()
data: list[str] = content.split("\n")
# close file now that we are done with it
f.close()

f = open("../rules.txt", "r")
rulesContent = f.read()
rules: list[str] = rulesContent.split("\n")
# close file now that we are done with it
f.close()

rulesDict = {}

for rule in rules:
    splitter: list[str] = rule.split("|")
    if splitter[0] in rulesDict:
        rulesDict[splitter[0]][splitter[1]] = ""
    else:
        # New dict in rulesDict will contain values that come after the number according to the rules
        rulesDict[splitter[0]] = {}
        rulesDict[splitter[0]][splitter[1]] = ''

f = open("bad-data.txt", "w")

dataStr: str = ""
bad_line_total: int = 0

for index in range(0, len(data)):
    numbers: list[str] = data[index].split(",")
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
        dataStr += data[index] + "\n"
        bad_line_total += 1

f.write(dataStr[0: len(dataStr) - 1])
f.close()
print("Finished writing to bad-data.txt with total bad lines being", bad_line_total)
