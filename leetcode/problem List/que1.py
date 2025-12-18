'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.'''
'''Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]'''
def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                print([seen[diff], i])
            seen[num] = i
nums =[2,7,11,15]
target = 9