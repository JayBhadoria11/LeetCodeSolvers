1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        a = []
5
6        for i in range(len(nums) - 2):
7
8            if i > 0 and nums[i] == nums[i - 1]:
9                continue
10
11            left = i + 1
12            right = len(nums) - 1
13
14            while left < right:
15                total = nums[i] + nums[left] + nums[right]
16
17                if total == 0:
18                    a.append([nums[i], nums[left], nums[right]])
19
20                    left += 1
21                    right -= 1
22
23                    while left < right and nums[left] == nums[left - 1]:
24                        left += 1
25
26                    while left < right and nums[right] == nums[right + 1]:
27                        right -= 1
28
29                elif total < 0:
30                    left += 1
31
32                else:
33                    right -= 1
34
35        return a