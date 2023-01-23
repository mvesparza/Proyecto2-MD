"""
Programa que permite verificar los precios de acciones de empresas conocidas.

Autor: Marco Vinicio Esparza

Versión: v2.3.2
"""

import requests
import big_o

def obtener_precio_accion(simbolo, api_key):
    """
    Proceso que obtiene el precio actual de una acción específica a través de una consulta a una API.
    Parámetros:
    --------------
    Si, recibe dos parámetros.
    simbolo : es el símbolo de la empresa para la cual se desea obtener el precio.
    api_key : es la clave de acceso a la API que se va a utilizar para hacer la consulta.

    Retorna:
    --------------
    Si, retorna el precio actual de la acción de la empresa especificada en el símbolo.
    """
    # Hacer petición a la API
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={simbolo}&apikey={api_key}"
    respuesta = requests.get(url)
    # Convertir la respuesta a JSON
    datos = respuesta.json()
    # Retorna el precio actual de la acción
    return datos["Global Quote"]["05. price"]

if __name__ == '__main__':
    # inicializar el programa
    print("********* VERIFICAR PRECIOS *********")
    # iniciar bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        # Tu clave de API
        api_key = "TU_CLAVE_API"
        # Diccionario de simbolos validos
        simbolos = {
        "Apple Inc.": "AAPL",
        "Google Inc.": "GOOG",
        "Amazon.com Inc.": "AMZN",
        "Tesla Inc.": "TSLA",
        "Microsoft Corp." : "MSFT",
        "Coca-Cola Co." : "KO",
        "Pfizer Inc." : "PFE",
        "Walt Disney Co." : "DIS",
        "Procter & Gamble Co." : "PG",
        "IBM Corporation": "IBM",
        "General Electric Co.": "GE",
        "AT&T Inc." : "T",
        "Walmart Inc." : "WMT",
        "Chevron Corporation" : "CVX",
        "The Home Depot, Inc." : "HD",
        "Boeing Co." : "BA",
        "Caterpillar Inc." : "CAT",
        "Cisco Systems, Inc." : "CSCO",
        "Dow Inc." : "DOW",
        "Exxon Mobil Corporation" : "XOM"
        }
        # Muestra la lista de simbolos validos
        print("Símbolos válidos:")
        for nombre, simbolo in simbolos.items():
            print(f"{nombre} ({simbolo})")
        # Pide al usuario que ingrese el simbolo de la empresa
        simbolo = input("Ingresa el símbolo de la empresa: ")
        # Verifica que el simbolo sea valido
        while simbolo not in simbolos.values():
            print(f"{simbolo} no es un símbolo válido.")
            simbolo = input("Ingresa el símbolo de la empresa: ")
        # Obtiene el precio actual de la acción
        precio = obtener_precio_accion(simbolo, api_key)
        # Imprimir el precio actual de la acción
        print(f"El precio actual de la acción {simbolo} es ${precio}")

        # Variable para calcular la complejidad
        com1 = lambda n: simbolo
        com2 = lambda m: precio
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