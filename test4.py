number={1,3,6,8,7,9}
for i in number:
    if i%2==0:
        number.discard(i)
        print("Has been removed")
#This will give you an error, because the size of the set changes for every iteration           