number=[5,7,2,4,3,1,6,8]
even=[]
odd=[]
for i in number:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort()
print(even)
print(odd)