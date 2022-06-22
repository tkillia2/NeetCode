class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mins.append(min(val, self.mins[-1]) if self.mins else val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''
What is happening?
init:
    creation of two stacks one to serve as the true "stack"
    and the other to keep track of the minimum at that time
    this allows for a faster runtime when calling getMin

push:
    simply append the value to the stack list
    append the minimum value between the previous min and the
    current value, if no value yet then current value

pop:   
    just popping the values off the stack -- do it for both
    ensures that keeping track of what the new min is

top:
    returns "back of list" which is top of stack

getMin: 
    since we have a mins list can simply run the identical "top"
    function on the mins stack

'''
