def SingleNumber(nums):
    n = len(nums)
    visited = [False for i in range(n)]

    for i in range(n):

        if (visited[i] == True):
            continue

        SingleNumber = 1
        for j in range(i + 1, n, 1):
            if (nums[i] == nums[j]):
                visited[j] = True
                SingleNumber += 1
        if SingleNumber == 1:
            print(nums[i])


nums = str(input("Enter the numbers:"))
list = nums.split (",")
SingleNumber(nums)
