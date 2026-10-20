class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # TODO 1: agrega el nodo al final sin perder los anteriores
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agrega el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: devuelve y elimina el último elemento;
        # controla el caso de pila vacía
        if len(self.items) == 0:
            return "Pila vacía"
        return self.items.pop()


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: devuelve y elimina el primer elemento;
        # controla el caso de cola vacía
        if len(self.items) == 0:
            return "Cola vacía"
        return self.items.pop(0)


# Agrega tus pruebas debajo. Usa los datos asignados en tu versión.
if __name__ == "__main__":
    # --- DATOS DE PRUEBA: M01: Alimento; M02: Correa; M03: Cama ---

    print("=== 1. MOSTRAR LISTA ENLAZADA ===")
    lista = ListaEnlazada()
    lista.agregar("M01", "Alimento")
    lista.agregar("M02", "Correa")
    lista.agregar("M03", "Cama")
    lista.mostrar()

    print("\n=== 2. DEMOSTRACIÓN PILA (LIFO) Y RETO INDIVIDUAL ===")
    pila = Pila()
    pila.apilar("M01: Alimento")
    pila.apilar("M02: Correa")
    pila.apilar("M03: Cama")

    # RETO INDIVIDUAL (15 pts): Cuenta los elementos de la pila sin modificarla
    cantidad_elementos = len(pila.items)
    print(f"Cantidad de elementos en la pila (sin modificar): {cantidad_elementos}")

    # Demostración LIFO (Last In, First Out)
    print("Desapilando (LIFO):", pila.desapilar())  # Sale M03: Cama
    print("Desapilando (LIFO):", pila.desapilar())  # Sale M02: Correa
    print("Desapilando (LIFO):", pila.desapilar())  # Sale M01: Alimento
    print("Desapilando (Pila vacía):", pila.desapilar())

    print("\n=== 3. DEMOSTRACIÓN COLA (FIFO) ===")
    cola = Cola()
    cola.encolar("M01: Alimento")
    cola.encolar("M02: Correa")
    cola.encolar("M03: Cama")

    # Demostración FIFO (First In, First Out)
    print("Desencolando (FIFO):", cola.desencolar())  # Sale M01: Alimento
    print("Desencolando (FIFO):", cola.desencolar())  # Sale M02: Correa
    print("Desencolando (FIFO):", cola.desencolar())  # Sale M03: Cama
    print("Desencolando (Cola vacía):", cola.desencolar())

