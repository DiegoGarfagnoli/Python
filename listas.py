
# Listas, 2 es el elemento 0. Lista que contiene una lista
l = [2, "tres", False, ["uno", "diez"], ["uno", "dos"], ["dos", "tres"]]
lista = [["Diego", "Garfagnoli"], ["Sabrina", "Depeller"]]
lista_banderas = [False, False, False, False, False, True]

l2 = l[1]

print l2

l2 = l[3][0]

print l2

l[3][1] = "nueve"
l2 = l[3][1]

print l2

if l[2] == True:
    print "Verdadero"
    l[2] = False
else:
    print "Falso"
    l[2] = True

if l[2] == True:
    print "Verdadero"
    l[2] = False
else:
    print "Falso"
    l[2] = True

if lista_banderas[5] == True:
    print lista[0][0] + " " + lista[0][1]
else: print lista[1][1] + ", " + lista[1][0]
if lista_banderas[2] == True:
    print lista[0][0] + " " + lista[0][1]
else: print lista[1][1] + ", " + lista[1][0]

l3 = l[3:4]
print l3

l3 = l[0::2]
print l
print l3
l3 = l[1::2]
print l3
l3 = l[-1]
print l3
# tuplas



# diccionarios
