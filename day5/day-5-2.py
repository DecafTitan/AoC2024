import math

f = open("bad-data.txt", "r")
content = f.read()
data: list[str] = content.split("\n")
# close file now that we are done with it
f.close()

f = open("rules.txt", "r")
rulesContent = f.read()
rules: list[str] = rulesContent.split("\n")
# close file now that we are done with it
f.close()

# The notation X|Y means that if
# both page number X and page number Y are to be produced
# as part of an update,
# page number X must be printed at some point before page number Y.

rulesDict = {}

for rule in rules:
    if '|' in rule:
        splitter: list[str] = rule.split("|")

        if not splitter[0] in rulesDict:
            rulesDict[splitter[0]] = {"before": {}, "after": {}}
        else:
            rulesDict[splitter[0]]['after'][splitter[1]] = ''
            # rulesDict[splitter[0]]["after"][splitter[1]] = ""

        # if not splitter[1] in rulesDict:
        #     rulesDict[splitter[1]] = {"before": {}, "after": {}}
        #     rulesDict[splitter[1]]["before"][splitter[0]] = ""

        # if splitter[0] in rulesDict:
        #     rulesDict[splitter[0]]["after"][splitter[1]] = ""

        # if splitter[1] in rulesDict:
        #     rulesDict[splitter[1]]["before"][splitter[0]] = ""

midNumData: int = 0


def makeCorrectLine(line: list[str], ruleBreakers: list[str]) -> list[str]:
    toEdit: list[str] = line[:]
    # print('Remainder of line:', toEdit)
    # print('Rule breakers:', ruleBreakers)
    for ruleBreaker in ruleBreakers:
        for x in range(len(toEdit) - 1, 0, -1):
            if ruleBreaker in rulesDict:
                # print('Checking for ' +
                #       toEdit[x] + ' in before dict for ' + ruleBreaker, rulesDict[ruleBreaker]['before'])
                if toEdit[x] in rulesDict[ruleBreaker]['after']:
                    # print("About to write:", ruleBreaker)
                    toEdit[x: x] = [ruleBreaker]
                    break
    return toEdit


f = open('corrected-data.txt', 'w')
bad_line_total: int = 0

for index in range(0, len(data)):
    line = data[index]
    numbers: list[str] = line.split(",")
    filteredNumbers: list[str] = numbers[:]
    isBad: bool = False
    ruleBreakers: list[str] = []
    # Start by going through each number in the line
    for x in range(0, len(numbers)):
        # Then compare each number with every other numbr
        for y in range(len(numbers) - 1, x + 1, -1):
            # If num y is in rulesDict then there is a list of rules for what should come after
            if numbers[y] in rulesDict:
                # If number x is found in y rulesDict then
                # num x is in violation of rule num y so it should not count this line
                if numbers[x] in rulesDict[numbers[y]]["after"]:
                    isBad = True
                    # print("Rule breaker: " +
                    #       numbers[x] + ' (' + str(x) + ')' " is supposed to be after " + numbers[y] + ' (' + str(y) + ')')
                    ruleBreakers.append(numbers[x])
                    filteredNumbers.remove(numbers[x])
                    break
    if not isBad:
        print('Good row:', ','.join(numbers))
        midIndex: int = math.floor(len(numbers) / 2)
        midNumData += int(numbers[midIndex])
    else:
        bad_line_total += 1
        # print("Bad row:", numbers)
        correctLine = makeCorrectLine(filteredNumbers, ruleBreakers)
        # print('Correct line:', correctLine)
        if (len(correctLine)) > 0:
            midNumData += int(correctLine[math.floor(len(correctLine) / 2)])
            f.write(','.join(correctLine))
            f.write('\n')
        else:
            print('Line that became empty is', numbers)

f.close()
print('number of bad lines:', bad_line_total)
print('midNumData:', midNumData)
