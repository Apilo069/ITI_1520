#Ce programme créé une bibliographie basé sur des entré du clavier


def bibformat(Na,Ap,Nl, V, Mp):
    Bi= (Na, (Ap), Nl, v, Mp)
    print(Bi)
  


print('Nom de auteur')
Na=str(input())

print('Nom du livre')
Nl=str(input())

print('Nom de la ville de publication')
v=str(input())

print('Année de publication')
Ap=str(input())

print('Nom de la maison de publication')
Mp=str(input())

print(bibformat(Na, (Ap), Nl, v,Mp))


