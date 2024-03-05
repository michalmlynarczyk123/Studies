class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class StuckSum(Stack):
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

# stack_obj = Stack()
# # # print(len(stack_obj.stack_list))
# stack_obj.push(1)
# stack_obj.push(2)
# stack_obj.push(3)
# #
# print(stack_obj.pop())
# print(stack_obj.pop())
# print(stack_obj.pop())

# stack_obj1 = Stack()
# stack_obj2 = Stack()
#
# stack_obj1.push(1)
# stack_obj2.push("Ala")
# stack_obj1.push(2)
# stack_obj2.push("ma")
# stack_obj1.push(3)
# stack_obj2.push("kota.")
#
# print(stack_obj1.pop())
# print(stack_obj1.pop())
# print(stack_obj1.pop())
# print(stack_obj2.pop())
# print(stack_obj2.pop())
# print(stack_obj2.pop())

# ------------------------------------------------------------------

stack1 = StuckSum()
# stack1.push(1)
# stack1.push(2)
# stack1.push(3)
#
# print("Suma elementów: ", stack1.get_sum())
#
# print(stack1.pop())
# print("Suma elementów: ", stack1.get_sum())
# print(stack1.pop())
# print("Suma elementów: ", stack1.get_sum())
# print(stack1.pop())
# print("Suma elementów: ", stack1.get_sum())

# ------------------------------------------------------------------

# for i in range(20):
#     stack1.push(i)
# print(stack1.get_sum())
#
# for i in range(5):
#     stack1.pop()
# print(stack1.get_sum())