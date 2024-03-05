from stack_oop import Stack

s1 = Stack()
s2 = Stack()
s3 = Stack()

for i in range(1, 101):
    s1.push(i)

for _ in range(100):
    s2.push(s1.pop())

for _ in range(100):
    s3.push(s2.pop())

for _ in range(100):
    print(s3.pop(), end=" ")