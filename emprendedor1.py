# Importa librerias
import sys

# Lee el largo del script, para asegurarse de ingresar la cantidad de argumentos correctos
largo = len(sys.argv)

# Solo si la cantidad de argumentos ingresados es correcta se realizan los calculos
if largo > 3:
    precio_venta = float(sys.argv[1]) # lee el primer argumento del script : precio de venta del servicio
    usuarios = float(sys.argv[2]) # lee el segundo argumento del script : numero de usuarios inscritos
    gastos = float(sys.argv[3]) # lee el tercer argumento del script : gastos asociados
    
    # Calcula las Utilidades
    utilidades = precio_venta*usuarios - gastos
    print("Las utilidades calculadas son de " + str(utilidades) + ".")

    """
    # Calcula el valor de Ue (velocidad de escape)
    # Usa round() para redondear hacia arriba con 2 decimales
    Ue = round(((2*g*r)**0.5),2)
    
    # Imprime en pantalla la velocidad de escape
    print("La velocidad de escape es " + str(Ue) + " m/s.")
    """
else:
    # Mensaje al usuario
    print("Hay argumentos que faltan. Por favor intente de nuevo.")

# Fin del programa