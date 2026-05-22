class Nodo:
    def __init__(self, dato=0, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
        # print(f'Nodo construido con {self.dato}')

    def __del__(self):
            # print(f'Nodo destruido con {self.dato}')
            pass

    def __str__(self):
        estado = f'| {self.dato} |'
        if self.siguiente != None:
            estado += ' -> '
        return estado

class LSE:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def __del__(self):
         self.liberaMemoria()

    def insertaAlUltimo(self, dato):
         if self.estaVacia():
              self.primero = Nodo(dato, None)
              self.ultimo = self.primero
         else:
              self.ultimo.siguiente = Nodo(dato, None)
              self.ultimo = self.ultimo.siguiente

    def eliminaAlPrimero(self):
        d = None
        if not self.estaVacia():
            d = self.primero.dato
            if self.primero==self.ultimo:
                del self.primero
                self.primero = None
                self.ultimo = None
            else:
                aux = self.primero
                self.primero = self.primero.siguiente
                del aux
        return d

    def estaVacia(self):
        return self.primero==None and self.ultimo==None
    
    def liberaMemoria(self):
        while not self.estaVacia():
            #   print(f'Se elimina {self.eliminaAlPrimero()}')
            self.eliminaAlPrimero()

    def muestraLSE(self):
        aux = self.primero
        while aux != None:
            print(aux, end='')
            aux = aux.siguiente

    def busca(self, dato):
        aux = self.primero
        while aux != None:
            if dato == aux.dato:
                return True
            aux = aux.siguiente
        return False

    def eliminaAlUltimo(self):
        d = None
        if self.primero==self.ultimo and self.primero!=None:
            d = self.ultimo.dato
            del self.ultimo
            self.primero = None
            self.ultimo = None
        else:
            d = self.ultimo.dato
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente
            del self.ultimo
            aux.siguiente = None
            self.ultimo = aux
        return d

    def elimina(self, dato):
        if self.estaVacia():
            return False
        elif dato == self.primero.dato:
            self.eliminaAlPrimero()
            return True
        elif dato==self.ultimo.dato:
            self.eliminaAlUltimo()
            return True
        else:
            aux1 = self.primero
            aux2 = self.primero.siguiente
            while aux2!=self.ultimo and dato!=aux2.dato:
                aux1 = aux1.siguiente
                aux2 = aux2.siguiente

            if aux2==self.ultimo:
                return False
            else:
                aux1.siguiente = aux2.siguiente
                del aux2
                return True
            
    def insertaAlPrimero(self, dato):
        if self.estaVacia():
            self.primero = Nodo(dato, None)
            self.ultimo = self.primero
        else:
            self.primero = Nodo(dato, self.primero)

    def insertaOrdenadamente(self, dato):
        if self.estaVacia() or dato <= self.primero.dato:
            self.insertaAlPrimero(dato)
        elif dato >= self.ultimo.dato:
            self.insertaAlUltimo(dato)
        else:
            aux1 = self.primero
            aux2 = self.primero.siguiente
            while dato > aux2.dato:
                aux1 = aux1.siguiente
                aux2 = aux2.siguiente
            aux1.siguiente = Nodo(dato, aux2)

    def cuentaNodos(self):
        n = 0
        aux = self.primero
        while aux!=None:
            n += 1                          # Se cuenta cada nodo
            aux = aux.siguiente             # Se desplaza una referencia auxiliar, nodo por nodo
        return n
