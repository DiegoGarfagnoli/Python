# -*- coding: cp1252 -*-
# practica de operadores, listas, tuplas, diccionarios
# tipos de datos

# ejercicio 1. Generar una lista llamada lista_equipos con 10 elementos,
#              cada elemento siendo un equipo de futbol.
# ejercicio 2. Agregar 2 elementos al final de la lista lista_equipos.
#              agregar un elemento en la posicion 2. mostrar lista.
# ejercicio 3. Quitar el quinto elemento de la lista lista_equipos.
#              Mostrar lista.
# ejercicio 4. Generar una tupla tupla_numeros que contenga 3 numeros
#              diferentes que esten comprendidos entre el 1 y el 11.
#              Mostrar tupla, mostrar los equipos que se correspondan con
#              los valores de la tupla.
# ejercicio 5. generar un diccionario llamado diccionario_numeros,
#              conteniendo 5 claves (1, 2, 3, 4, 5) y para cada clave
#              un valor numerico INT, teniendo en cuenta que la clave 1 debe
#              ser diferente a 0.
#              Mostrar diccionario.
# ejercicio 6. Multiplicar las claves del diccionario diccionario_numeros
#              2 y 3 dividiendo (INT) el resultado ANT con el primer registro de la tupla
#              tupla_numeros. Division (DEC) entre la clave 4 del diccionario
#              diccionario_numeros y el segundo registro de la tupla
#              tupla_numeros. Division
#              Modulo de la division decimal entre la clave 5  diccionario_numeros y el
#              registro de la posición 3 de la tupla_numeros.
# ejercicio 7. Generar una lista, lista_cadenas con 4 cadenas.
#              Concatenar los cuatro valores en una cadena var_cadena, mostrando el resultado.
#              Mostrar los valores 2 y 4 de la lista lista_cadenas.
#              Mostrar los valores 1 y 3 de la lista lista_cadenas.
#              Agregar 4 registros que sean cadenas a la lista lista_cadenas. Mostrar la concatenacion
#              de los registros 2, 4, 6, 8 y mostrar la concatenacion de los registros 1, 3, 6, 7.
# ejercicio 8. Generar una lista de 7 numeros hexadecimales. Mostrar la lista.


#1
Lista_equipos = ["Boca", "River", "Colon", "Union", "Central", "Newells", "Racing", "Independiente", "Huracan", "Independiente"]
#2
Lista_equipos.append("Defensa y J.")
Lista_equipos.append("Atl. Tucuman")
Lista_equipos.insert(1, "Lanus")
print Lista_equipos
#3
Lista_equipos.pop(4)
print Lista_equipos
#4
tupla_numeros = (1, 2, 4)
print tupla_numeros
print Lista_equipos[tupla_numeros[0] - 1], Lista_equipos[tupla_numeros[1] - 1], Lista_equipos[tupla_numeros[2] - 1]
#5
diccionario_numeros = {1:20,
                       2:21,
                       3:5,
                       4:12,
                       5:0}
print diccionario_numeros
#6
resultado = ( diccionario_numeros[2] * diccionario_numeros[3] ) / tupla_numeros[0]
print resultado
resultado = float(diccionario_numeros[4]) / tupla_numeros[1]
print resultado
resultado = diccionario_numeros[5] % tupla_numeros[2]
print resultado
#7
lista_cadenas = ["Cadena1", "Cadena2", "Cadena3", "Cadena4"]
i = 0
var_cadena = ""
while i < 4:
    var_cadena = var_cadena + lista_cadenas[i] 
    i = i + 1
print var_cadena
print lista_cadenas[1:4:2]
print lista_cadenas[0:4:2]
lista_cadenas.append("Boca1")
lista_cadenas.append("Boca2")
lista_cadenas.append("Boca3")
lista_cadenas.append("Boca4")
print lista_cadenas[1:10:2]
i = 0
var_cadena = ""
while i < 8:
    if i == 0 or i == 2 or i == 5 or i == 6:
        var_cadena = var_cadena + lista_cadenas[i]
    i = i + 1

print var_cadena
#8
var_hexa = 0
i = 0
lista_hexadecimal = [var_hexa]
while i < 7:
    i = i + 1
    var_hexa = var_hexa + 15
    if i == 1:
        lista_hexadecimal[0] = var_hexa
    else:
        
        lista_hexadecimal.append (var_hexa)
    print hex(lista_hexadecimal[i - 1]), hex(lista_hexadecimal[i - 1] / 2) , hex(lista_hexadecimal[i - 1] * (lista_hexadecimal[i - 1]) / 2)
    
    print hash(lista_hexadecimal[i - 1])
print max(lista_hexadecimal), min(lista_hexadecimal)
