
# cadenas
  # simple con salto de linea
cads = 'texto entre \n comilla simple'
  # doble con tabulacion
cadd = "Texto entre \t comillas dobles"
  # triple comilla doble
cadt = """
linea 1
linea 2
....
....
....
linea n
"""
  # Repeticion y concatenacion
cadrep = cadd * 3
cadconc = cads + cadd + cadt


print type (cads), cads
print type (cadd), cadd
print type (cadt), cadt
print type (cadrep), cadrep
print type (cadconc), cadconc  

# logicos la primer letra va en mayus
bT = True
bF = False
bAnd = bT and bF
bOr  = bT or bF
bNot = not bT

print bAnd, bOr, bNot
