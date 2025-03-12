f = open('data.txt', 'r')
content = f.read()
splitter = content.split('\n')
# close file now that we are done with it
f.close()

# Data has two lists of equal length so no equal length checking needed
list1 = []
list2 = []

for nums in splitter:
    split2 = nums.split('   ')
    list1.append(int(split2[0]))
    list2.append(int(split2[1]))


similarityDict = {}

total = 0

for x in range(0, len(list1)):
    if list1[x] in similarityDict:
        similarityDict[list1[x]]['left'] += 1
    else:
        similarityDict[list1[x]] = { 'left': 1, 'right': 0 }
    
for x in range(0, len(list2)):
    if list2[x] in similarityDict:
        similarityDict[list2[x]]['right'] += 1

print(similarityDict)

for (key, value) in similarityDict.items():
    print('key: ' + str(key))
    total += key * value['left'] * value['right']

print(total)