name="Jaden is developer"
print(name)
print(name[5])
story=""" The quick brown fox jumped over the big lazy dog
Old mcdonald had a cow that live on his farm
he also had some pigs.
"""
print(story)
for i in name:
    print(i)
count=len(name)
print(count)
"""length=input("Type in a sentence less than 10 characters in length!")
count=len(length)
if count<=10:
    print("Very good!You have passed")
else:
    print("This sentence contains more than 10 characters,try again!")"""
print("z" in name)
print(20<10)
#exept for number 0,the boolean function returns true for a number
print(bool(10))
print(bool(None))
a=13
print(isinstance(a,int))
b="This is a string"
print(isinstance(b,str))
string=input("Type in a string!")
print(isinstance(string,str))
number=input("enter a number")
number=int(number)
print(isinstance(number,int))