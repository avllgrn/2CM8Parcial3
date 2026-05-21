from Clases.LSE import LSE
from subprocess import run
from random import randrange

if __name__=='__main__':
    run('cls', shell=True)

    L = LSE()

    n = randrange( 10 )
    for i in range(n):
        x = randrange( 100 )
        print(f' Se inserta {x} al último')
        L.insertaAlUltimo( x )
        L.muestraLSE()
    print('\n\n')

    run('pause', shell=True)
    print('\n\n')
    
    while not L.estaVacia():
        print(f' Se elimina {L.eliminaAlPrimero()}, el primero ')
        L.muestraLSE()
    print('\n\n')

    run('pause', shell=True)
    run('cls', shell=True)

    n = randrange( 10 )
    for i in range(n):
        x = randrange( 100 )
        print(f' Se inserta {x} como primero')
        L.insertaAlPrimero( x )
        L.muestraLSE()
    print('\n\n')

    run('pause', shell=True)
    print('\n\n')
    
    while not L.estaVacia():
        print(f' Se elimina {L.eliminaAlUltimo()}, el último ')
        L.muestraLSE()
    print('\n\n')

    run('pause', shell=True)
    run('cls', shell=True)

    n = randrange( 10 )
    for i in range(n):
        x = randrange( 100 )
        # print(f' Se inserta {x} como primero')
        L.insertaAlPrimero( x )
    L.muestraLSE()
    print('\n\n')

    x = int(input('Qué dato buscas? '))
    if L.busca(x):
        print(f'{x} ESTÁ en la lista')
    else:
        print(f'{x} NO está en la lista')
    print('\n\n')
        
    x = int(input('Qué dato eliminas? '))
    if L.elimina(x):
        print(f'{x} ELIMINADO de la lista')
    else:
        print(f'{x} NO está en la lista')
    print('\n\n')
        
    L.muestraLSE()
    print('\n\n')
    L.liberaMemoria()

    run('pause', shell=True)
    run('cls', shell=True)

    n = randrange( 10 )
    for i in range(n):
        x = randrange( 100 )
        print(f' Se inserta {x}')
        L.insertaOrdenadamente( x )
        L.muestraLSE()
    print('\n\n')

