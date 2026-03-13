1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3
4        for i in range(len(nums)):
5            index = abs(nums[i]) - 1
6            nums[index] = -abs(nums[index])
7
8        arr = []
9        for i in range(len(nums)):
10            if nums[i] > 0:
11                arr.append(i+1)
12
13        return arr