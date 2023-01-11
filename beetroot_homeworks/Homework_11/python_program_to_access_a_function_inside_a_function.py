def result_func(text):
    def up_func(t):

        return t.upper()

    return up_func(text)


result_func("Hi")
