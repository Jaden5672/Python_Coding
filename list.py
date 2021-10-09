fruits=["Apple","Apple","Bananas","Blueberry"]
print(fruits)
#duplicates are allowed in a list
mixed=["Car",56,789,"cat",True,"bus"]
print(mixed)
#A list allows multiple data types
print(type(fruits))
print(mixed[0:4])
print(mixed[:2])
mixed[0]= "Jeep"
print(mixed)
#you can change the values of a list, these types of varibles are called mutable
print(mixed[-4:-1])
print(mixed[-5:-1])
if "truck" in mixed:
    print("Cat is present in this list!")
else:
    print("This value is not present in this list.")
mixed[1:3]= ["Sheep",200]
print(mixed)
mixed[0:4]=["Milk","Apple",66,"pizza"]
print(mixed)
mixed[0:1]=["Forest","Farm",101]
print(mixed)
print(len(mixed))
mixed[0:2]=["Earth"]
print(mixed)
print(len(mixed))
mixed.insert(1,False)
print(mixed)