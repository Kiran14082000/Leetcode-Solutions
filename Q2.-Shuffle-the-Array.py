1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3
4        ans=[]
5        even_counter = 0
6        odd_counter=n
7        for i in range(len(nums)):
8            if i%2==0:
9                ans.append(nums[even_counter])
10                even_counter+=1
11            else:
12                ans.append(nums[odd_counter])
13                odd_counter+=1
14        return ans
15
16            