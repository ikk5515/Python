def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    else:
        result = None

    return result


a = add_mul("add", 1, 2, 3)
b = add_mul("mul", 1, 2, 3, 4, 5, 6)
c = add_mul("sub", 1, 2, 3)

print(a, "/", b, "/", c)
