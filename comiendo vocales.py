userWord = input("Ingresa tu palabra:")
userWord = userWord.upper ()

for letter in userWord:
    if letter == "A" or letter == "E" or letter == "I" or letter=="O" or letter == "U":
        continue
    else:
        print(letter)
    


