def oops():

    string = "text"
    return string


try:
    raise KeyError

except Exception as a:
    print(type(a))

print(oops())
