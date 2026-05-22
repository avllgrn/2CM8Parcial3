from Clases.LSE import LSE
from subprocess import run
from random import randrange

def cuentaNodos(L):
    n = 0
    aux = L.primero
    while aux!=None:
        n += 1                          # Se cuenta cada nodo
        aux = aux.siguiente             # Se desplaza una referencia auxiliar, nodo por nodo
    return n

if __name__=='__main__':
    run('cls', shell=True)

    L = LSE()

    for i in range ( randrange(20) ):   # No se sabe cuantos nodos se insertaran (maximo 20)
        L.insertaAlUltimo( randrange(100) )
    L.muestraLSE()
    print('\n\n')

    n = cuentaNodos( L )
    print(f'En la lista, hay {n} nodo(s)')
