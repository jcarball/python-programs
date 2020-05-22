palabraSinVocal = ""

userWord = input("Ingrese su palabra:")
userWord = userWord.upper ()

for letra in userWord:
	if letra == "A":
		continue
	elif letra == "E":
		continue
	elif letra == "I":
		continue
	elif letra == "O":
		continue
	elif letra == "U":
		continue
	else:
		palabraSinVocal= palabraSinVocal + letra

print(palabraSinVocal)