1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        
4        max=0
5        count=0
6        for i in range(len(nums)):
7            if nums[i]==1:
8                count+=1
9            else:
10                if max<count:
11                    max=count
12                count=0
13                
14        if max<count:
15            max = count
16        return max
17        