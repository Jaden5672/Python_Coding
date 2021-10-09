trees={"Maple","Evergreen","Pine Tree"}
print(trees)
print(trees)
trees=["Maple","Maple","Maple"]
print(trees)
trees={"Maple","Maple","Maple"}
print(trees)
trees={"Maple","Evergreen","Pine Tree"}
print(len(trees))
b={True,False,False,True}
print(b)
random={"Ball",700,True,"day",2,"Dog"} 
print(random)
print(type(random))
names=["Josh","Andy","Sara"]
print(type(names))
for i in random:
    print(i)
print("Wall" in random)
random.add("Wall")
print(random)
trees.update(random)
print(trees)
random.remove("Wall")
print(random)
random.discard("Milk")
print(random)
e=random.pop()
print(random)
print(e)
#random.clear()
del random
#print(random)
#Clear will remove the contents of the list, but will still keep the list
#Del will remove the list entirely