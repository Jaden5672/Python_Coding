input1=input("Enter any list of words!")
a=[]
for i in input1.split():
    a.append(i.lower())
print(a)
a.sort()
print(a)

words=[i.lower() for i in input1.split()]
words.sort() 
print(words)