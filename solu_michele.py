"""

ESERICIZIO:
Write a function called solution(data, n) 
that takes in a list of less than 100 integers and a number n, 
and returns that same list 
but with all of the numbers that occur more than n times("ma
con tutti i numeri che occorrono piu di n volte") removed entirely. 
The returned list should retain the same ordering as the original list - 
you don't want to mix up ("confondere") those carefully-planned shift rotations! 
For instance, if data was [5, 10, 15, 10, 7] and n was 1,
solution(data, n) would return the list [5, 15, 7] because 10 occurs twice, 
and thus was removed from the list entirely

VINCOLI:
Your code will run inside a Python 2.7.13 sandbox. 
All tests will be run by calling the solution() function.

Standard libraries are supported 
except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, 
signal, termios, thread, time, unicodedata, zipimport, zlib.

Input/output operations are not allowed.

Your solution must be under 32000 characters in length 
including new lines and and other non-printing characters.

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([1, 2, 3], 0)
Output:
    

Input:
solution.solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
Output:
    1,4

 """



#data =   [1, 2, 2, 3, 3, 3, 4, 5, 5]
#data =   [1, 2, 3]
#data =   [2,7,7,1,3,4,7,9,5,4,5,6,5,6]



data  = [5,1,15,11,5,2, 5, 5, 8, 9, 8, 6, 3]
n = 1

#soluzione prima
def solution(data, n):
    data2 = []                              #creo un alista vuota
    for el in data:                         #per ogni elemento della lista originale
        data2.append(el)                    #creo la lista 2 gemella
    for el in set(data):                    #per ogni elemento nel set(lista), quindi per ogni elemento unico in lista
        if data.count(el) > n:              #se il numero delle ricorrenze e' inferiore alla soglia
            for r in range(data.count(el)): #ciclo tante volte quanto il numero unico e' presente nella lista
                data2.remove(el)            #e lo cancello tante volte fino ad eliminarlo completamente
    return data2                            #ritorno la lista dei numeri definitivi

#soluzione 2 ma da sistemare l'ordinamento

def solution2(data, n):                     #invece di costruire la lista gemella, la riempio direttamente quando trovoun elemento sotto soglia
    data2=[]                                #creo la lista 2 vuota
    for el in set(data):                     #per ogni elemento nel set(lista), quindi per ogni elemento unico in lista
        if data.count(el) <= n:              #se il numero delle ricorrenze e' inferiore alla soglia
            data2.append(el)                  #e lo appendo alla lista 2 che inizialmente e' vuota (quindi conterra' solo quello che seerve)
    return data2                        


print(solution2(data, n))
print(data)
print(solution(data, n))


"""   list comprehention
def solutions1(data, n):
    data2 = []
    for el in data:
        data2.append(el)   
    data2.remove(el for el in set(data) if data.count(el) > n for i in range(data.count(el)) 
    return data2

print(solutions1(data, n))

"""