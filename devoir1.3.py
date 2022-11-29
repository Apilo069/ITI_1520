#Ce programme utilise des valeur déja donné pour créé une bibliographie

def bibformat(Na,Ap,Nl,V,Me):
    Bi=(Na, (Ap), Nl, V, Me,)
    return Bi
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
