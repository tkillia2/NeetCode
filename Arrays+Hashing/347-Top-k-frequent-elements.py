class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for number in nums:
            if number not in d:
                d[number] = 1
            else:
                d[number] += 1
        max_vals = sorted(d, key=d.get, reverse=True)
        return(max_vals[:k])

    
'''
WHAT'S HAPPENING?
create the dictionary
for every number in the nums list (input)
    check if that number is in the dictionary yet 
        (if not make it 1 as in seen it once)
        (if yes - add one to it as in seen it one more time)
then sort the dictionary based on its values (this traditionally goes L->G so reverse it)
then return the max_vals list from the beginning to the kth entry to get the top k elements
'''
