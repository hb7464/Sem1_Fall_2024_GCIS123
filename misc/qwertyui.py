c = ''
while True:
    c = input("Enter x to break the loop, enter anything else to continue: ")
    if c == 'x':
        break
    elif c == 'X':
        print("Not the correct x")
        continue
    print('brr')