class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedMap = { ')': '(', ']' : '[', '}': '{' }
        for char in s:
            if char in closedMap:
                if stack and stack[-1] == closedMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
'''
What is happening?
initialize the "stack", a list, and the closedMap, a dictionary
from there iterate over each character in the string
if that character is in the closedMap's keys --> ), ], }
then check if the stack exists(not empty) AND 
    if the most recent element of the stack is the corresponding 'value' or open version
    i.e '(' would be added to the stack b/c it is not in closedMap's keys then when ')'
        appears it would see that the most recent open bracket is ( and it would be popped
    pop the open bracket from stack
    if it does not match then it's false
    append all open brackets
at the end if the stack is not empty return False, if it is empty True

Essentially adding all open parentheses versions onto the stack and then each time a 
closing parentheses is seen you check if the most recent opened parentheses (which is stack[-1])
is the corresponding open version of that closed one, if it is pop (remove) that open
if it is not then it is false
and then ensure that all opened parentheses have been closed at the end before returning true
'''    
