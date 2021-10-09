year=input("Type in any year!")
year=int(year)
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("This year is a leap year!")
        else:
            print("This year is not a leap year!")
    else:
        print("This is a leap year!")
else:
    print("This is not a leap year!")