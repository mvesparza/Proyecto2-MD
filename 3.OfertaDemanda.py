"""
Programa que permite verificar la oferta y demanda de acciones de empresas conocidas.

Autor: Marco Vinicio Esparza

Versión: v3.1.0
"""
# importar librerías necesarias
import yfinance as yf
import matplotlib.pyplot as plt
from tkinter import *
from datetime import datetime
import big_o

def mostrar_porcentaje_perdida(stock):
    """
    Proceso que toma una acción en la bolsa de valores, obtiene su historial de precios de
    cierre en los últimos 12 meses, agrupa los datos por mes, calcula el porcentaje de pérdida
    en relación al precio de cierre inicial, y finalmente, grafica y muestra los porcentajes de
    pérdida en un gráfico.
    Parámetros:
    --------------
    Si, recibe un parámetro "stock" que representa el nombre de una acción en la bolsa de valores.

    Retorna:
    --------------
    No retorna ningún valor.
    """
    # Obtiene el historial de precios de cierre de la acción especificada en el parámetro "stock" en los últimos 12 meses
    historial_acciones = yf.Ticker(stock).history(period='1y')
    # Agrega una columna "mes" con el mes correspondiente a cada fecha en el historial de precios
    historial_acciones['mes'] = historial_acciones.index.to_period('M')
    # Agrupa los datos por mes y selecciona solo el último precio de cierre de cada mes
    agrupado = historial_acciones.groupby('mes').last()
    # Guarda el precio de cierre inicial en una variable
    precio_inicial = agrupado['Close'].iloc[0]
    # Calcula el porcentaje de pérdida en relación al precio de cierre inicial
    porcentajes_perdida = (precio_inicial - agrupado['Close']) / precio_inicial
    # Grafica los porcentajes de pérdida
    porcentajes_perdida.plot()
    # Agrega una etiqueta al eje y del gráfico
    plt.ylabel('Porcentaje de Pérdida')
    # Muestra el gráfico en pantalla
    plt.show()

if __name__ == '__main__':
    # inicializar el programa
    print("********* VERIFICAR OFERTA Y DEMANDA *********")
    # iniciar bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        # Muestra la lista de entradas válidas al usuario
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
        print("Entradas válidas:")
        for name, ticker in simbolos.items():
            print(f"{name} ({ticker})")
        # Crea una ventana principal utilizando la biblioteca Tkinter
        ventana_principal = Tk()
        # Establece el título de la ventana
        ventana_principal.title("Porcentaje de Pérdida")
        # Crea una etiqueta que indica al usuario que ingrese el símbolo de la acción
        etiqueta_accion = Label(ventana_principal, text="Ingresa el símbolo de la acción:")
        # Muestra la etiqueta en la ventana
        etiqueta_accion.pack()
        # Crea un campo de entrada para que el usuario ingrese el símbolo de la acción
        entrada_accion = Entry(ventana_principal)
        # Muestra el campo de entrada en la ventana
        entrada_accion.pack()
        # Crea un botón "Mostrar" que, al ser presionado, ejecuta la función "mostrar_porcentaje_perdida" con el símbolo de la acción ingresado por el usuario
        boton_mostrar = Button(ventana_principal, text="Mostrar", command=lambda: mostrar_porcentaje_perdida(entrada_accion.get()))
        # Muestra el botón en la ventana
        boton_mostrar.pack()
        # Inicia el bucle principal de la ventana
        ventana_principal.mainloop()
        
        # Variable para calcular la complejidad
        com1 = lambda n: entrada_accion
        com2 = lambda m: mostrar_porcentaje_perdida
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