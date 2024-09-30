def loopcontrol():
    sum=0
    while True:
        a = int(input("Enter a number: "))
        if a == 0:
            break
        elif a%2 == 0:
            continue
        else:
            sum=sum+a
    print("Sum is",sum)
loopcontrol()