import random

def juegaUser():
    choice=input('PIEDRA, PAPEL O TIJERA?: ')
    if choice.lower() == 'piedra':
        return 0
    if choice.lower() == 'tijera':
        return 1
    if choice.lower() == 'papel':
        return 2

def juegaAI():
    random.seed()
    return random.randint(0,2)
    
cantPartidas=input("Al mejor de cuanto lo jugamos?: ")
cantPartidas=int(cantPartidas)
ptos={'User':0,'AI':0}
elementos=['Piedra','Tijera','Papel']

while ptos['User'] + ptos['AI'] < cantPartidas:
    indexU=juegaUser()
    indexA=juegaAI()
    if (elementos[indexU] == elementos[indexA]):
        print("Empate!")
        continue
    if (elementos[indexU-1]==elementos[indexA]): #(1)
        print("%s vence a %s: Punto de AI!" %(elementos[indexA], elementos[indexU]))
        ptos['AI']+=1
    elif (elementos[indexA-1]==elementos[indexU]):
        print("%s vence a %s: Punto del User!"%(elementos[indexU], elementos[indexA]))
        ptos['User']+=1

if ptos['User'] > ptos['AI']:
    print('Ganó el user con %d puntos'%ptos['User'])
else:
    print('Gano AI con %d puntos' %ptos['AI'])

# Aprovecho que en Python cuando a un array le doy subindice -1 va al ultimo elemento --> si user elige roca y AI papel 0 -1 = -1 nos
# lleva al último elemento que es papel == jugada AI por ende gana AI
