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

string = "Hello!"
string = reverse(string)
print("Reversed string is " + string)