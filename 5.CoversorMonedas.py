"""
Programa que sirve para convertir un valor de una moneda a otra, según las necesidades del usuario.

Autor: Marco Vinicio Esparza

Versión: v3.1.1
"""

from forex_python.converter import CurrencyRates
import big_o

# Crear un diccionario con una lista de monedas válidas para correr el programa
monedas_validas = {'USD': 'Dólar estadounidense', 'EUR': 'Euro', 'GBP': 'Libra esterlina', 'JPY': 'Yen japonés', 'CAD': 'Dólar canadiense', 'AUD': 'Dólar australiano', 'MXN':'Peso Mexicano','CNY':'Renminbi Chino', 'CHF':'Franco Suizo', 'BRL':'Real Brasileño','PHP':'Peso Filipinas', 'MYR':'Ringgit Malasio','INR':'Rupia India', 'ZAR':'Rand Sudafricano','IDR':'Rupia Indonesia','TRY':'Lira Turca'}

def convertir_moneda(origen, destino, cantidad):
    """
    Proceso que convierte una cantidad de una moneda a otra utilizando la biblioteca "forex-python".
    Parámetros:
    --------------
    Si, recibe tres parámetros.
    origen y destino: es el código de la moneda origen, se utiliza para especificar de qué moneda se va a convertir. Es un string con el formato "USD", "EUR", etc.
    cantidad: es la cantidad de la moneda origen a convertir. Es un número decimal.

    Retorna:
    --------------
    Si, retorna resultado que es la cantidad equivalente en la moneda destino después de realizar la conversión.
    """
    # Se crea una instancia de la clase CurrencyRates
    c = CurrencyRates()
    # Se utiliza el método convert() para calcular el resultado de la conversión
    resultado = c.convert(origen, destino, cantidad)
    # Se devuelve el resultado de la conversión
    return resultado

def obtener_datos():
    """
    Proceso que se utiliza para recibir los datos necesarios para realizar la conversión de moneda.
    Parámetros:
    --------------
    No recibe ningún parámetro.

    Retorna:
    --------------
    Si, retorna tres parámetros.
    origen y destino: es el código de la moneda origen, se utiliza para especificar de qué moneda se va a convertir. Es un string con el formato "USD", "EUR", etc.
    cantidad: es la cantidad de la moneda origen a convertir.
    """
    # Pide al usuario que ingrese el código de la moneda origen
    origen = input("Ingrese la moneda de origen (ejemplo: USD): ")
    # Pide al usuario que ingrese el código de la moneda destino
    destino = input("Ingrese la moneda de destino (ejemplo: EUR): ")
    # Pide al usuario que ingrese la cantidad a convertir y la convierte a un número decimal
    cantidad = float(input("Ingrese la cantidad a convertir: "))
    # Devuelve los valores ingresados por el usuario
    return origen, destino, cantidad

def mostrar_monedas():
    """
    Proceso que se utiliza para imprimir una lista de las monedas válidas que son aceptadas por la función de conversión de monedas.
    Parámetros:
    --------------
    No recibe ningún parámetro.

    Retorna:
    --------------
    No retorna ningún parámetro.
    """
    # Imprime una lista de monedas válidas
    print("Lista de monedas válidas:")
    # Itera sobre cada moneda en monedas_validas
    for moneda in monedas_validas:
        # Imprime el código de la moneda y su nombre
        print(moneda + ": " + monedas_validas[moneda])

if __name__ == '__main__':
    # inicializar el programa
    print("********* CONVERSOR DE MONEDA *********")
    # iniciar bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        # llama a la funcion mostrar_monedas
        mostrar_monedas()
        origen, destino, cantidad = obtener_datos()
        # guarda convertir_moneda en una variable resultado
        resultado = convertir_moneda(origen, destino, cantidad)
        print(cantidad, origen, "es igual a", resultado, destino)

        # Variable para calcular la complejidad
        com1 = lambda n: obtener_datos
        com2 = lambda m: resultado
        # calcular la complejidad en el tiempo
        best, others = big_o.big_o(com2, com1)
        verificarComplejidad = input("¿Desea verificar la complejidad en el tiempo de la funcion? (si/no): ")
        if verificarComplejidad.lower() == "si":
            print(best)

        # preguntar si quiere volver a usar el programa  
        repetirProceso = input("¿Repetir proceso? (si/no): ")
        if repetirProceso.lower() != "si":
            print("********** FIN DEL PROCESO **********")
            # detener el bucle por completo
            break