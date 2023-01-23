"""
Programa que sirve para validar compras de acciones.

Autor: Marco Vinicio Esparza

Versión: v2.1.3
"""

import big_o

# lista con productos disponibles
productos = [
    {"Símbolo Acción": "AAPL", "precio": 137870.0, "marca": "Apple Inc."},
    {"Símbolo Acción": "GOOG", "precio": 99280.0, "marca": "Google Inc."},
    {"Símbolo Acción": "AMZN", "precio": 97250.0, "marca": "Amazon.com Inc."},
    {"Símbolo Acción": "TSLA", "precio": 133420.0, "marca": "Tesla Inc."},
    {"Símbolo Acción": "MSFT", "precio": 240220.0, "marca": "Microsoft Corp."},
    {"Símbolo Acción": "KO", "precio": 60080.0, "marca": "Coca-Cola Co."},
    {"Símbolo Acción": "PFE", "precio": 45110.0, "marca": "Pfizer Inc."},
    {"Símbolo Acción": "DIS", "precio": 103480.0, "marca": "Walt Disney Co."},
    {"Símbolo Acción": "PG", "precio": 142970.0, "marca": "Procter & Gamble Co."},
    {"Símbolo Acción": "IBM", "precio": 141200.0, "marca": "IBM Corporation"},
    {"Símbolo Acción": "GE", "precio": 77680.0, "marca": "General Electric Co."},
    {"Símbolo Acción": "T", "precio": 19230.0, "marca": "AT&T Inc."},
    {"Símbolo Acción": "WMT", "precio": 140540.0, "marca": "Walmart Inc."},
    {"Símbolo Acción": "CVX", "precio": 180900.0, "marca": "Chevron Corporation"},
    {"Símbolo Acción": "HD", "precio": 315000.0, "marca": "The Home Depot, Inc."},
    {"Símbolo Acción": "BA", "precio": 206760.0, "marca": "Boeing Co."},
    {"Símbolo Acción": "CAT", "precio": 249710.0, "marca": "Caterpillar Inc."},
    {"Símbolo Acción": "DOW", "precio": 57440.0, "marca": "Dow Inc."},
    {"Símbolo Acción": "XOM", "precio": 113350.0, "marca": "Exxon Mobil Corporation"}
]

compras_realizadas = []

def validar_compra(producto, lugar, dinero):
    """
    Proceso que que valida si una compra es válida o no.
    Parámetros:
    --------------
    Si, recibe tres parámetros.
    producto: Es una cadena de texto que representa el producto que se desea comprar, se asume que el producto es una acción de una empresa.
    lugar: Es una cadena de texto que representa el lugar donde se desea realizar la compra, puede ser "Tienda en línea" o "Tienda física".
    dinero: Es un número decimal que representa el dinero que se tiene disponible para realizar la compra.

    Retorna:
    --------------
    Si, retorna una cadena de texto que indica el resultado de la compra.
    """
    # Lista de lugares permitidos
    lugares_permitidos = ["Tienda en línea", "Tienda física"]
    #precio del producto
    precio = 0

    # Validar que el producto existe en nuestra base de datos
    producto_existe = False
    for p in productos:
        if p['Símbolo Acción'] == producto:
            precio = p["precio"]
            producto_existe = True
            break
    if not producto_existe:
        return "Producto no válido"

    # Validar que el lugar de compra está en la lista de lugares permitidos
    if lugar not in lugares_permitidos:
        return "Lugar de compra no válido"

    # validar que el dinero es suficiente
    numA = int(input("Ingrese en numero de acciones a comprar: ")) 
    if dinero < (precio*numA):
        return "Dinero insuficiente"
    
    saldo = dinero - (precio*numA)
    # Si pasa todas las validaciones, se confirma la compra
    compras_realizadas.append({"producto": producto, "lugar": lugar, "precio $": (precio*numA)})
    return f"Compra confirmada, su saldo es {saldo} "

if __name__ == "__main__":
    # inicializar el programa
    print("********* COMPRA DE ACCIONES *********")
    # iniciar bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        while True:
            #Solicita al usuario el nombre del producto a comprar
            producto = input("Ingrese el nombre del producto: ")
            #Solicita al usuario el lugar de compra
            lugar = input("Ingrese el lugar de compra, las acciones se disponen en Tienda física o Tienda en línea: ")
            #Solicita al usuario cuanto dinero tiene y lo convierte a flotante
            dinero = float(input("Ingrese cuanto dinero tiene: "))
            #llama a la funcion validar_compra con los parametros de producto, lugar y dinero
            resultado = validar_compra(producto, lugar, dinero)
            #Imprime el resultado de la funcion validar_compra
            print(resultado)
            #solicita al usuario si quiere realizar otra compra
            otra_compra = input("Desea realizar otra compra? (si/no)")
            #si el usuario ingresa "no" termina el bucle
            if otra_compra.lower() == "no":
                break
        print("Registro de compras:")
        for compra in compras_realizadas:
            print(compra)
        
        # Variable para calcular la complejidad
        com1 = lambda n: validar_compra
        com2 = lambda m: resultado
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