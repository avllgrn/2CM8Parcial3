from subprocess import run
from random import randrange

if __name__ == '__main__':
    run('cls', shell=True)

    V = [randrange(100) for i in range(5)]
    print(V)

    I = iter(V)         # Se instancia un iterador a un objeto iterable (lista)

    print( next(I) )
    print( next(I) )
    print( next(I) )
    print( next(I) )
    print( next(I) )
    print()
    # print( next(I) )  # Este ya NO DEBE ejecutarse 
                        # porque previamente el iterador alcanzó 
                        # el último elemento

    for dato in V:
        print(dato)
    print()

    I = iter(V)         # Debe instanciarse un nuevo iterador
    for dato in I:      # porque previamente el iterador alcanzó
        print(dato)     # el último elemento
    print()

    I = iter(V)         # Debe instanciarse un nuevo iterador
    try:                # porque previamente el iterador alcanzó
        while True:     # el último elemento
            print( next(I) )
    except StopIteration:
        pass
