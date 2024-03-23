class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def empty(self):
        return self.size() == 0
        # return len(self.__stack_list) == 0

    def size(self):
        return len(self.__stack_list)

    def top(self):
        return self.__stack_list[-1]

stack = Stack()

print("Jest pusty?", stack.empty())

stack.push("Ala")
stack.push("Tomek")
stack.push("Marta")
stack.push("Agata")

print("Jest pusty?", stack.empty())
print("Ile ma elementów?", stack.size())

print("Na samej górze jest: ", stack.top())

print(stack.pop())
print(stack.pop())
print(stack.pop())