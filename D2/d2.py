#Question 1
import math
def patinage(e,tm):
    if e >= 30 and tm <= -10:
        p = True 
    else:
        p=False
    return p
'''
(float, float) -> bool
e = Épaiseur de la glace
tm = Température moyenne
p = patinage
'''

print('Température moyenne des dix dernier jours')
tm = float(input())

print('Épaisseur de la glace (cm)')
e = float(input())

print(patinage(e,tm))









#Question 2

'''
float -> str
x = note obtenu, sur 100
n = note en lettre
'''
def alphaNote(x):
    if 90<=x<=100:
        n = str('A+')
    elif 85<=x<=89:
        n = str('A')
    elif 80<=x<=84:
        n = str('A-')
    elif 75<=x<=79:
        n = str('B+')
    elif 70<=x<=74:
        n = str('B')
    elif 65<=x<=69:
        n =str('C+')
    elif 60<=x<=64:
        n = str('C')
    elif 55<=x<=59:
        n = str('D+')
    elif 50<=x<=54:
        n = str('D')
    elif 40<=x<=49:
        n=str('E')
    elif 0<=x<=39:
        n=str('F')
    return n

print('Quelle est votre note')
x = float(input())
print(alphaNote(x))









#Question 3

'''
float -> str, str
x = note obtenue
n = vérificateur de note
'''

def alphaNoteVerif(x):
   
    if alphaNote(x) == 'E': 
       print('Échoué')
    elif alphaNote(x)=='F':
        print('Échoué')
    else:
        print('Réussi')


print('Quelle est votre note')
x = float(input())

while 0 > x:
    print('Veullez entre votre note (nombre réel entre 0 et 100)')
    x = float(input())

while x > 100:
    print('Veullez entre votre note (nombre réel entre 0 et 100)')
    x = float(input())

print(alphaNoteVerif(x))

print(alphaNote(x))

#Question 4

print('Quelle valeur donné vous a n?')
n = int(input())
b = 1

'''
int -> int
n = la valeur qui cloture la fonction
b = compteur
'''
while n <= 1:
    print('le nombre doit être plus grand que 1, veulliez entré un nouveau nombre')
    n = int(input())



def boucles(n):
    for b in range (1,n,2):
        print(b)
        x = ' '
    return x
print(boucles(n))









#question 5

print('quelle nombre entier vouler vous factiriser')
n = int(input())

while n<=1:
    print("le nombre que vous avez choisi n'a pa de facteur sauf 1 et lui même, ou est négatif, veuillez entré un nouveau nombre positif")
    n = int(input())

'''
int -> int, bool
n = nombre qui sera factoriser
div = diviseur, il commence a 2 puisque diviser par 1 'est pas requis dnas ce programme
res = résultat de la division de n par div 
somme = la somme de chaque res
'''    
    
def facteurDeN(n):
    div = 2
    somme = 0


    while div < n:
        
        res = n/div
        
        if n%div == 0:
            print(int(res))
            somme = res + somme
            
        div = div + 1
    somme = int(somme)

    print(n >= somme)
    return somme

print(facteurDeN(n))









#question 6

print('Ce programme détermine si un nombre est un carré parfait, veulliez entré le nombre que vous voulez tester')
x = float(input())

while x < 0:
    print('Vous avez entré un nombre négatif, veulliez entré un nombre positif') 

def carreParfait(x):
    '''
    float->bool 
    x = nombre qui pourrais etre un carré parfait
    z = racine carré de x
    m est un test par rapport a la racine du nombre choisi.

        Un nombre qui est un carré parfait sera divisible par sa racine carré puisque
        la racine carré sera un facteur du nombre.
        Dans le cas inverse, la racine carré est un nombre irrationnel. Ce type de nombre
        ne peut pas être le facteur d'un n'autre nombre puisqu'il ne peut pas exprimé
        comme un ratio
    '''
    
    z = math.sqrt(x)
    m = x%z
    if m == 0:
        m = True
    else:
        m = False
    return m
print(carreParfait(x))
    

