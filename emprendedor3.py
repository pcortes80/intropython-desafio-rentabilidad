# Importa librerias
import sys

# Lee el largo del script, para asegurarse de ingresar la cantidad de argumentos correctos
largo = len(sys.argv)

# Solo si la cantidad de argumentos ingresados es correcta se realizan los calculos
if largo > 4:
    precio_venta = float(sys.argv[1]) # lee el primer argumento del script : precio de venta del servicio
    usuarios = float(sys.argv[2]) # lee el segundo argumento del script : numeros de usuarios
    gastos = float(sys.argv[3]) # lee el tercer argumento del script : gastos asociados
    utilidades_anteriores = float(sys.argv[4]) # lee el cuarto argumento del script : utilidades del año anterior
         
    # Calcula las Utilidades actuales
    utilidades_actuales = precio_venta*usuarios - gastos
    print("Las utilidades actuales son " + str(utilidades_actuales) + ".")
    
    # Muestra las utilidades anteriores por pantalla
    print("Las utilidades anteriores son " + str(utilidades_anteriores) + ".")
    
    # Calcula la razón entre las utilidades actuales y las del año anterior
    razon = round((utilidades_actuales/utilidades_anteriores),2)
    print("La razón entre las utilidades actuales y las anteriores es " + str(razon) + ".")
        
    if razon > 1:
        print("Por lo tanto, las utilidades actuales fueron superiores a las anteriores.")
    else:
        print("Por lo tanto, las utilidades actuales fueron menores a las anteriores.")
    
    # si el usuario no ingresa las utilidades anteriores, se asumirán 1000
else:
    precio_venta = float(sys.argv[1]) # lee el primer argumento del script : precio de venta del servicio
    usuarios = float(sys.argv[2]) # lee el segundo argumento del script : numeros de usuarios
    gastos = float(sys.argv[3]) # lee el tercer argumento del script : gastos asociados
    utilidades_anteriores = 1000 # se asume que las utilidades anteiores son 1000
         
    # Calcula las Utilidades actuales
    utilidades_actuales = precio_venta*usuarios - gastos
    print("Las utilidades actuales son " + str(utilidades_actuales) + ".")
    
    # Muestra las utilidades anteriores por pantalla
    print("Las utilidades anteriores son " + str(utilidades_anteriores) + ".")
    
    # Calcula la razón entre las utilidades actuales y las del año anterior
    razon = round((utilidades_actuales/utilidades_anteriores),2)
    print("La razón entre las utilidades actuales y las anteriores es " + str(razon) + ".")
    
    if razon > 1:
        print("Por lo tanto, las utilidades actuales fueron superiores a las anteriores.")
    else:
        print("Por lo tanto, las utilidades actuales fueron menores a las anteriores.")
        
# Fin del programa