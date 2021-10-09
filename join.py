group1=["Mike","James","Sally","Susan"]
group2=["Bill","Robert","Elizibeth"]
group=group1+group2
print(group)
fruits=["apple","orange","blueberry"]
fruits1=["watermelon","strawberry"]
for i in fruits1:
    fruits.append(i)
print(fruits)
veggies=["cumcumber","tomato","spinach"]
veggies1=["carrot","potato"]
veggies.extend(veggies1)
print(veggies)