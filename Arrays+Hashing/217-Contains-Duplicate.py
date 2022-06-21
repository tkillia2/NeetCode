class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True
'''
For this problem shoving the list into a set is sufficient for checking for duplicates.
this is b/c a set will only keep one of each value so [1,2,1] as a list would become [1,2] as a set
then checking their lengths against each other will determine if there are duplicates or not
'''
