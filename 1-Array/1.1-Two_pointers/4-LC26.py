def RemoveDuplicates(nums):
    slow=0
    for fast in range(1,len(nums)):
        if nums[slow]!=nums[fast]:
            slow+=1
            nums[slow]=nums[fast]
    k=slow+1
    return k
nums=list(map(int,input().split()))
print(RemoveDuplicates(nums))