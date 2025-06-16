expression = input()
stack = []

for i in expression:
    if i == "+":
        stack.append(stack.pop() + stack.pop())
    elif i == "-":
        a, b = stack.pop(), stack.pop()
        stack.append(b - a)
    elif i == "*":
        stack.append(stack.pop() * stack.pop())
    elif i == "/":
        a, b = stack.pop(), stack.pop()
        stack.append(b / a)
    else:
        stack.append(int(i))

print(stack[0])
