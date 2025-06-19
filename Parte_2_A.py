#TP Integrador II de Matematica
#Conjuntos DNI

# Parte 2 – Desarrollo del Programa en Python
# El programa debe implementar varias de las ideas trabajadas en papel. Debe incluir:

# A. Operaciones con DNIs
# ·         Ingreso de los DNIs (reales o ficticios).
# ·         Generación automática de los conjuntos de dígitos únicos.
# ·         Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.
# ·         Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
# ·         Suma total de los dígitos de cada DNI.
# ·         Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.
# Ejemplos:
# ·         Si un dígito aparece en todos los conjuntos, mostrar "Dígito compartido".
# ·         Si algún conjunto tiene más de 6 elementos, mostrar "Diversidad numérica alta


def Genera_Conjuntos(Aux):
    str_DNI = str(Aux)
    Conjunto_DNI = {int(digito) for digito in str_DNI}
    return Conjunto_DNI

def Union_Conjuntos(A,B):
    C = A.union(B)
    return C

def Union_total(A, B, C):
    U_total = A | B | C
    return U_total


def Inter_Conjuntos(A,B):
    C = A.intersection(B)
    return C

def Inter_Total(A,B,C):
    I_total = A & B & C
    return I_total

def Diferencia_Conjuntos(A,B):
    C = A - B
    return C

def Diferencia_simetrica(A,B):
    C = A.symmetric_difference(B)
    return C

def DSimetrica_total(A, B, C):
    Ds_total= A ^ B ^ C 
    return Ds_total

def contar_frecuencia_digitos(dni):
    frecuencia = {str(i): 0 for i in range(10)}
    suma_total = 0
    for digito in dni:
        if digito in frecuencia:
            frecuencia[digito] += 1
            suma_total += int(digito)
    return frecuencia, suma_total

def mostrar_elementos(conjunto):
    elementos = ""
    for i, digito in enumerate(conjunto):
        if i > 0:
            elementos += ", "
        elementos += str(digito)
    return elementos

    
#DNI de los Integrantes de Grupo
#Generacion de Conjuntos apartirde los DNI con los que se va a operar

DNI_1 = 34711991
conjunto_DNI1 = Genera_Conjuntos(DNI_1)

DNI_2 = 31230293
conjunto_DNI2 = Genera_Conjuntos(DNI_2)

DNI_3 = 39717139
conjunto_DNI3 = Genera_Conjuntos(DNI_3)

#Aquí mostramos los conjunto con los que se va a operar
print(f"Conjunto 1: {conjunto_DNI1}")
print(f"Conjunto 2: {conjunto_DNI2}")
print(f"Conjunto 3: {conjunto_DNI3}")

#Visualización de Operaciones de conjuntos unión, intersección, diferencias y diferencia simétrica
print("-----------------------Union de Conjuntos---------------------")

print(f"{conjunto_DNI1} Union {conjunto_DNI2} = {Union_Conjuntos(conjunto_DNI1,conjunto_DNI2)}")
print(f"{conjunto_DNI1} Union {conjunto_DNI3} = {Union_Conjuntos(conjunto_DNI1,conjunto_DNI3)}")
print(f"{conjunto_DNI2} Union {conjunto_DNI3} = {Union_Conjuntos(conjunto_DNI2,conjunto_DNI3)}")

print(f"Union Total de los Conjuntos = {Union_total(conjunto_DNI1,conjunto_DNI2,conjunto_DNI3)}")

print("--------------------Interseccion de Conjuntos------------------")

print(f"{conjunto_DNI1} Interseccion {conjunto_DNI2} = {Inter_Conjuntos(conjunto_DNI1,conjunto_DNI2)}")
print(f"{conjunto_DNI1} Interseccion {conjunto_DNI3} = {Inter_Conjuntos(conjunto_DNI1,conjunto_DNI3)}")
print(f"{conjunto_DNI2} Interseccion {conjunto_DNI3} = {Inter_Conjuntos(conjunto_DNI2,conjunto_DNI3)}")


print(f"Interseccion Total de los Conjuntos = {Inter_Total(conjunto_DNI1,conjunto_DNI2,conjunto_DNI3)}")

print("-------------------Diferencia de Conjuntos por Pares-----------------")
print(f"{conjunto_DNI1} Diferencia {conjunto_DNI2} = {Diferencia_Conjuntos(conjunto_DNI1,conjunto_DNI2)}")
print(f"{conjunto_DNI2} Diferencia {conjunto_DNI1} = {Diferencia_Conjuntos(conjunto_DNI2,conjunto_DNI1)}")

print(f"{conjunto_DNI1} Diferencia {conjunto_DNI3} = {Diferencia_Conjuntos(conjunto_DNI1,conjunto_DNI3)}")
print(f"{conjunto_DNI3} Diferencia {conjunto_DNI1} = {Diferencia_Conjuntos(conjunto_DNI3,conjunto_DNI1)}")

print(f"{conjunto_DNI2} Diferencia {conjunto_DNI3} = {Diferencia_Conjuntos(conjunto_DNI2,conjunto_DNI3)}")
print(f"{conjunto_DNI3} Diferencia {conjunto_DNI2} = {Diferencia_Conjuntos(conjunto_DNI3,conjunto_DNI2)}")


print("----------------Diferencia Simetrica de Conjuntos------------")

print(f"{conjunto_DNI1} Diferencia Simetrica {conjunto_DNI2} = {Diferencia_simetrica(conjunto_DNI1,conjunto_DNI2)}")
print(f"{conjunto_DNI1} Diferencia Simetrica {conjunto_DNI3} = {Diferencia_simetrica(conjunto_DNI1,conjunto_DNI3)}")
print(f"{conjunto_DNI2} Diferencia Simetrica {conjunto_DNI3} = {Diferencia_simetrica(conjunto_DNI2,conjunto_DNI3)}")

print(f"Diferencia Simetrica Total = {DSimetrica_total(conjunto_DNI1,conjunto_DNI2,conjunto_DNI3)}")


##################################################################################################################

print("----------------Conteo de frecuencia de cada dígito en cada DNI-----------------")
print("----------------Suma total de los dígitos de cada DNI-----------------")
dnis = [str(DNI_1), str(DNI_2), str(DNI_3)]
for dni in dnis:
    frecuencia, suma_total = contar_frecuencia_digitos(dni)
    print(f"Frecuencia de dígitos en el DNI {dni}:")
    for digito, count in frecuencia.items():
        if count > 0:
            print(f"Dígito {digito}: {count} veces")
    print(f"Suma total de los dígitos en el DNI {dni}: {suma_total}")
    print("")


################################################################################################################
print("--------------- Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas -------------------")

A = Inter_Total(conjunto_DNI1,conjunto_DNI2,conjunto_DNI3)
B = Union_total(conjunto_DNI1,conjunto_DNI2,conjunto_DNI3)
if len(A) != 0:
    elementos = mostrar_elementos(A)
    if len(A) > 1:
        print(f"Los digitos compartidos entre los tres DNIs son {elementos}.")
    else:
        print(f"El digito compartido entre los tres DNIs es {elementos}.")
else:
    print("No existe dígito común a todos los conjuntos")

if len(B)>0:
    elementos_union = mostrar_elementos(B)
    print(f"Los dígitos presente en los tres DNIs son {elementos_union}")

Conjunto_DNIs=[conjunto_DNI1,conjunto_DNI2, conjunto_DNI3]
digitos = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
for i in range(0, len(Conjunto_DNIs)):
    elementos_dni = Inter_Conjuntos(Conjunto_DNIs[i],{0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
    if len(elementos_dni) >=5:
        print(f"El DNI {dnis[i]} tiene 5 dígitos. Podemos decir que tiene 'Diversidad numérica alta'")




