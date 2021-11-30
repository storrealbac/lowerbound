# Ordenamiento burbuja
El ordenamiento burbuja es un algoritmo sencillo que permite ordenar una lista de valores intercambiando los valores adyacentes si no están dispuestos de forma correcta.

Si el largo de la lista es $n$ podemos asumir que existen  $n-1$ parejas. Por cada vez que el algoritmo recorre todas las parejas, el ultimo elemento estará ordenado de forma correcta y así sucesivamente hasta ordenar todas las parejas de elementos.

Este algoritmo no es eficiente  y normalmente tiene fines educativos.

Aquí un ejemplo:![Bubble sort visualization](https://upload.wikimedia.org/wikipedia/commons/0/06/Bubble-sort.gif)
## Complejidad algorítmica
Peor caso: $O(n^2)$

Mejor caso: $O(n)$

Espacio auxiliar: $O(1)$

## Implementación
La idea del algoritmo es recorrer $n-1$ veces, las parejas que no están ordenadas correctamente, para poder así cambiarlas de posición.

También se necesitaría una función $\textrm{swap}$, que permita cambiar los valores de posición.

Aquí una implementación en C++
```cpp
void bubbleSort(vector<int> &v) {
	for (int i = 0; i < v.size()-1; i++)
		for (int j = 0; j < v.size()-i-1; j++)
			if (v[j] > v[j+1])
				swap(v[j], v[j+1]
}
```
