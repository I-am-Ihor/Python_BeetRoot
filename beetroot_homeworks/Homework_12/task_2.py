def decor_func(words: list):
    def inner(func):
        def action(args):

            z = args.split()
            y = []
            for word in z:

                if word in words:
                    word = "*"

                    y.append(word)
                else:
                    y.append(word)

            return func(" ".join(y))

        return action

    return inner


@decor_func(words=["yes", "no", "and"])
def find_stop(name):
    return name


name = "yes no beetroot the best"


print(find_stop(name))
