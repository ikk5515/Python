def get_formatted_name(first, last):
    fullname = f"{first} {last}".title()
    return fullname


while True:
    print("\nTell me your name (quit: q)")

    f_name = input("First Name: ")
    if f_name.lower() == 'q':
        break

    l_name = input("Last Name: ")
    if f_name.lower() == 'q':
        break

    fullname = get_formatted_name(f_name, l_name)
    print(f"Hello, {fullname}")
