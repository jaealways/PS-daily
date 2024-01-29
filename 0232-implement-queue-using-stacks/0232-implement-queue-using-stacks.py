class MyQueue:

    def __init__(self):
        self.array=[]

    def push(self, x: int) -> None:
        self.array.append(x)

    def pop(self) -> int:
        result=self.array[0]
        self.array=self.array[1:]
        return result

    def peek(self) -> int:
        return self.array[0]

    def empty(self) -> bool:
        if len(self.array)>0:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()