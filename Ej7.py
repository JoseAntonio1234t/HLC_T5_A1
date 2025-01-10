def entradadatos():
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el segundo número: "))
    return suma(numero1, numero2)
def suma(numero1, numero2):
    return "La suma de los números es " + str(numero1 + numero2)
print(entradadatos())