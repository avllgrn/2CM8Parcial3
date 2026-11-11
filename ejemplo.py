from subprocess import run
from random import randrange

if __name__ == '__main__':
    run('cls', shell=True)

    L = [randrange(100) for i in range(5)]
    print(L)

    Iterador = iter(L)         # Se instancia un iterador a un objeto iterable (lista)
    for dato in Iterador:
        print(dato)
    print()

    T = tuple([randrange(100) for i in range(5)])
    print(T)

    Iterador = iter(T)         # Se instancia un iterador a un objeto iterable (tupla)
    for dato in Iterador:
        print(dato)
    print()

    C = set([randrange(100) for i in range(5)])
    print(C)

    Iterador = iter(C)         # Se instancia un iterador a un objeto iterable (conjunto)
    for dato in Iterador:
        print(dato)
    print()

    D = dict.fromkeys(L, None)
    print(D)

    Iterador = iter(D)         # Se instancia un iterador a un objeto iterable (diccionario)
    for dato in Iterador:
        print(dato)
    print()
