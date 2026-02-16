# ============================================
# LISTA DOBLEMENTE ENLAZADA (SIN GRAPHVIZ)
# ============================================

# ---------- CLASE NODO ----------
class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.carnet})"


# ---------- CLASE LISTA DOBLEMENTE ENLAZADA ----------
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    # Insertar al principio
    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)

        if self.cabeza is None:
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

        print("Nodo insertado al principio correctamente.")

    # Insertar al final
    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)

        if self.cola is None:
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

        print("Nodo insertado al final correctamente.")

    # Eliminar por carnet
    def eliminar_por_valor(self, carnet):
        actual = self.cabeza

        while actual:
            if actual.carnet == carnet:

                # Si es el primero
                if actual.anterior is None:
                    self.cabeza = actual.siguiente
                    if self.cabeza:
                        self.cabeza.anterior = None
                else:
                    actual.anterior.siguiente = actual.siguiente

                # Si es el último
                if actual.siguiente is None:
                    self.cola = actual.anterior
                    if self.cola:
                        self.cola.siguiente = None
                else:
                    actual.siguiente.anterior = actual.anterior

                print("Nodo eliminado correctamente.")
                return

            actual = actual.siguiente

        print("No se encontró un nodo con ese carnet.")

    # Mostrar lista
    def mostrar_lista(self):
        actual = self.cabeza
        resultado = "None <- "

        while actual:
            resultado += f"[{actual}] <-> "
            actual = actual.siguiente

        resultado += "None"
        print(resultado)

    # Mostrar lista en orden inverso (extra opcional)
    def mostrar_lista_inversa(self):
        actual = self.cola
        resultado = "None <- "

        while actual:
            resultado += f"[{actual}] <-> "
            actual = actual.anterior

        resultado += "None"
        print(resultado)


# ---------- MENÚ PRINCIPAL ----------
def menu():
    lista = ListaDoblementeEnlazada()

    while True:
        print("\n========= MENÚ =========")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por carnet")
        print("4. Mostrar lista")
        print("5. Mostrar lista inversa (extra)")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.insertar_al_principio(nombre, apellido, carnet)

        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.insertar_al_final(nombre, apellido, carnet)

        elif opcion == "3":
            carnet = input("Carnet a eliminar: ")
            lista.eliminar_por_valor(carnet)

        elif opcion == "4":
            lista.mostrar_lista()

        elif opcion == "5":
            lista.mostrar_lista_inversa()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# ---------- EJECUCIÓN ----------
if __name__ == "__main__":
    menu()
