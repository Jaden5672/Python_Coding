choice=input("Type in 1 for Kilograms to pound, or 2 for pound to Kilograms:")
if choice=="1":
    
    kg=input("Type in any number of kilograms to convert to pounds:")
    kg=float(kg)
    pound=kg*2.204
    print(pound)
elif choice=="2":
    pound1=input("Type in any amount of pounds to convert into kilograms:")
    pound1=float(pound1)
    kg1=pound1/2.204
    print(kg1)
else:
    print("invalid choice!try again")