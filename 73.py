def solution(nums,target):
	if len(nums) < 2:
            return
for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                     return [i, j]
