def decor_func(type_:type, max_lenght:int, contains:list):
    def inner(func):
        def actions(args):
            if (
                isinstance(args, type_) and
                len(args) <= max_lenght and
                all(item for item in contains if item in args)
            ):
                return func(args)
            else:
                return False
        return actions
    return inner    
           


@decor_func(type_=str, max_lenght=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW!'


print(create_slogan(''))

