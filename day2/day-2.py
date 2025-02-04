f = open('data.txt', 'r')
content = f.read()
reports = content.split('\n')
# close file now that we are done with it
f.close()

def recursiveCheck(i: int, nums: list[str], isAsc: bool) -> bool:
    if i is (len(nums) - 1):
        return True
    num1: int = int(nums[i])
    num2: int = int(nums[i + 1])
    if((isAsc and (num1 < num2)) or ((not isAsc) and (num1 > num2))):
        diff: int = 0
        if(isAsc):
            diff = num2 - num1
        else:
            diff = num1 - num2
        if diff >= 1 and diff <= 3:
            return recursiveCheck(i + 1, nums, isAsc)
    return False

safeReports: int = 0

for x in range(0, len(reports)):
    levels: list[str] = reports[x].split(' ')
    num1: int = int(levels[0])
    num2: int = int(levels[1])
    isSafe = recursiveCheck(0, levels, num1 < num2)
    if(isSafe):
        safeReports += 1
        
print('Safe reports: ' + str(safeReports))