f = open('data.txt', 'r')
content = f.read()
reports = content.split('\n')
# close file now that we are done with it
f.close()

def numCheck(num1: int, num2: int, isAsc: bool) -> bool:
    if((isAsc and (num1 < num2)) or ((not isAsc) and (num1 > num2))):
        diff: int = 0
        if(isAsc):
            diff = num2 - num1
        else:
            diff = num1 - num2
        return diff >= 1 and diff <= 3
    return False

def recursiveCheck(i: int, nums: list[str], isAsc: bool, hasDampenedProblem: bool) -> bool:
    if i == (len(nums) - 1):
        return True
    num1: int = int(nums[i])
    num2: int = int(nums[i + 1])
    if numCheck(num1, num2, isAsc):
        return recursiveCheck(i + 1, nums, isAsc, hasDampenedProblem)
    if not hasDampenedProblem:
        print('Problem row index: ' + str(i) + ' ', nums)
        # Need to check if the first number is the problem
        isFirst: bool = i == 0
        isNotLast: bool = i + 2 <= len(nums) - 2
        if isFirst and isNotLast:
            num3: int = int(nums[i + 2])
            if numCheck(num1, num3, num1 < num3):
                nums.pop(i + 1)
            else:
                nums.pop(i)
        else:
            nums.pop(i + 1)
        return recursiveCheck(i, nums, isAsc, True)
    return False

safeReports: int = 0

for x in range(0, len(reports)):
    levels: list[str] = reports[x].split(' ')
    num1: int = int(levels[0])
    num2: int = int(levels[1])
    isSafe = recursiveCheck(0, levels, num1 < num2, False)
    if(isSafe):
        safeReports += 1
        
print('Safe reports: ' + str(safeReports))