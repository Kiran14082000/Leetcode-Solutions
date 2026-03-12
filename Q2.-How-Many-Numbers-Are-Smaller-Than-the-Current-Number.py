1class Solution:
2    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
3        arr=[]
4        for i in range(len(nums)):
5            c=0
6            for j in range(len(nums)):
7                if nums[i]>nums[j]:
8                    c+=1
9            arr.append(c)
10        return arr