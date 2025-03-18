import math
import json

f = open("filtered-data.txt", "r")
content = f.read()
data: list[str] = content.split("\n")
# close file now that we are done with it
f.close()

f = open("filtered-rules.txt", "r")
rulesContent = f.read()
rules: list[str] = rulesContent.split("\n")
# close file now that we are done with it
f.close()

# The notation X|Y means that if
# both page number X and page number Y are to be produced
# as part of an update,
# page number X must be printed at some point before page number Y.

rulesDict: dict[str:dict[str:str]] = {}

for rule in rules:
    if '|' in rule:
        splitter: list[str] = rule.split("|")
        if splitter[0] in rulesDict:
            rulesDict[splitter[0]]['after'][splitter[1]] = ''
        else:
            rulesDict[splitter[0]] = {"after": {}, "before": {}}
            rulesDict[splitter[0]]['after'][splitter[1]] = ''

        if splitter[1] in rulesDict:
            rulesDict[splitter[1]]['before'][splitter[0]] = ''
        else:
            rulesDict[splitter[1]] = {"after": {}, "before": {}}
            rulesDict[splitter[1]]['before'][splitter[0]] = ''

f = open('after-dict.json', 'w')

json.dump(rulesDict, f, sort_keys=True, indent=4)

midNumData: int = 0


def makeCorrectLine(remainder: list[str], ruleBreakers: list[str]) -> list[str]:
    toEdit: list[str] = remainder
    rule_breakers_editable: list[str] = ruleBreakers
    print('Remainder of line:', toEdit)
    print('Rule breakers:', ruleBreakers)
    # Need to somehow identify where the first rule breaker goes
    # Code below currently does not work as intended
    for ruleBreaker in ruleBreakers:
        for x in range(len(toEdit) - 1, -1, -1):
            if ruleBreaker in rulesDict:
                # print('Checking for ' +
                #       toEdit[x] + ' in before dict for ' + ruleBreaker, rulesDict[ruleBreaker]['before'])
                if ruleBreaker in rulesDict[toEdit[x]]['after']:
                    # print("About to write:", ruleBreaker)
                    # toEdit[x: x] = [ruleBreaker]
                    toEdit.insert(x + 1, ruleBreaker)
                    rule_breakers_editable.remove(ruleBreaker)
                    break
    for ruleBreaker in rule_breakers_editable:
        toEdit.append(ruleBreaker)
    print('Correct line:', toEdit)
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
        for y in range(len(numbers) - 1, -1, -1):
            # If num y is in rulesDict then there is a list of rules for what should come after
            if numbers[y] in rulesDict:
                # If number x is found in y rulesDict then
                # num x is in violation of rule num y so it should not count this line
                if numbers[x] in rulesDict[numbers[y]]["after"]:
                    isBad = True
                    print("Rule breaker: " +
                          numbers[x] + ' (' + str(x) + ')' " is supposed to be after " + numbers[y] + ' (' + str(y) + ')')
                    ruleBreakers.append(numbers[x])
                    filteredNumbers.remove(numbers[x])
                    break
    if not isBad:
        print('Good row:', ','.join(numbers))
        midIndex: int = math.floor(len(numbers) / 2)
        midNumData += int(numbers[midIndex])
    else:
        bad_line_total += 1
        print('Bad row:', numbers)
        correctLine = makeCorrectLine(filteredNumbers, ruleBreakers)
        if (len(correctLine)) > 0:
            midNumData += int(correctLine[math.floor(len(correctLine) / 2)])
            f.write(','.join(correctLine))
            f.write('\n')
        else:
            print('Line that became empty is', numbers)

f.close()
print('number of bad lines:', bad_line_total)
