
#Gabrio
lista =[1,2,3,8,3,4,5,5,6, 7, 3, 2, 2, 3, 2]
soglia = 2
d = {}

# calcola il numero di occorrenze per ogni elemento
for elem in lista:
    if elem not in d:
        d[elem] = 0
    d[elem]+=1

# calcola risultato, che esclude numeri che appaiono troppo
risultato = []
for elem in lista:
    if d[elem] < soglia:
        risultato.append(elem)
    else:
        pass

print(risultato)
