class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class StackSum(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

# stack1 = StackSum()

# --------------------------------------------------- 3 podejście

# for i in range(20):
#     stack1.push(i)
#
# print(stack1.get_sum())
#
# for i in range(5):
#     stack1.pop()
#
# print(stack1.get_sum())
# --------------------------------------------------- 2 podejście

# stack1.push(1)
# stack1.push(2)
# stack1.push(3)
#
# print("Suma: ", stack1.get_sum())
#
# print(stack1.pop())
# print("Suma: ", stack1.get_sum())
# print(stack1.pop())
# print("Suma: ", stack1.get_sum())
# print(stack1.pop())
# print("Suma: ", stack1.get_sum())


# --------------------------------------------------- 1 podejście

# stack1 = Stack()
# stack2 = Stack()
#
# stack1.push(1)
# stack2.push("Ala")
# stack1.push(2)
# stack2.push("Tomek")
# stack2.push("Agata")
# stack1.push(3)
#
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())
#
# print(stack2.pop())
# print(stack2.pop())
# print(stack2.pop())