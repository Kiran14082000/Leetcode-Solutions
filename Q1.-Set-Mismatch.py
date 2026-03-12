1class Solution:
2    def findErrorNums(self, nums: List[int]) -> List[int]:
3        duplicate = 0
4        missing = 0
5        n = len(nums)
6
7        s = set()
8
9        for num in nums:
10            if num in s:
11                duplicate = num
12            s.add(num)
13
14        for i in range(1, n+1):
15            if i not in s:
16                missing = i
17
18        return [duplicate, missing]