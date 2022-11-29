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
