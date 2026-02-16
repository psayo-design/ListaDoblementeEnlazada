# README — Lista Doblemente Enlazada en Python

## Cómo ejecutar el programa

1. Guarda el código en un archivo, por ejemplo:

```
lista_doblemente_enlazada.py
```

2. Abre una terminal en la carpeta donde guardaste el archivo.

3. Ejecuta:

```bash
python lista_doblemente_enlazada.py
```

---

## Estructura del programa

### Clase Nodo
Representa cada elemento de la lista.

Contiene:

- Nombre
- Apellido
- Carnet
- Referencia al nodo siguiente
- Referencia al nodo anterior

---

### Clase ListaDoblementeEnlazada
Administra toda la estructura de la lista.

Incluye los métodos:

- Insertar al principio
- Insertar al final
- Eliminar por carnet
- Mostrar lista (inicio → fin)
- Mostrar lista inversa (fin → inicio)

---

## Opciones del menú

Al ejecutar el programa aparecerá:

```
========= MENÚ =========
1. Insertar al principio
2. Insertar al final
3. Eliminar por carnet
4. Mostrar lista
5. Mostrar lista inversa (extra)
6. Salir
```

### Insertar al principio
Agrega un nuevo nodo al inicio de la lista.

Se solicitará:

- Nombre
- Apellido
- Carnet

---

### Insertar al final
Agrega un nuevo nodo al final de la lista.

Se solicitará:

- Nombre
- Apellido
- Carnet

---

### Eliminar por carnet
Busca y elimina el nodo cuyo carnet coincida.

Si no existe, se mostrará un mensaje indicando que no se encontró.

---

### Mostrar lista
Muestra la lista desde el primer nodo hasta el último.

Ejemplo:

```
None <- [Juan Pérez (2023001)] <-> [Ana López (2023002)] <-> None
```

---

### Mostrar lista inversa (extra)
Muestra la lista desde el último nodo hasta el primero.

---

### Salir
Finaliza la ejecución del programa.

---

## Ejemplo de uso

1. Insertar varios registros
2. Visualizar la lista
3. Eliminar un carnet específico
4. Mostrar nuevamente la lista

---

## Notas importantes

- La lista inicia vacía.
- Los carnets no se validan como únicos.
- Los datos se almacenan solo en memoria (no se guardan en archivos).
- Al cerrar el programa, toda la información se pierde.
