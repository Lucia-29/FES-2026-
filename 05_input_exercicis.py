###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###



# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

nom_tecnic = input("Introdueix el nom del tecnic: ")
nom_xarxa = input("Introdueix el nom de la xarxa: ")

print(f"Tècnic: {nom_tecnic}; xarxa en instalació: {nom_xarxa}")


# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

long_enllaç = float(input("Longitud de l'enllaç en quilòmetres: "))
velocitat_enllaç = float(input("velocitat de transmissió en Gbps: "))
velocitat_segons = 8 / velocitat_enllaç

print(f"L'enllaç te {long_enllaç} kilometres. Necessita {velocitat_segons} segons per rasnmetre 1 GB.")


# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

h_feina = float(input("nombre d'hores de feina: "))
preu_h = float(input("preu per hora: "))
preu_m = float(input("preu material: "))

cost_total = preu_h*h_feina + preu_m

print(f"El cost total de l'instalació es de {cost_total}€")