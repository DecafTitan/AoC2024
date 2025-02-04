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

# Manually sorting massive list is horribly inefficient
list1.sort()
list2.sort()

totalDiff = 0

for i in range(0, len(list1)):
    num1 = list1[i]
    num2 = list2[i]
    if num1 > num2:
        totalDiff += list1[i] - list2[i]
    else:
        totalDiff += list2[i] - list1[i]

print(totalDiff)