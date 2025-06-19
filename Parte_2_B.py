"""Operaciones con años de nacimiento
· Ingreso de los años de nacimiento (Si dos o mas integrantes del grupo tienen el mismo año, 
  ingresar algún dato ficticio, según el caso).
· Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.
· Si todos nacieron después del 2000, mostrar "Grupo Z".
· Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".
· Implementar una función para determinar si un año es bisiesto.
· Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.
"""
# Importamos la paquete bisiesto
import bisiesto as bi 
import itertools


#Ingreso de los años de nacimiento
print("Ingrese su año de nacimiento: [Coloque 0 para terminar]")
a = 1 # generamos un contador 
anios = []
edades = []
while a != 0:
    a = int(input(": "))
    if a != 0:
        anios.append(a)
        edades.append(2025-a)

#Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.
#Si todos nacieron después del 2000, mostrar "Grupo Z".

contador_pares = 0   # Inicializar contadores
contador_impares = 0
contador_2000= 0
contador_bisiestro = 0
i=0
while i < len(anios):
    anio=anios[i]
    # Contar cuantos años son pares y cuantos impares 
    if anio % 2 == 0: # Verifica si el resto de la división por 2 es igual a 0
        contador_pares += 1
    else:
        contador_impares += 1
    
    # Cuenta cuantos son mayores que 2000
    if anio > 2000: 
        contador_2000 +=1

    # Verificar si hay años bisiestos 
    if bi.es_bisiesto(anio):
        contador_bisiestro +=1
    
    i+=1

# Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales 
producto_cartesiano = []
for año in anios:
    for edad in edades:
        producto_cartesiano.append((año, edad))

#Muestra resultados

print(f"Nacidos en años pares: {contador_pares}")
print(f"Nacidos en años impares: {contador_impares}")
if contador_2000 == len(anios):
    print('"Grupo Z"')
if contador_bisiestro > 0:
    print('"Tenemos un año especial"')
print("Producto Cartesiano entre años y edades:")
for par in producto_cartesiano:
    print(par)

def es_bisiesto(año):
    """
    Función para determinar si un año es bisiesto.
    :param año: Año a verificar.
    :return: True si el año es bisiesto, False de lo contrario.
    """
    if año % 400 == 0:
        return True
    if año % 100 == 0:
        return False
    if año % 4 == 0:
        return True
    return False

# Ejemplo de uso
if __name__ == "__main__":
    año = int(input("Ingrese un año: "))
    if es_bisiesto(año):
        print(f"{año} es un año bisiesto.")
    else:
        print(f"{año} no es un año bisiesto.")