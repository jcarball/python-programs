miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
miLista2 = []
for i in miLista:
    if miLista[i] in miLista:
        del miLista[i]
miLista.sort()
print("La lista solo con elementos únicos:")
print(miLista)