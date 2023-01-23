"""
Programa que permite verificar las tasas de intercambio de las monedas mas usadas.

Autor: Marco Vinicio Esparza

Versión: v3.2.5
"""
# importar librerías necesarias
from forex_python.converter import CurrencyRates
import big_o

# Crear un diccionario con una lista de monedas válidas para correr el programa
monedas_validas = {'USD': 'Dólar estadounidense', 'EUR': 'Euro', 'GBP': 'Libra esterlina', 'JPY': 'Yen japonés', 'CAD': 'Dólar canadiense', 'AUD': 'Dólar australiano', 'MXN':'Peso Mexicano','CNY':'Renminbi Chino', 'CHF':'Franco Suizo', 'BRL':'Real Brasileño','PHP':'Peso Filipinas', 'MYR':'Ringgit Malasio','INR':'Rupia India', 'ZAR':'Rand Sudafricano','IDR':'Rupia Indonesia','TRY':'Lira Turca'}

def mostrar_monedas_validas():
    """
    Función que se encarga de imprimir una lista de monedas válidas.
    Parámetros:
    --------------
    No recibe ningún parámetro.

    Retorna:
    --------------
    No retorna ningún valor.
    """
    print("Lista de monedas válidas:")
    # Iterar a través de cada elemento en la lista de monedas válidas
    for moneda in monedas_validas:
        # Imprime el nombre de la moneda y su descripción
        print(moneda + ": " + monedas_validas[moneda])
        
def entrada_valida(c):
    """
    Proceso que valida que la entrada del usuario sea una moneda válida.
    Parámetros:
    --------------
    Si, recibe un parámetro "c" que es una cadena de texto que se utiliza como el mensaje de solicitud de entrada.

    Retorna:
    --------------
    Si, retorna la entrada del usuario, previamente validada que se encuentra en la lista de monedas validas.
    """
    # El ciclo while se ejecutará mientras se cumpla la condición "True"
    while True:
        # Solicitar una entrada del usuario utilizando el parámetro "c" como el mensaje de solicitud de entrada
        entrada = input(c)
        # Si la entrada del usuario se encuentra en la lista "monedas_validas", 
        if entrada in monedas_validas:
            return entrada
        # Si la entrada no se encuentra en la lista "monedas_validas", se imprime un mensaje de error
        print("Moneda no válida, por favor ingrese una moneda válida.")

def tasa_intercambio(base, cotizacion):
    """
    Proceso que calcula la tasa de intercambio entre dos monedas.
    Parámetros:
    --------------
    Si, recibe dos parámetros:
    "base" es una cadena de texto que representa la moneda base
    "cotizacion" es una cadena de texto que representa la moneda con la que se va a comparar.

    Retorna:
    --------------
    Si, retorna un número flotante que representa la tasa de intercambio entre las dos monedas.
    """
    # Crear una instancia de la clase "CurrencyRates"
    c = CurrencyRates()
    # Utilizar el método "get_rate" de la clase "CurrencyRates" para obtener la tasa de cambio entre la moneda base "base" y la moneda de cotización "cotizacion"
    return c.get_rate(base, cotizacion)

if __name__ == '__main__':
    # inicializar el programa
    print("********* VERIFICAR TASAS DE INTERCAMBIO *********")
    # iniciar bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        # Llamar a la función "mostrar_monedas_validas" para mostrar las monedas válidas
        valida = mostrar_monedas_validas()
        # Almacenar la entrada del usuario en una variable "base" mediante la función "entrada_valida"
        base = entrada_valida("Ingrese la moneda base: ")
        # Almacenar la entrada del usuario en una variable "cotizacion" mediante la función "entrada_valida"
        cotizacion = entrada_valida("Ingrese la moneda de cotización: ")
        # Almacenar la tasa de intercambio en una variable "indice" mediante la función "tasa_intercambio"
        indice = tasa_intercambio(base, cotizacion)
        # Llamar a la función "mostrar_tasa_intercambio" para mostrar la tasa de intercambio entre las monedas base y cotizacion
        print("1 " + base + " = " + str(indice) + " " + cotizacion)
        
        # Variable para calcular la complejidad
        com1 = lambda n: valida
        com2 = lambda m: indice
        # calcular la complejidad en el tiempo
        best, others = big_o.big_o(com1, com2)
        verificarComplejidad = input("¿Desea verificar la complejidad en el tiempo de la funcion? (si/no): ")
        if verificarComplejidad.lower() == "si":
            print(best)

        # preguntar si quiere volver a usar el programa  
        repetirProceso = input("¿Repetir proceso? (si/no): ")
        if repetirProceso.lower() != "si":
            print("********** FIN DEL PROCESO **********")
            # detener el bucle por completo
            break