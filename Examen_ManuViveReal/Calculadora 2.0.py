
def suma(valor1, valor2):
    return valor1 + valor2

def resta(valor1, valor2):
    return valor1 - valor2

def multiplicacion(valor1, valor2):
    return valor1 * valor2

def division(valor1, valor2):
    if valor2 != 0:
        return valor1 / valor2
    else:
        return "Error: No se puede dividir entre cero."

# Solicitar al usuario que ingrese los valores
valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))

# Imprimir los resultados obtenidos
print("Suma:", suma(valor1, valor2))
print("Resta:", resta(valor1, valor2))
print("Multiplicación:", multiplicacion(valor1, valor2))
print("División:", division(valor1, valor2))


