colors={"red","blue","yellow","purple","green"}
colors2={"orange","brown","sage"}
colors.add("cyan")
colors.remove("yellow")
print(len(colors))
colors2.discard("magenta")
colors.update(colors2)
print(colors)
