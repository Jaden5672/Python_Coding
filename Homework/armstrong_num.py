number=input("Enter any number to out find if it is an armstrong number or not!")
number=(int(number))
temp=number
a=(temp%10)
temp=temp//10
b=(temp%10)
temp=temp//10
c=(temp)
armstrong=((a*a*a)+ (b*b*b)+ (c*c*c))
if armstrong==number:
    print("This is a armstrong number!")
else:
    print("This is not an armstrong number!")