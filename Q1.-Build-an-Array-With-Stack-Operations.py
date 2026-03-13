1class Solution:
2    def buildArray(self, target: List[int], n: int) -> List[str]:
3        arr=[]
4        s=[]
5        #Output: ["Push","Push","Pop","Push"]
6
7        for i in range(1,n+1):
8            arr.append(i)
9
10        j=0
11        for i in arr:
12            if j == len(target):
13                break
14            if i in target:
15                s.append("Push")
16                j+=1
17            else:
18                s.append("Push")
19                s.append("Pop")
20        return s