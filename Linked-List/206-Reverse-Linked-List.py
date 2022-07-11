# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        
        while current:
            next_val = current.next
            current.next = previous
            previous = current
            current = next_val
        return previous
    
'''
What is Happening?

None (previous) -> 1 (current) -> 2 -> 3 -> 4 -> 5  #### example start
**entering while loop**
    next_val = current.next     #### next_val = 2   
    current.next = previous     #### current.next = None
    previous = current          #### previous = 1
    current = next_val          #### current = 2
 NOW:::: None <- 1 -> 2 -> 3 -> 4 -> 5
 
 Second Run: 
    next_val = current.next     #### 2 = 3   
    current.next = previous     #### 3 = 1
    previous = current          #### 1 = 2
    current = next_val          #### 2 = 3
NOW :::: None <- 1 <- 2 -> 3 -> 4 -> 5

This will continue essentially flipping the previous and next values until there
are no more entries in the list, it then returns the new "head" which will actually be equal to the previous value
'''
