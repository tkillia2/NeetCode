class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1
'''
What is happening?
if the target number exists in the nums list return the index of that value
otherwise return -1
'''
