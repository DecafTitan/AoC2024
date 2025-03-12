import re

f = open('data.txt', 'r')
content = f.read()
# close file now that we are done with it
f.close()

regex: str = re.compile("mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)")

matches: list[str] = re.findall(regex, content)

canMultiply: bool = True

total:int = 0


print(matches)

for match in matches:
    if match == 'do()':
        canMultiply = True
        continue
    if match == 'don\'t()':
        canMultiply = False
        continue
    if canMultiply:
        splitter1 = match.split(')')[0]
        splitter2 = splitter1.split('mul(')[1]
        splitter3 = splitter2.split(',')
        mul = int(splitter3[0]) * int(splitter3[1])
        total += mul
        print(match + ' = ' + str(mul) + ' total is ' + str(total))
print(total)
