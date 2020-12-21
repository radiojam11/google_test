"""ESERCIZIO:

You got the guards to teach you a card game today, 
it's called Fizzbin. It's kind of pointless, 
but they seem to like it and it helps you pass the time 
while you work your way up to Commander Lambda's inner circle.

Rumor has it the prison guards are inexplicably fond of bananas. 
You're an apple person yourself, 
but you file the information away for future reference. 
You never know when you might need to bribe a guard (or three)...

Lovely Lucky LAMBs
==================

Being a henchman isn't all drudgery. 
Occasionally, when Commander Lambda is feeling generous, 
she'll hand out Lucky LAMBs (Lambda's All-purpose Money Bucks). 
Henchmen can use Lucky LAMBs to buy things like a second pair of socks, 
a pillow for their bunks, or even a third daily meal!

However, actually passing out LAMBs isn't easy. 
Each henchman squad has a strict seniority ranking which must be respected - 
or else the henchmen will revolt and you'll all get demoted back to minions again! 

There are 4 key rules which you must follow in order to avoid a revolt:
    1. The most junior henchman (with the least seniority) gets exactly 1 LAMB.  
	(There will always be at least 1 henchman on a team.)
    2. A henchman will revolt if the person 
	who ranks immediately above them gets more than double the number of LAMBs they do.
    3. A henchman will revolt if the amount of LAMBs given to their next two subordinates 
	combined is more than the number of LAMBs they get.  
	(Note that the two most junior henchmen won't have two subordinates,
	so this rule doesn't apply to them.  
	The 2nd most junior henchman would require at least as many LAMBs as the most junior henchman.)
    4. You can always find more henchmen to pay - the Commander has plenty of employees.  
	If there are enough LAMBs left over such that another henchman could be added as the most senior 
	while obeying the other rules, you must always add and pay that henchman.

Note that you may not be able to hand out all the LAMBs. 
A single LAMB cannot be subdivided. That is, 
all henchmen must get a positive integer number of LAMBs.

Write a function called solution(total_lambs), 
where total_lambs is the integer number of LAMBs in the handout you are trying to divide. 
It should return an integer 
which represents the difference between the minimum and maximum number of henchmen 
who can share the LAMBs 
(that is, being as generous as possible to those you pay and as stingy as possible, respectively) 
while still obeying all of the above rules to avoid a revolt.  
For instance, if you had 10 LAMBs and were as generous as possible, 
you could only pay 3 henchmen (1, 2, and 4 LAMBs, in order of ascending seniority), 
whereas if you were as stingy as possible, 
you could pay 4 henchmen (1, 1, 2, and 3 LAMBs). 
Therefore, solution(10) should return 4-3 = 1.

To keep things interesting, Commander Lambda varies the sizes of the Lucky LAMB payouts. 
You can expect total_lambs to always be a positive integer less than 1 billion (10 ^ 9).

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(143)
Output:
    3

Input:
solution.solution(10)
Output:
    1

VINCOLI:
Python
======
Your code will run inside a Python 2.7.13 sandbox. 
All tests will be run by calling the solution() function.

Standard libraries are supported except for 
bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, 
termios, thread, time, unicodedata, zipimport, zlib.

Input/output operations are not allowed.

Your solution must be under 32000 characters in length 
including new lines and and other non-printing characters.

##########################################################

ESERCIZIO:

Hai le guardie per insegnarti un gioco di carte oggi,
si chiama Fizzbin. È un po 'inutile
ma a loro sembra piacere e ti aiuta a passare il tempo
mentre ti fai strada fino alla cerchia ristretta del Comandante Lambda.

Si dice che le guardie carcerarie amino inspiegabilmente le banane.
Anche tu sei una persona mela,
ma archivi le informazioni per riferimento futuro.
Non sai mai quando potresti dover corrompere una guardia (o tre) ...

Lovely Lucky LAMBs
==================

Essere uno scagnozzo non è tutto faticoso.
Occasionalmente, quando il comandante Lambda si sente generoso,
distribuirà Lucky LAMBs (i soldi per tutti gli usi di Lambda).
Gli scagnozzi possono usare Lucky LAMBs per comprare cose come un secondo paio di calzini,
un cuscino per le loro cuccette, o anche un terzo pasto giornaliero!

Tuttavia, in realtà distribuire gli AGNELLI non è facile.
Ogni squadra di scagnozzi ha una rigorosa classifica di anzianità che deve essere rispettata -
altrimenti gli scagnozzi si ribelleranno e verrete tutti retrocessi di nuovo a servitori!

Ci sono 4 regole chiave che devi seguire per evitare una rivolta:
    1. Lo scagnozzo più giovane (con la minore anzianità) ottiene esattamente 1 AGNELLO.
(Ci sarà sempre almeno 1 scagnozzo in una squadra.)
    2. Uno scagnozzo si ribellerà se la persona
chi si colloca immediatamente sopra di loro ottiene più del doppio del numero di AGNELLI che ottengono.
    3. Uno scagnozzo si ribellerà se la quantità di AGNELLI sarà data ai suoi successivi due subordinati
combinato è più del numero di AGNELLI che ottengono.
(Nota che i due scagnozzi più giovani non avranno due subordinati,
quindi questa regola non si applica a loro.
Il secondo scagnozzo più giovane richiederebbe almeno tanti AGNELLI quanti lo scagnozzo più giovane.)
    4. Puoi sempre trovare più scagnozzi da pagare: il Comandante ha molti dipendenti.
Se ci sono abbastanza AGNELLI rimasti in modo che un altro scagnozzo possa essere aggiunto come il più anziano
pur obbedendo alle altre regole, devi sempre aggiungere e pagare quello scagnozzo.

Nota che potresti non essere in grado di distribuire tutti gli AGNELLI.
Un solo AGNELLO non può essere suddiviso. Questo è,
tutti gli scagnozzi devono ottenere un numero intero positivo di LAMB.

Scrivi una funzione chiamata soluzione (total_lambs),
dove total_lambs è il numero intero di LAMB nella dispensa che stai cercando di dividere.
Dovrebbe restituire un numero intero
che rappresenta la differenza tra il numero minimo e massimo di scagnozzi
chi può condividere gli AGNELLI
(cioè essere il più generosi possibile con coloro che paghi e il più avari possibile, rispettivamente)
pur obbedendo a tutte le regole di cui sopra per evitare una rivolta.
Ad esempio, se avessi 10 AGNELLI e fossi il più generoso possibile,
potresti pagare solo 3 scagnozzi (1, 2 e 4 LAMB, in ordine di anzianità crescente),
mentre se tu fossi il più avaro possibile,
potresti pagare 4 scagnozzi (1, 1, 2 e 3 AGNELLI).
Pertanto, la soluzione (10) dovrebbe restituire 4-3 = 1.

Per mantenere le cose interessanti, il comandante Lambda varia le dimensioni dei pagamenti Lucky LAMB.
Puoi aspettarti che total_lambs sia sempre un numero intero positivo inferiore a 1 miliardo (10 ^ 9).
"""
def solution(lambs):
    avaro = [1]
    generoso = [1]
    cont=0
    if lambs == 1:
        cont = 1
    elif lambs == 2:
        avaro.append(1)
        generoso.append(1)
        cont = 1
      
    else:
        avaro.append(1)
        generoso.append(2)
        cont = 0 
    while cont == 0:
        if sum(avaro)+(avaro[-1]+ avaro[-2]) < lambs:
            avaro.append(avaro[-1]+ avaro[-2])
        else:
            print("esco dai primo while e La somma dei numeri in Avaro e :", sum(avaro))
            cont = 1
    cont = 0
    while cont==0:
        if sum(generoso)+generoso[-1]*2 < lambs :
            generoso.append(generoso[-1]*2)
        else:
            print("esco dai secondo while e La somma dei numeri in Generoso e :", sum(generoso))
            cont = 1
        print(avaro)
        print(generoso)
        

    risultato = len(avaro)-len(generoso)
    return risultato
print("risultato di 143: ", solution(1))
#print("risultato 10: ", solution(10))
