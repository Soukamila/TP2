def add (n,no):
    
    return n+no

def sous(a,c):
    res=a-c
    return res

def multi (b,m):
    
    return b*m

def divi (c,m):
    return c/m

def factorielle(nombre):
    if nombre < 0:
        return -1
    else:
        resultat = 1
        for i in range(1, nombre + 1):
            resultat *= i
        return resultat


def exposant(n,e):
    resu=1
    while (e >0):
        resu*=n
        e-=1
    return resu

def racine_carree(nombre):
    if nombre < 0:
        return "La racine carrée n'est pas définie pour les nombres négatifs"
    
    if nombre == 0:
        return 0

    estimation = nombre / 2
    for _ in range(100):
        estimation = 0.5 * (estimation + nombre / estimation)

    return estimation



