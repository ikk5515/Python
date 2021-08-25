for i in range(5):
    print(' ')
    for j in range(i):
        print(' ',end='')
    for j in range(2*(5-i)-1):
        print("*",end='')