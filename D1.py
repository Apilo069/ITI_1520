#cette fonction calcule la durée d'un voyage basé sur la distance et la vitesse
def tempsVoyage(d,v):
    th=d/v
    tm=th * 60
    return tm

'''
float->float

la variable t(m) représente le temps, en minute
la variable t(h) représente le temps, en heure
la variable d représente la distance, en kilometre
la variable v représente la vitesse, en kilometre par heure

Cette fonction utilise la distance et la vitesse pour calculé le montant de temps que parcourir cette distance prenrda
'''

print('distance a parcourir, en kilometre (k)')
d = float(input())

print('vitesse, en kilometre par heure (km/h)')
v = float(input())

print('Ce voyage durera', tempsVoyage(d,v), 'minute(s)')






#Cette fonction calcule la note finale dans un cours, basé sur 5 critère
def noteFinale(lab,d,qz,ep,ef):
    notef = lab*0.10 + d*0.25 + qz*0.05 + ep*0.20 + ef*0.40
    return notef
'''
float->float

notef = note finale
lab = moyenne dans les laboratoire
d = note moyenne dans devoir
qz = note moyenne dans quiz
ep = note dans examen partiel
ef = note dans examen finale
'''



print('note moyenne pour les laboratoire')
lab=float(input())

print('note moyenne pour les devoirs')
d=float(input())

print('note moyenne pour les quiz')
qz=float(input())

print('note pour examen partiel')
ep=float(input())

print('note pour examen finale')
ef=float(input())

print('votre note finale est', noteFinale(lab,d,qz,ep,ef))




def bibformat(Na,Ap,Nl,V,Me):
    Bi=(Na, (Ap), Nl, V, Me,)
    print(Bi)
'''
Na=Nom de auteur
Ap= anné de publication
Nl=Nom du livre
V=ville
Me=Maison edition
'''


Na ='Bob Woodward'
V = 'New York'
Ap = '1999'
Nl= 'Shadow: Five Presidents and the Legacy of Watergate'
Me = 'Simon & Schuster'

print(bibformat(Na,Ap,Nl,V,Me))

#Ce programme créé une bibliographie basé sur des entré du clavier

print('Nom de auteur')
Na=str(input())

print('Nom du livre')
Nl=str(input())

print('Nom de la ville de publication')
V=str(input())

print('Année de publication')
Ap=str(input())

print('Nom de la maison de publication')
Me=str(input())

print(bibformat(Na,Ap,Nl,V,Me))

