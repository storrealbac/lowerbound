# Números de Fibonacci

La sucesión de Fibonacci es la siguiente sucesión infinita de números naturales:

$$0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597 ...$$

Como se puede observar la sucesión empieza el número $0$ y $1$, luego a partir de esto, podemos definir que el siguiente número de la sucesión es la suma de los dos anteriores, así creando una relación de recurrencia (recursiva)

## Propiedades
Los números de Fibonacci tienen algunas propiedades interesantes, aquí alguna de ellas
- Identidad de Cassini: $F_{n-1}\cdot F_{n+1} - F_n^2=(-1)^n$
	
- Regla de la adición: $F_{n+k} = F_kF_{n+1} + F_{k-1}F_n$
	
- Si se aplica la identidad anterior también tenemos: $F_{2n}=F_n(F_{n+1} + F_{n-1})$
	
- También se puede demostrar con inducción que cualquier numero positivo $k$, $F_{nk} es multplo de $F_n$
	
- Lo inverso también es verdadero: Si $F_m$ es múltiplo de $F_n$, entonces $m$ es múltiplo de $n$
	
- Identidad del máximo común divisor: $\textrm{GCD}(F_m, F_n) = F_{\textrm{GCD}(m, \space n)}$
	
- Los números de Fibonacci son la peor entrada posible para el Algoritmo euclidiano

## Formula de Fibonacci
La formula de Binet, permite calcular un numero de Fibonacci en una sola operación
$$F_n = \frac{(\frac{1+\sqrt 5}{2})^n  - (\frac{1-\sqrt 5}{2})^n}{\sqrt 5}$$
Se puede observar que el valor absoluto del segundo termino siempre es menor que el primero, entonces podríamos decir que si obtenemos el valor de $F_n$ solo con el primer termino el resultado será muy similar.

$$F_n = \frac{(\frac{1+\sqrt5}{2})^n}{\sqrt5}$$

El único problema de esta forma de calcularlo es que necesitas mucha precisión al dividir, pero siguen siendo útiles para cálculos pequeños.

## Definición recursiva
Podemos definir recursivamente la función de Fibonacci de la siguiente manera.
Los casos bases serian los siguientes:
$$f_0 = 0$$

$$f_1 = 1$$
Y para cualquier numero natural mayor que uno, quedaría definido así
$$f_n = f_{n-1} + f_{n-2}$$

## Implementación recursiva
Esta es la implementación recursiva, pero no es la más eficiente, ya que como es una función recursiva se calculan muchos $f_n$ que ya se calcularon previamente.

La complejidad de esta solución es $\varphi ^n$, donde $\varphi = \frac{1 + \sqrt{5}}{2}$
```cpp
int fibonacci(int n) {
	// Acá definiriamos los casos bases (f_0 y f_1)
	if (n <= 1)
		return n;
	// En cualquier otro caso decimos que el f_n va
	// ser la suma de los dos anteriores.
	return fibonacci(n-1)+fibonacci(n-2);
}
```

## Implementación iterativa (con vector/arreglo/lista)
Esta implementación es mucho más eficiente que la anterior, pero es costosa en memoria, con una complejidad $O(n)$ en tiempo y memoria.
```cpp
int fibonacci(int n) {
	// Si es un caso base
	if (n <= 1)
		return n;
	// Creamos el vector
	vector<int> f(n+1);
	// Asignamos los casos bases
	f[0] = 0; f[1] = 1;
	
	// Asignamos el nuevo valor con la suma de los anteriores
	for (int k = 2; k <= n; k++)
		f[k] = f[k-1] + f[k-2];
	
	// Retornemos f[n]
	return f[n];
}
```

## Implementación iterativa (memoria constante)
Esta es la implementación lineal más eficiente (por el hecho de que tiene memoria constante),  con una complejidad en tiempo de $O(n)$ y de memoria $O(1)$, sin embargo no es la mejor forma de calcular un número de Fibonacci
```cpp
int fibonacci(int n) {
	int a = 0, b = 1;
	for (int i = 0; i < n-1; i++){
		b = b + a;
		a = b - a;
	}
	return b;
}
```

## Implementación dividir y conquistar
Si partimos de la siguiente ecuación, utilizando leyes de exponentes, es posible calcular $x^n$ como

![Ecuación dividir y conquistar Fibonacci](https://wikimedia.org/api/rest_v1/media/math/render/svg/2adbf062607df80b7db6645cd24529d57b7bb613)

De esta manera, el algoritmo será de tipo Divide y vencerás, con una complejidad en tiempo de $O(log_2(n))$ multiplicaciones matriciales. Sin embargo, no es necesario guardar los 4 valores de la matriz, ya que es de la siguiente forma:
$$
\begin{bmatrix}  
a & b\\  
b & a+b 
\end{bmatrix}
$$

Entonces, cada matriz queda representada en dos valores (a y b), su cuadrado se puede calcular como:
$$
\begin{bmatrix}  
a & b\\  
b & a+b 
\end{bmatrix}^2=
\begin{bmatrix}  
a^2 + b^2 & b(2a+b)\\  
b(2a+b) & (a+b)^2 + b^2
\end{bmatrix}^2
$$

Como resultado el algoritmo quedará de la siguiente forma:
```cpp
int fibonacci(int n) {
	// Solo acepta los numeros naturales
	if (n <= 0)
		return  0;
	// Definimos los valores iniciales
	int i = n-1, x = 0, y = 1;
	int a, b, c, d;
	// La matriz quedaria así
	a = y; b = x;
	c = x; d = y;
	while (i > 0) {
		// Si es impar
		if (i % 2) {
			x = d*b + c*a;
			y = d*(b+a) + c*b;
			a = x;
			b = y;
		}
		x = c*c + d*d;
		y = d*(2*c + d);
		c = x;
		d = y;
		i /= 2;
	}
	return a + b;
}
```
