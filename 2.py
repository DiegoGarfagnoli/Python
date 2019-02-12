def maximo(x,y,z):
    if x > z and x > y:
        return 'x', x
    if y > z and y > x:
        return 'y', y
    if z > y and z > x:
        return 'z', z
    if x == y and x > z:
        return 'x' , x, 'y', y
    if x == z and x > y:
        return 'x',x, 'z', z
    if y == z and y > x:
        return 'y', y, 'z', z
    if y == x == z:
        return 'x , y ,z son iguales. Valor: ' ,x


        
def histograma(a):
    return '*'*a


print maximo(3,3,3)
c = 1
d = 1
e = 2
while c < 80:
    c = c + 2
    if c / 2 == 4:
        c = c +1
    if c / 5 == 2:
        d = 3 + d
    if c / 6 > 2:
        e,c = e-1, (c+d-e)/3
    if d < 12:
        d = d  + 2

    if d < 40 and d > 20:
        c = c - 3
        d = d - 2
        e = e + 1
        
        
        
    print histograma(c)
