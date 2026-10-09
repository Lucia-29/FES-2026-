###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí

print("Lucía Gayán Milián \n Rubí")

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

### Completa aquí

print("tipus a: ", type(a))
print(", tipus b: ", type(b))
print(", tipus c: ", type(c))
print(", tipus d: ", type (d))
print(", tipus e: ", type(e))

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí

cadena = 12345
nombre_enter =int(cadena)
nombre_decimal = float(cadena)

print("nombre enter: ", nombre_enter)
print("nombre decimal: ", nombre_decimal)

n_original = 3.99
n_enter = int(n_original)

print("Nombre original decimal: ", n_original)
print("Nombre decimal transformat en enter: ", n_enter)

print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 38 anys i faig 1.75 metres"
#name = "Marc"
#age = 38

### Completa aquí
nom = "Lucía"
edat = 20
alçada = 1.56

print(f"Hola, em dic {nom}, tinc {edat} anys i faig {alçada} metres")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

numero_pi = round(PI)
n_res = numero_pi / 2

print("El resultat es: ", n_res)

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí

temp_C = float(input("Introdueix una temperatura en celsius: "))
temp_F = (temp_C * 9/5) + 32

print (f"La temperatura en celsius es de {temp_C}º i {temp_F} en Fahrenheit.")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí

compte = float(input("Introdueix el total del compte: "))
propina = float(imput("Introdueix el percentatge de propina que vols deixar: "))

propina_total = propina/100 * compte
total = compte + propina_total

print(f"La propina será de {propina_total}€. En total haura de pagar: {total}€.")

print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí

contrasenya = input("introdueix una contrasenya: ")
if len (contrasenya) < 8:
    print("Contrasenya no vàlida.")
    
else:
    
        print ("contrasenya valida")
    