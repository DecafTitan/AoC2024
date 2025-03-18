f = open("../rules.txt", "r")
rulesContent = f.read()
rules = rulesContent.split("\n")
# close file now that we are done with it
f.close()

f = open("filtered-data.txt", "r")
content = f.read()
data: list[str] = content.split("\n")
# close file now that we are done with it
f.close()

ruleStr: str = ""

f = open("filtered-rules.txt", "w")

for line in data:
    for index in range(0, len(rules)):
        if '|' in rules[index]:
            splitter = rules[index].split("|")
            if splitter[0] in line and splitter[1] in line:
                ruleStr += rules[index] + "\n"

f.write(ruleStr[0: len(ruleStr) - 1])
f.close()
print("Finished writing test rules")
