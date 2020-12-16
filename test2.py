"""Hey, I Already Did That!
========================
Commander Lambda uses an automated algorithm to assign minions randomly to tasks, 
in order to keep her minions on their toes. But you've noticed a flaw in the algorithm - 
it eventually loops back on itself, so that instead of assigning new minions as it iterates, 
it gets stuck in a cycle of values so that the same minions end up doing the same tasks over and over again. 
You think proving this to Commander Lambda will help you make a case for your next promotion. 

You have worked out that the algorithm has the following process: 

1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
4) Assign n = z to get the next minion ID, and go back to step 2

For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. 
Then the next minion ID will be n = 0999
and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.

Depending on the values of n, k (derived from n), and b, 
at some point the algorithm reaches a cycle, such as by reaching a constant value. 
For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] 
and it will stay in this cycle no matter how many times it continues iterating. 
Starting with n = 1211, the routine will reach the integer 6174, and since 7641 - 1467 is 6174, 
it will stay as that value no matter how many times it iterates.

Given a minion ID as a string n representing a nonnegative integer of length k in base b, 
where 2 <= k <= 9 and 2 <= b <= 10, write a function solution(n, b) 
which returns the length of the ending cycle of the algorithm above starting with n. 
For instance, in the example above, solution(210022, 3) would return 3, 
since iterating on 102212 would return to 210111 when done in base 3. 
If the algorithm reaches a constant, such as 0, then the length is 1.

Test cases
==========
-- Python cases --
Input:
solution.solution('1211', 10)
Output:
    1

Input:
solution.solution('210022', 3)
Output:
    3



VINCOLI:
Python
======
Your code will run inside a Python 2.7.13 sandbox. 
All tests will be run by calling the solution() function.
Standard libraries are supported 
except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, 
thread, time, unicodedata, zipimport, zlib.
Input/output operations are not allowed.
Your solution must be under 32000 characters 
in length including new lines and and other non-printing characters.
"""

def solution(n,b):
    lcontrol=[]
    while True :
            
        #calcolo x e y
        lista=[]
        for el in n:
            lista.append(el)
        lista.sort(reverse=True) #ottengo la lista ordinata discendente
        x=""
        for el in lista:         #costruisco la X
            x += el
        lista.sort(reverse=False)
        y=""
        for el in lista:          #costruisco la Y
            y += el
 
        #Calcolo della Z diverso se b10 oppure bx
        #calcolo conversione da base 10 a base b
        if b != 10:
            x=int(x, base=b)
            y=int(y, base=b)
            z = x - y
            stringaNum =""
            while z>0:  
                stringaNum += str(z%b)
                z=z//b
            
            z = ""
            for i in range (len(stringaNum)-1, 0, -1):
                z += stringaNum[i]
        else:
            z=int(x)-int(y)
            z = str(z)
        print("il valore di Z alla riga 99 prima di contr K: ",z)
        print("il valore di X alla riga 99 prima di contr K: ",x)
        print("il valore di Y alla riga 99 prima di contr K: ",y)

        #Controllo il valore di K ed eventualmente lo sitemo
        ka=len(z)
        k = len(n)
        stringa = ""
        if ka < k:                      #sistemo la lunghezza di K
            for i in range (k-ka):
                stringa += "0"
            z = stringa + z
        else:
            pass
        for el in lcontrol:
            if z == el:
                print("Valore di Z dopo controllo                 K:",z)
                print("lunghezza di N : ", len(lcontrol))
                print("i valori di N : ",lcontrol)
                return len(lcontrol)
            else:
                pass

        lcontrol.append(z)
        n = z

        
solution('19333',10)
#solution('1211',10)
#solution('210022', 3)
