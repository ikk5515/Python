def add_many(*args):
    print(type(args))
    result = 0
    for i in args:
        result += i
    return result


a = add_many(1, 2, 3)
b = add_many(1, 2, 3, 4, 5, 6)

print(a, "/", b)