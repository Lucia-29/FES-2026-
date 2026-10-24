###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
print("EXERCICI 1: \n")
num1 = float(input("Introdueix un nombre: \n"))
num2 = float(input("Introdueix un altre nombre: \n"))

if num1 < num2:
    print(f"{num2} és més gran que {num1} \n")
else:
    print(f"{num1} és més gran que {num2} \n")
 


# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

print("\n EXERCICI 2: \n")
num1 = float(input("Introdueix el primer nombre: \n"))
num2 = float(input("Introdueix el segón nombre: \n"))
operacio = input("Introdueix l'operació que vols fer ( +, -, *, /): \n")

if operacio == '+':
    print(f"{num1} + {num2} = {num1+num2} \n")
    
elif operacio == '-':
   print(f"{num1} - {num2} = {num1-num2} \n")
   
elif operacio == '*':
    print(f"{num1} * {num2} = {num1*num2} \n")
    
elif operacio == '/':
    if num2 == 0:
        print("Error; no es pot dividir per 0. \n")
    else:
        print(f"{num1} / {num2} = {num1/num2} \n")
else:
    print("ERROR; Operació innexistent.\n")



# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

print("\nEXERCICI 3: \n")
any = int(input("introdueix l'any: \n"))
if (any %4 == 0 and any%100 == 0) or any% 400 == 0:
    print (f"l'any {any} es de trespas.\n")
else:
    print(f"l'any {any} no es un any de trespas.\n")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)
print ("\n EXERCICI 4: \n")
edat = int(input("Introdueix la teva edat: \n"))
if edat < 0: 
    print("ERROR: edat innexistent.\n")
elif edat <= 2:
    print("És un nadó.\n")
elif edat <= 12:
    print("És un infant.\n")
elif edat <= 17:
    print("És un adolescent.\n")
elif edat <= 64:
    print ("És un adult.\n")
else:
    print ("És una persona gran.\n")

# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

print("\n EXERCICI 5: \n")

senyal = float(input("Introdueix el nivell de senyal rebut (RSSI) en dBm: \n"))
if -50 <= senyal:
    print("Nivell de cobertura excl·lent. \n")
elif -67 <= senyal < -50:
    print("Nivell de cobertura bona. \n")
elif -75 <= senyal < -67:
    print("Nivell de cobertura feble. \n")
else:
    print ("Nivel e cobertura molt feble. \n")


# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

print ("\n EXERCICI 6: \n")
potencia_optica = float(input("Introdueix la potència òptica en dbm: \n"))
if potencia_optica < -27:
    print("El nivell és massa baix. \n")
elif potencia_optica > -8:
    print("El nivell és massa alt. \n")
else:
    print("El nivell és acceptable. \n")

# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

print("\n EXERCICI 7\n")
consum_dades = float(input("Introdueix el consum de dades en GB de la línia mòbil: \n"))
if consum_dades <= 20:
    print("El consum és dins del límit.")
else:
    dades_extra = consum_dades - 20
    print(f"El consum es major al límit per {dades_extra} GB")

# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

print("\n EXERCICI 8 \n")

indicador_optic = bool (input("Introdueix 1 si l'indicador LOS està encès i 0 si està apagat: \n"))
indicador_router = bool(input("Introdueix 1 si l'indicador d'internet està encès i 0 si està apagat: \n"))

if indicador_optic and indicador_router:
    print ("La connexió sembla funcionar correctament. \n")
elif indicador_optic:
    print ("S'ha de comprovar el servei del proveïdor. \n")
elif indicador_router:
    print("s'ha de revisar el cable de fibra. \n")
else:
    print("S'ha de revidar el cable de fibra i comprovar el servei del proveïdor.\n")

# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

print("\n EXERCICI 9 \n")

bateria = float(input("Introdueix el percentatge de bateria disponible al SAI\n"))

if bateria < 20:
    print("El nivell és crític. \n")
elif 20 <= bateria <= 49:
    print("Nivel baix. \n")
elif 100 >= bateria >= 50:
    print("batería suficient. \n")
else:
    print("Valor fora del reang. \n")

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

print("\n EXERCICI 10 \n")
latencia = float (input("Introdueix la làtencia en mil·lisegons: \n"))
paquets_perduts = float(input("Introdueix el percentatge de paquets perduts: \n"))
if latencia < 0 or 0 > paquets_perduts > 100:
    print ("Valors incorrectes \n")
elif latencia <= 30 and paquets_perduts <= 1:
    print ("connexió excel·lent. \n")
elif latencia <= 80 and paquets_perduts <= 3:
    print ("connexió bona. \n")
elif latencia <= 150 and paquets_perduts <= 5:
    print("Connexió acceptable. \n")
else:
    print("Connexió deficient. \n")


 

# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

print("\n EXERCICI 11 \n")
pla = input("Introdueix el tipus de pla de dades (basic o plus): \n")
consum_mensual = float(("Introdueix el consum mensual: \n"))
extra = 0
if consum_mensual < 0 or (pla != ('bàsic') or pla != ('plus')):
    print("Error: dades mal introduides.")
elif pla == 'basic':
    
    if consum_mensual > 10:
        extra = consum_mensual -10

    preu = 10 + extra*1,5
else:
    if consum_mensual > 30:
        extra = consum_mensual - 30

    preu = 20 + extra * 0.75

print (f"El cost total es de {preu}€ \n")

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

print("\n EXERCICI 12 \n")
compte = bool (input("estat del compte: \n"))
contrasenya = bool(input(" contrasenya: \n"))

if compte and contrasenya:
    codi = bool(input("Introdueix si el codi es correcte: \n"))
    if not codi:
        print("el codi falla. \n")
    else:
        print("Accés permés: \n")
elif not compte:
    print("Accés denegat, campte no activat. \n")
elif not contrasenya:
    print("Contrasenya no valida. \n")


# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

print("\n EXERCICI 13 \n")

router = bool (input("Introdueix si el router està ences: \n"))
indicador_LOS = bool(input("Introduiex si l'indicador LOS està encès: \n "))
indicador_internet = bool(input("Indica si l'indicador d'internet està encès: \n"))

if not router:
    print("Encen el router. \n")
elif not indicador_LOS: 
    print("Cal revisar el cable de fibra. \n")
elif not indicador_internet:
    print ("Cal contactar amb el proveïdor. \n")
else:
    print("La connexió funciona correctament. \n")

# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.

print("\n EXERCICI 14 \n")
incidencia = bool(input("La incidencia afecta un servei crític? 1->si, 0 -> no: \n"))
n_usuaris = int(input("Introdueix el nombre d'usuaris afectats: \n"))
alternativa = bool(input("Hi ha una alte alternativa 1-> si 0 ->no: \n"))
if n_usuaris < 0:
    print("nombre d'usuaris innexistents. \n")
elif incidencia and not alternativa or n_usuaris >= 50 and not alternativa:
    print("Prioritat crítica.\n")
elif n_usuaris >= 10 or incidencia:
    print("Prioritat alta. \n")
else:
    print("Prioritat baixa. \n")
