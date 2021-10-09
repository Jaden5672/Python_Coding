pick=input("Type in A to convert miles to kilometers,or type in B to convert kilometers to miles:")
pick=pick.upper()
if pick=="A":
    miles=input("Enter any number of miles to convert to kilometers")
    miles=float(miles)
    km=miles*1.609
    print(km)
elif pick=="B":
    kilometers=input("Enter any number of kilometers to convert to miles")
    kilometers=float(kilometers)
    mile1=kilometers/1.609
    print(mile1)
else:
    print("Invalid operation!Try again")