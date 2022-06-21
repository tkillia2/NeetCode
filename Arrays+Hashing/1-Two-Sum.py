class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        for n in range(len(nums)):
#            for m in range(len(nums)):
#                if nums[n] + nums[m] == target and n != m:
#                    return [n,m]
        hashmap = {}
        for index, number in enumerate(nums):
            val = target - number
            if val in hashmap:
                return hashmap[val], index # returnable in any order
            hashmap[number] = index
'''
hashmap is of the form --> value: index
what is happening?
within this list there must be two values such that a+b = target
in other words target - a = b or target - b = a
so this code is checking if those a and b pairings exist such that the target can be summed
the catch is that if the hashmap is populated prior to this check we will could return something like where nums[0] = 2 and the target is 4
then, if the hashmap was populated prior to checking, it would return 0, 0 which is invalid
'''
