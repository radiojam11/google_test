#data =   [1, 2, 3]
#data =   [1, 2, 2, 3, 3, 3, 4, 5, 5]
data =[1,2,3,8,3,4,5,5,6, 7, 3, 2, 2, 3, 2]
soglia = 2
diz={}
risultato = []
for el in set(data):           #per tutti i numeri unici della lista
    indice = []
    for i in range(len(data)): #per tutti gli indici della lista
        if el == data[i]:      # se trovo il numero unico 
            indice.append(i)    #mi segno il suo indice nella lista indice
        diz[el] = indice        #aggiugno al dizionario diz la chiave(numero unico) e come valore la lista delle posizioni (indice)
for key in diz:                 #adesso ho un dizionario di chiave(numero unico della lista originale) e valore( una lista delle sue posizioni nella lista)
    if len(diz[key]) <= soglia: #se il numero delle ricorrenze del numero unico e' inferiore alla soglia, 
        risultato.append(key)   #lo prendo e lo registro in risultato che e' la lista finale 


##                  ##DA RIVEDERE PERCHE' NON MANTIENE LA POSIZIONE ORIGINALE DEL NUMERO NELLA LISTA - DIPENDE DALL'ORDINAMENTO DEL DIZIONARIO ##

print(data)

print(diz)
print(risultato)
