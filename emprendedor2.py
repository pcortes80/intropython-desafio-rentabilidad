# Importa librerias
import sys

# Lee el largo del script, para asegurarse de ingresar la cantidad de argumentos correctos
largo = len(sys.argv)

# Solo si la cantidad de argumentos ingresados es correcta se realizan los calculos
if largo > 5:
    usuarios_normales = float(sys.argv[1]) # lee el primer argumento del script : numeros de usuarios normales
    usuarios_premium = float(sys.argv[2]) # lee el segundo argumento del script : numero de usuarios premium
    usuarios_prueba = float(sys.argv[3]) # lee el tercer argumento del script : numero de usuarios de prueba
    precio_venta = float(sys.argv[4]) # lee el cuarto argumento del script : precio de venta del servicio
    gastos = float(sys.argv[5]) # lee el quinto argumento del script : gastos asociados
        
    # Calcula las Utilidades por tipo de usuario
    utilidades_usuarios_normales = precio_venta*usuarios_normales - gastos
    utilidades_usuarios_premium = 2*precio_venta*usuarios_premium - gastos
    utilidades_usuarios_prueba = - gastos
    print("Las utilidades de los usuarios normales son " + str(utilidades_usuarios_normales) + ".")
    print("Las utilidades de los usuarios premium son " + str(utilidades_usuarios_premium) + ".")
    print("Las utilidades de los usuarios de prueba son " + str(utilidades_usuarios_prueba) + ".")

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