def Rotateright(nums):

    last=nums[-1]
    for i in range(len(nums)-1,-1,-1):
        nums[i]=nums[i-1]
    nums[0]=last
    return nums
nums=list(map(int,input().split()))
# print(Rotateright(nums))

def RotateLeft(nums):
    first=nums[0]
    for i in range(len(nums)-1):
        nums[i]=nums[i+1]
    nums[-1]=first
    return nums
print(RotateLeft(nums))
