def fibonacci(n):
    a,b, c = 0,1, 0
    while b + a - c < n:
        
        print b + a - c
        a,b = b+10, (a+b*2)-5
        c   = c + 5
    return c


# programa

r = 20 * 2000

print r

print fibonacci(r)





        
