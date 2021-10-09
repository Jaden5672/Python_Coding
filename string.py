Name="Josh"
Name1="Sally"
#Upper function for converting the name into uppercase
print (Name.upper())
Nameu=Name1.upper()
NameL=Name1.lower()
print(Nameu,NameL)
#Remove white space from beggining and end
Toy="      Rubick's       Cube            "
print(Toy.strip())
#Replacing the values in a string
a="Hurry Hurry"
print(a.replace("u","a"))
b="funny man"
print(b.replace("n","l"))
#split string into substring
print(b.split("n"))
c="Hi!Hello!I am Jaden!"
print(c.split("!"))
d=c.split("!")
print(d)
print(d[1])
money="15$"
money=int(money.split("$")[0])+20
print(money)
marks="8 out of 10"
marks=(marks.split(" ")[3])
print(marks)
#concatenation
string1="I like"
string2=" to play games"
print(string1+string2)
string1="1"
string2="2"
print(string1+string2)
