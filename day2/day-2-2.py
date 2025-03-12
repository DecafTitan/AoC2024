f = open('data.txt', 'r')
content = f.read()
reports = content.split('\n')
# close file now that we are done with it
f.close()

def handleSameNumbers(i:int, isAsc: bool, nums: list[str]):
    # Pop either one off since this is the last comparison, the next check will return True
    nums.pop(i)
    # This is to check if this is the last recursiveCheck for the reports
    if (i + 1) >= len(nums) - 1:
        return True
    return recursiveCheck(i, nums, True, True)

# Check whether the difference between number 1 and number 2 is bigger than 0 and less than 4
def numCheck(num1: int, num2: int, isAsc: bool) -> bool:
    if((isAsc and (num1 < num2)) or ((not isAsc) and (num1 > num2))):
        diff: int = 0
        if(isAsc):
            diff = num2 - num1
        else:
            diff = num1 - num2
        return diff >= 1 and diff <= 3
    return False

# Recursive function to call numCheck for all of the numbers in the given row
# If it is the last number it should just exit out since there is no other number to compare to
# Now if numCheck returns false it should remove the problematic number from the row so it is valid and check again... ideally... but it is currently not doing that correctly
def recursiveCheck(i: int, nums: list[str], isAsc: bool, hasDampenedProblem: bool) -> bool:
    if i == (len(nums) - 1):
        return True
    # Need to convert numbers to ints because they are currently strings from being parsed from a .txt file
    num1: int = int(nums[i])
    num2: int = int(nums[i + 1])
    # If it passes the first check, do the recursive check for the rest of the numbers
    if numCheck(num1, num2, isAsc):
        return recursiveCheck(i + 1, nums, isAsc, hasDampenedProblem)
    if not hasDampenedProblem:
        print('Problem row index: ' + str(i) + ' ', nums)
        if num1 == num2:
            # Pop either one off since this is the last comparison, the next check will return True
            nums.pop(i + 1)
            # This is to check if this is the last recursiveCheck for the reports
            if (i + 1) >= len(nums) - 1:
                return True
            # Now getting new next number to check if it is ascending or descendind
            num2 = int(nums[i + 1])
            return recursiveCheck(i, nums, isAsc, True)
        # If this is true then just do a basic check since it is the last two numbers
        # or the only two numbers
        if i == len(nums) - 2:
            return numCheck(num1, num2, isAsc)
        # If this is true then it is currently on the third last number so just check which number in the sequence is wrong (if there is a right answer)
        # This will also work if the sequence is only 3 numbers
        if i == len(nums) - 3:
            num3: int = int(nums[i + 2])
            check1: bool = numCheck(num1, num3, isAsc)
            check2: bool = numCheck(num2, num3, isAsc)
            if(check1 or check2):
                if check1:
                    nums.pop(i + 1)
                if check2:
                    nums.pop(i) 
                return recursiveCheck(i + 1, nums, isAsc, True)
        # if it is the first number and it is at least 4 numbers reassess whether it is ascending
        # or descending using the first four numbers and remove the problem number
        if i == 0:
            num3: int = int(nums[i + 2])
            check1A: bool = numCheck(num1, num3, True)
            check1B: bool = numCheck(num1, num3, False)
            check2A: bool = numCheck(num2, num3, True)
            check2B: bool = numCheck(num2, num3, False)
            if check1A or check1B:
                nums.pop(i + 1)
                print('Just popped array')
                print(nums)
                return recursiveCheck(i + 1, nums, check1A, True)
            if check2A or check2B:
                nums.pop(i)
                return recursiveCheck(i + 1, nums, check2A, True)
    return False

safeReports: int = 0


# Loop through each report and add to the number of the safe reports
for x in range(0, len(reports)):
    # Adding this to handle test data
    if reports[x] == '':
        continue
    # Splitting the string to get the array of numbers
    levels: list[str] = reports[x].split(' ')
    num1: int = int(levels[0])
    num2: int = int(levels[1])
    hasDampened: bool = False
    
    if num1 == num2:
        levels.pop(1)
        # Get new next number for comparison
        num2 = int(levels[1])
        hasDampened = True

    # Starting recursive check with the first two numbers
    # If number 1 is smaller than number 2 then the report is ascending
    # If number 2 is smaller than number 1 then the report is descending
    isSafe = recursiveCheck(0, levels, num1 < num2, hasDampened)
    if(isSafe):
        safeReports += 1
        
print('Safe reports: ' + str(safeReports))