def createStack():
    stack = []
    return stack


def size(stack):
    return len(stack)


def isEmpty(stack):
    if size(stack) == 0:
        return True


def push(stack, item):
    stack.append(item)


def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()


def reverse(string):
    n = len(string)
    stack = createStack()
    for i in range(0, n):
        push(stack, string[i])
    string = ""
    for i in range(0, n):
        string += pop(stack)
    return string


def get_from_stack(stack, value):
    value2 = ""
    new_stack = []
    if value not in stack:
        pass

    for char in stack:
        if char == value:
            new_stack.append(None)

            value2 += char
        else:
            new_stack.append(char)
    print(new_stack)
    return value2


string = "Hello!"
string3 = get_from_stack(string, "o")
print(string3)
