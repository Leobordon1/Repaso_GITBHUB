"""
def es_par_o_es_impar(numero):
    if numero % 2 == 0:
        return "Par." 
    else:
        return "Impar"

numero = int(input("Introduce un número:"))  
print(f"El número {numero} ingresado es: {es_par_o_es_impar(numero)}") 
""" 
"""
def es_mayor_de_edad(edad):
    if edad >= 18:
        return "Mayor de Edad"
    else:
        return "Menor de Edad"

edad = int(input("Ingrese su edad: "))
print(es_mayor_de_edad(edad))
"""
"""
def calcular_descuento(precio,porcentaje):
       descuento = (precio * porcentaje/100)
       total = precio - descuento
       return total

precio = 1000
porcentaje = 20
print(calcular_descuento(precio, porcentaje))
"""

"""
def es_contraseña_segura(contraseña):
    tiene_letra = any(c.isalpha() for c in contraseña)
    tiene_numero = any(c.isdigit() for c in contraseña)
    if len(contraseña) >= 8 and tiene_letra and tiene_numero:
        return "Segura"
    else:
         return "Insegura"


contraseña= input("Ingrese su contraseña:")
print(es_contraseña_segura(contraseña))
"""
"""
def analizar_palabra(palabra):
    mayusculas = 0
    minusculas = 0
    longitud = len(palabra)
    for caracter in palabra:
        if caracter.isupper():
            mayusculas +=1 
        elif caracter.islower():
            minusculas +=1
    return {
        "longitud": longitud,
        "mayúsculas": mayusculas,
        "minúsculas": minusculas
    }

palabra = "Leonel Bordon"
resultado = analizar_palabra(palabra)
print("Análisis de la palabra:", palabra)
print("Longitud:", resultado["longitud"])
print("Mayúsculas:", resultado["mayúsculas"])
print("Minúsculas:", resultado["minúsculas"])
"""

def calcular_promedio(lista):
    promedio = sum(lista) / len(lista)
    mayor = max(lista)
    menor = min(lista)
    return {
        "Promedio": promedio,
        "Mayor": mayor,
        "Menor": menor
    }


numeros = [5,10,15]
diccionario = calcular_promedio(numeros)
print("Promedio:", diccionario["Promedio"])
print("Mayor:", diccionario["Mayor"])
print("Menor:", diccionario["Menor"])