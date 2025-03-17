import math
import json

f = open('../rules.txt', 'r')
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

f = open('rules.json', 'w')

json.dump(rulesDict, f)

f.close()
