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
