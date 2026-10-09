###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom_encaminador = "Encaminador uni"
ubicacio = "secretaria"
ports = 3
encaminador_ences = True

print(f"Encaminador: {nom_encaminador}; ubicació: {ubicacio};"
      f"Ports: {ports}; engegat: {encaminador_ences}")



# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

GB_inclosos = 16
GB_Consumits = 6.5

GB_restants = GB_inclosos - GB_Consumits

print(f"Queden: {GB_restants} GB")

GB_Consumits = 12
GB_restants = GB_inclosos - GB_Consumits
print(f"Queden: {GB_restants} GB")