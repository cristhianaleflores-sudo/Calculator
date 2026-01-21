# ============================
# CALCULADORA  tradicional  (con historial)
# ============================

# Historial global de operaciones
historial = []

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*50)
    print("CALCULADORA AVANZADA")
    print("="*50)
    print("1. Suma de 'n' números (positivos y negativos)")
    print("2. Producto entre 'n' números")
    print("3. División entre 2 números")
    print("4. Calcular factorial (n!)")
    print("5. Tablas de multiplicar (del 1 al 10)")
    print("6. Calcular cuadrado y cubo de un número")
    print("7. Calcular promedio de una serie de números")
    print("8. Encontrar máximo y mínimo de 'n' números")
    print("9. Salir")
    print("10. Ver historial de operaciones")
    print("="*50)

def suma_n_numeros():
    """Realiza la suma de n números ingresados por el usuario"""
    print("\n--- SUMA DE N NÚMEROS ---")
    try:
        n = int(input("¿Cuántos números desea sumar?: "))

        if n <= 0:
            print("Debe ingresar un número mayor que 0.")
            return

        suma = 0
        numeros = []
        for i in range(1, n + 1):
            try:
                num = float(input(f"Ingrese el número {i}: "))
                numeros.append(num)
                suma += num
            except ValueError:
                print("Error: Debe ingresar un número válido.")
                return

        print(f"\nLa suma de los {n} números es: {suma}")
        historial.append(f"Suma de {n} números {numeros} = {suma}")

    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

def producto_n_numeros():
    """Realiza el producto de n números ingresados por el usuario"""
    print("\n--- PRODUCTO DE N NÚMEROS ---")
    try:
        n = int(input("¿Cuántos números desea multiplicar?: "))

        if n <= 0:
            print("Debe ingresar un número mayor que 0.")
            return

        producto = 1
        numeros = []
        for i in range(1, n + 1):
            try:
                num = float(input(f"Ingrese el número {i}: "))
                numeros.append(num)
                producto *= num
            except ValueError:
                print("Error: Debe ingresar un número válido.")
                return

        print(f"\nEl producto de los {n} números es: {producto}")
        historial.append(f"Producto de {n} números {numeros} = {producto}")

    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

def division_dos_numeros():
    """Realiza la división entre dos números"""
    print("\n--- DIVISIÓN ENTRE 2 NÚMEROS ---")
    try:
        num1 = float(input("Ingrese el dividendo: "))
        num2 = float(input("Ingrese el divisor: "))

        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            print(f"\n{num1} ÷ {num2} = {resultado}")
            historial.append(f"División: {num1} ÷ {num2} = {resultado}")

    except ValueError:
        print("Error: Debe ingresar números válidos.")

def calcular_factorial():
    """Calcula el factorial de un número"""
    print("\n--- CÁLCULO DE FACTORIAL ---")
    try:
        n = int(input("Ingrese un número entero no negativo: "))

        if n < 0:
            print("Error: El factorial no está definido para números negativos.")
            return

        factorial = 1
        for i in range(1, n + 1):
            factorial *= i

        print(f"\n{n}! = {factorial}")
        historial.append(f"Factorial: {n}! = {factorial}")

    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

def tablas_multiplicar():
    """Muestra las tablas de multiplicar del 1 al 10"""
    print("\n--- TABLAS DE MULTIPLICAR ---")
    try:
        tabla = int(input("Ingrese el número de tabla que desea ver (1-10): "))

        if tabla < 1 or tabla > 10:
            print("Error: Debe ingresar un número entre 1 y 10.")
            return

        print(f"\nTabla del {tabla}:")
        print("-" * 15)
        for i in range(1, 11):
            print(f"{tabla} x {i} = {tabla * i}")

        historial.append(f"Tabla de multiplicar consultada: Tabla del {tabla}")

    except ValueError:
        print("Error: Debe ingresar un número válido.")

def calcular_cuadrado_cubo():
    """Calcula el cuadrado y cubo de un número"""
    print("\n--- CUADRADO Y CUBO DE UN NÚMERO ---")
    try:
        num = float(input("Ingrese un número: "))

        cuadrado = num ** 2
        cubo = num ** 3

        print(f"\nNúmero: {num}")
        print(f"Cuadrado: {cuadrado}")
        print(f"Cubo: {cubo}")

        historial.append(f"Cuadrado y cubo: {num}² = {cuadrado}, {num}³ = {cubo}")

    except ValueError:
        print("Error: Debe ingresar un número válido.")

def calcular_promedio():
    """Calcula el promedio de una serie de números terminada con -1"""
    print("\n--- CÁLCULO DE PROMEDIO ---")
    print("Ingrese números para calcular el promedio.")
    print("Para terminar, ingrese -1")

    numeros = []
    contador = 1

    while True:
        try:
            entrada = input(f"Ingrese el número {contador} (o -1 para terminar): ")
            num = float(entrada)

            if num == -1:
                break

            numeros.append(num)
            contador += 1

        except ValueError:
            print("Error: Debe ingresar un número válido.")

    if len(numeros) == 0:
        print("No se ingresaron números para calcular el promedio.")
    else:
        promedio = sum(numeros) / len(numeros)
        print(f"\nCantidad de números ingresados: {len(numeros)}")
        print(f"Suma total: {sum(numeros)}")
        print(f"Promedio: {promedio}")

        historial.append(f"Promedio de {len(numeros)} números {numeros} = {promedio}")

def encontrar_maximo_minimo():
    """Encuentra el máximo y mínimo de n números enteros"""
    print("\n--- MÁXIMO Y MÍNIMO DE N NÚMEROS ---")
    try:
        n = int(input("¿Cuántos números desea ingresar?: "))

        if n <= 0:
            print("Debe ingresar un número mayor que 0.")
            return

        numeros = []
        for i in range(1, n + 1):
            try:
                num = int(input(f"Ingrese el número entero {i}: "))
                numeros.append(num)
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
                return

        if numeros:
            maximo = max(numeros)
            minimo = min(numeros)

            print(f"\nCantidad total de valores: {len(numeros)}")
            print(f"Valor máximo: {maximo}")
            print(f"Valor mínimo: {minimo}")
            print(f"Lista de números ingresados: {numeros}")

            historial.append(f"Máximo y mínimo de {n} números {numeros} -> Máx: {maximo}, Mín: {minimo}")

    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

def mostrar_historial():
    """Muestra el historial de operaciones realizadas"""
    print("\n--- HISTORIAL DE OPERACIONES ---")

    if not historial:
        print("No se han realizado operaciones aún.")
    else:
        for i, operacion in enumerate(historial, start=1):
            print(f"{i}. {operacion}")

def main():
    """Función principal del programa"""
    print("BIENVENIDO A LA CALCULADORA AVANZADA")

    while True:
        mostrar_menu()

        try:
            opcion = int(input("\nSeleccione una opción (1-10): "))

            if opcion == 1:
                suma_n_numeros()
            elif opcion == 2:
                producto_n_numeros()
            elif opcion == 3:
                division_dos_numeros()
            elif opcion == 4:
                calcular_factorial()
            elif opcion == 5:
                tablas_multiplicar()
            elif opcion == 6:
                calcular_cuadrado_cubo()
            elif opcion == 7:
                calcular_promedio()
            elif opcion == 8:
                encontrar_maximo_minimo()
            elif opcion == 9:
                print("\n¡Gracias por usar la Calculadora Avanzada!")
                print("¡Hasta pronto!")
                break
            elif opcion == 10:
                mostrar_historial()
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 10.")

        except ValueError:
            print("Error: Debe ingresar un número válido.")

        # Pausa antes de mostrar el menú nuevamente
        input("\nPresione Enter para continuar...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
