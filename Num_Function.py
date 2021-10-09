storing=[]
count=input("How many numbers do you want to type in?")
count=int(count)
for i in range(0,count):
    a=input("Enter the number!"+str(i)+":")
    storing.append(int(a))
print(min(storing))
print(max(storing))