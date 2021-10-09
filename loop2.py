for i in range(31):
    if i%2==0:
        print("This number is even",i)
    else:
        print("This number is odd",i)
number=[5,6,7,2,5]
for i in range(5):
    print(number[i])
    number[i]=number[i]+2
print(number)
