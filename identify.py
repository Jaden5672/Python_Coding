animals=["pig1","Dog2","pig2","bunny1","horse1","dog1","Bunny2","horse2"]
pig=[]
dog=[]
horse=[]
bunny=[]
for i in animals:
    i=i.lower()
    if i[0]=="p":
        pig.append(i)
    elif i[0]=="d":
        dog.append(i)
    elif i[0]=="b":
        bunny.append(i)
    elif i[0]=="h":
        horse.append(i)
print(pig)
print(dog)
print(horse)
print(bunny)