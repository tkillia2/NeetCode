class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        # s = ''.join(char for char in s.isalnum()) # same thing if filter confusing
        if s.lower() == s.lower()[::-1]:
            return True
        return False
'''
The first line is removing all of the spaces and joining the sentence or phrase into one "word". It then goes through and filters out anything that is non-alphanumeric and does not keep that as part of the "s" string

This new string is then brought into the following conditional where it is made lowercase and compared to its reversed string (also lowercased)

if they are the same return true else false
[::-1] means start at the end of s, and end at the beginning with a step of -1
'''
