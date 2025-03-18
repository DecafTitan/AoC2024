import math
import json

f = open('../rules.txt', 'r')
rulesContent = f.read()
rules = rulesContent.split('\n')
# close file now that we are done with it
f.close()

rulesArrays: dict[str, list[str]] = {}
rulesDict: dict[str, dict[str, str]] = {}

for rule in rules:
    splitter = rule.split('|')
    if splitter[0] in rulesArrays:
        rulesDict[splitter[0]][splitter[1]] = ''
        rulesArrays[splitter[0]].append(splitter[1])
    else:
        # New dict in rulesDict will contain values that come after the number according to the rules
        rulesArrays[splitter[0]] = [splitter[1]]
        rulesDict[splitter[0]] = {}
        rulesDict[splitter[0]][splitter[1]] = ''

for rule in rulesArrays:
    rulesArrays[rule] = sorted(rulesArrays[rule])


json.dump(rulesArrays, open('rules.min.json', 'w'), sort_keys=True)

json.dump(rulesArrays, open('rules.json', 'w'), sort_keys=True, indent=4)

json.dump(rulesDict, open('rules.dict.json', 'w'), sort_keys=True, indent=4)

f.close()
