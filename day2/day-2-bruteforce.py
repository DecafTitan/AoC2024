f = open('data.txt', 'r')
content = f.read()
reports = content.split('\n')
# close file now that we are done with it
f.close()

def recursiveCheck(i: int, nums: list[str], isAsc: bool) -> int:
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

def toInt(x: str) -> int:
    return int(x)

for x in range(0, len(reports)):
    levels: list[str] = reports[x].split(' ')
    numsMain: list[int] = list(map(toInt, levels))
    isSafe: bool = False
    for y in range(0, len(numsMain)):
        nums = numsMain.copy()
        print(nums)
        nums.pop(y)
        num1: int = nums[0]
        num2: int = nums[1]
        safeLevels: bool = recursiveCheck(0, nums, num1 < num2)
        if safeLevels:
            isSafe = True
            break
    if isSafe:
        safeReports += 1
        
print('Safe reports: ' + str(safeReports))