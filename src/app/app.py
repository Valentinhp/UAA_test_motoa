from __future__ import absolute_import

class App:
    @staticmethod
    def add(a, b):
        """
        Retorna la suma de a y b.
        """
        return a + b

    def resta(self, a, b):
        """
        Resta b de a y retorna el resultado.
        """
        return a - b

    def multiplicacion(self, a, b):
        """
        Multiplica a por b y retorna el resultado.
        """
        return a * b

    def division(self, a, b):
        """
        Divide a entre b y retorna el resultado.
        Maneja la división por cero levantando una excepción.
        """
        if b == 0:
            raise ValueError("La división por cero no está permitida.")
        return a / b

    # 1. Verifica si una lista contiene un número primo
    def contiene_numero_primo(self, lista):
        """
        Verifica si hay al menos un número primo en la lista.
        Retorna True si hay un número primo, de lo contrario, False.
        """
        def es_primo(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5)+1, 2):
                if n % i == 0:
                    return False
            return True

        # Utilizamos any() para verificar si existe al menos un número primo
        return any(es_primo(num) for num in lista)

    # 2. Cuenta los números pares en un rango dado
    def contar_pares(self, inicio, fin):
        """
        Cuenta la cantidad de números pares en el rango desde 'inicio' hasta 'fin' (inclusive).
        Retorna la cantidad de números pares.
        """
        # Encontramos el primer y último número par en el rango
        primero = inicio if inicio % 2 == 0 else inicio + 1
        ultimo = fin if fin % 2 == 0 else fin - 1

        if ultimo < primero:
            return 0

        # Calculamos la cantidad total de números pares
        return ((ultimo - primero) // 2) + 1

    # 3. Encuentra el número máximo en una lista que sea múltiplo de un valor dado
    def maximo_multiplo(self, lista, multiplo):
        """
        Encuentra y retorna el valor máximo de la lista que es múltiplo del parámetro 'multiplo'.
        Si no hay múltiplos, retorna None.
        """
        # Filtramos los múltiplos y buscamos el máximo
        multiplos = (num for num in lista if num % multiplo == 0)
        try:
            return max(multiplos)
        except ValueError:
            return None

    # 4. Verifica si una palabra es palíndroma (se lee igual en ambos sentidos)
    def es_palindromo(self, palabra):
        """
        Verifica si la palabra es un palíndromo (igual al leerla al revés).
        Retorna True si es palíndromo, de lo contrario, False.
        """
        # Normalizamos la palabra eliminando espacios y convirtiendo a minúsculas
        palabra_limpia = ''.join(char.lower() for char in palabra if char.isalnum())
        return palabra_limpia == palabra_limpia[::-1]

    # 5. Calcula la suma de los primeros n números impares
    def suma_primeros_impares(self, n):
        """
        Calcula y retorna la suma de los primeros 'n' números impares.
        """
        # La suma de los primeros n impares es igual a n al cuadrado
        return n ** 2

    # 6. Verifica si todos los elementos de una lista son únicos
    def elementos_unicos(self, lista):
        """
        Verifica si todos los elementos de la lista son únicos.
        Retorna True si son únicos, de lo contrario, False.
        """
        # Comparamos la longitud de la lista con la longitud de un conjunto de sus elementos
        return len(lista) == len(set(lista))

    # 7. Calcula el factorial de un número sin usar recursión
    def calcular_factorial(self, numero):
        """
        Calcula y retorna el factorial de 'numero' usando un ciclo.
        """
        if numero < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

    # 8. Cuenta la cantidad de vocales en una cadena
    def contar_vocales(self, cadena):
        """
        Cuenta y retorna la cantidad de vocales en la cadena.
        """
        vocales = set('aeiouAEIOU')
        return sum(1 for char in cadena if char in vocales)

    # 9. Encuentra el segundo número mayor en una lista
    def segundo_mayor(self, lista):
        """
        Encuentra y retorna el segundo número más grande en la lista.
        Si no existe, retorna None.
        """
        # Usamos un conjunto para eliminar duplicados
        numeros_unicos = set(lista)
        if len(numeros_unicos) < 2:
            return None
        numeros_unicos.remove(max(numeros_unicos))
        return max(numeros_unicos)

    # 10. Calcula la serie de Fibonacci hasta n términos
    def fibonacci(self, n):
        """
        Genera y retorna una lista con los primeros 'n' términos de la serie de Fibonacci.
        """
        if n <= 0:
            return []
        serie = [0, 1]
        while len(serie) < n:
            serie.append(serie[-1] + serie[-2])
        return serie[:n]
