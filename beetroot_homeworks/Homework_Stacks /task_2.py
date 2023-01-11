def Balanced(exp):
    n_exp = ""
    for item in exp:
        if item in ["(", ")", "(", ")"]:
            n_exp += item
    stack = []
    for char in n_exp:
        if char in ["(", "{"]:
            stack.append(char)
        else:
            if not stack:
                return False
            cur_char = stack.pop()
            if cur_char == "(":
                if char != ")":
                    return False

            if cur_char == "{":
                if char != "}":
                    return False
    if stack:
        return False
    return True


string = "(((({{{{}}}}))))"
print(Balanced(string))
