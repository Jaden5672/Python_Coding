characters=["Pikachu","Zerrer","Zlither","Wilmer","Yerro"]
card1="Wilmer"
card2="Aloha"
if card1 in characters:
    print("This character is found!")
else:
    print("This character is not found.")
    characters.append(card1)
if card2 in characters:
    print("This character is found!")
else:
    print("This character is not found.")
    characters.append(card2)
print(characters)
