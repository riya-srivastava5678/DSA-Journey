def threeSum(nums):
    n=len(nums)
    for i in range(len(nums)):
        sums=0
        left=i+1
        right=n-1
        sums=nums[i]+nums[left]+nums[right]
        while left<right:
            if sums<0:
                left+=1
            elif sums>0:
                right-=1

        
            
            