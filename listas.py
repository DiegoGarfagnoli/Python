
# Listas, 2 es el elemento 0. Lista que contiene una lista
# agregar elementos, eliminar elementos
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

l.append('Marta Martinez')

l3 = l
print l3

  #eliminar elementos.
      # eliminar el ultimo elemento (tendria que desaparecer Marta Martinez)
      # usa LISTA.pop()
l.pop()
print l
      # eliminar elemento por indice usa LIStA.pop(0) donde 0 va el indice del elemento
l.pop(0)
print l
      # eliminar elemento por valor (usa LISTA.remove)
l.remove(["uno", "dos"])
print l


# tuplas, son parecidas a las listas
#  las tuplas no puedo agregarles elementos
# no puedo cambiar elementos

t = (1, True, "Hola")
print t
print type(t)

print t[1]


# diccionarios / CLAVES ASOCIATIVAS
#los diccionarios no son secuencias
d = {'Clave1':[1,2,3],
     'Clave2':[2,2,2],
     'Clave3':[3,0,0]}

print d['Clave1']
