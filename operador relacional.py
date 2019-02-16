# operadores relacionales
    #operdores relacionales NUMERICOS
v = 4
c = 5
r = v == c
print r

r = v != c
print r

r = v < c
print r

r = v >= c
print r

    # operadores relacionales CADENAS
v = 'Hola'
c = 'Adios'
r = c <= v
print r

v = 'Hola'
c = 'Z'
r = c == v
print r

v = 'Hola'
c = 'X'
r = c <> v
print r

    # Usar operadores relacionales con Listas, etc
v = ['Hola', 3, 4]
c = ['Hola', 3, 5]

r = v == c # compara LISTAS completas!!
print r
r = v != c # compara LISTAS completas!!
print r


