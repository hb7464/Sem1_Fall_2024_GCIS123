def whilecontinue():
    coun=0
    while coun < 11:
        if coun == 5:
            coun+=1
            continue
        print(coun)
        coun+=1
whilecontinue()