"""
Programa que sirve para simular un fondo de inversiones.

Autor: Marco Vinicio Esparza

Versión: v3.1.1
"""

import random
import big_o

class FondoDeInversion:
    def __init__(self, activos, precio_unitario):
        """
        Proceso que inicializa un nuevo fondo de inversión con una lista de activos y un precio unitario inicial.
        Parámetros:
        --------------
        Si, recibe dos parámetros.
        activos: es una lista de los activos en los que el fondo ha invertido.
        precio_unitario: es un valor numérico que representa el precio de una unidad de participación del fondo.

        Retorna:
        --------------
        No retorna ningún valor
        """
        #La lista de activos en los que el fondo ha invertido.
        self.activos =activos   
        #El precio de una unidad de participación del fondo.
        self.precio_unitario = precio_unitario  
        #El número de unidades de participación del fondo que han sido emitidas y están en manos de los inversionistas.
        self.unidades_circulacion = 0   

    def comprar_unidades(self, cantidad):
        """
        Proceso que permite comprar unidades de participación en el fondo.
        Parámetros:
        --------------
        Si, recibe un parámetro cantidad que representa el número de unidades que el usuario desea comprar.

        Retorna:
        --------------
        No retorna ningún valor
        """
        # Suma la cantidad de unidades compradas a la cantidad de unidades en circulación del fondo
        self.unidades_circulacion += cantidad  
        # Calcula el costo de la compra multiplicando el precio unitario del fondo por la cantidad de unidades compradas
        costo = self.precio_unitario * cantidad  
        # Imprime un mensaje informando al usuario de la cantidad de unidades compradas y el costo total de la compra
        print(f"Has comprado {cantidad} unidades por un costo de {costo}") 

    def vender_unidades(self, cantidad):
        """
        Proceso que permite vender unidades de participación en el fondo.
        Parámetros:
        --------------
        Si, recibe un parámetro cantidad que representa el número de unidades que el usuario desea vender.

        Retorna:
        --------------
        No retorna ningún valor
        """
        # Revisa si el usuario tiene suficientes unidades para vender
        if cantidad > self.unidades_circulacion: 
            print("No tienes suficientes unidades para vender")
            # Si no tiene suficientes unidades para vender, termina la ejecución de la función
            return  
        # Resta la cantidad de unidades vendidas a la cantidad de unidades en circulación del fondo
        self.unidades_circulacion -= cantidad  
        # Calcula el costo de la venta multiplicando el precio unitario del fondo por la cantidad de unidades vendidas
        costo = self.precio_unitario * cantidad  
        # Imprime un mensaje informando al usuario de la cantidad de unidades vendidas y el costo total de la venta
        print(f"Has vendido {cantidad} unidades por un costo de {costo}")  

    def simular_rendimiento(self):
        """
        Proceso que simula un rendimiento aleatorio para el fondo.
        Parámetros:
        --------------
        No recibe ningún valor

        Retorna:
        --------------
        No retorna ningún valor
        """
        # Genera un número aleatorio entre -0.1 y 0.1 para simular el rendimiento del fondo
        rendimiento = random.uniform(-0.1, 0.1) 
        # Actualiza el precio unitario del fondo multiplicándolo por el rendimiento más 1
        self.precio_unitario *= 1 + rendimiento  
        # Imprime un mensaje informando al usuario del rendimiento del fondo en porcentaje
        print(f"El rendimiento del fondo ha sido de {rendimiento*100} %") 

if __name__ == "__main__":
    # inicializar el programa
    print("********* FONDO DE INVERSIONES *********")
    # iniciar bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        fondo = FondoDeInversion(["Acciones"], 10)
        while True:
            try:
                accion = input("Que deseas hacer? (comprar, vender, salir): ")
                if accion.lower() == "comprar":
                    cantidad = int(input("Cuantas unidades deseas comprar?: "))
                    fondo.comprar_unidades(cantidad)
                elif accion.lower() == "vender":
                    cantidad = int(input("Cuantas unidades deseas vender?: "))
                    fondo.vender_unidades(cantidad)
                elif accion.lower() == "salir":
                    break
                else:
                    print("Acción no valida")
                fondo.simular_rendimiento()
            except ValueError:
                print("Ingresa un valor numérico válido")
        
        # Variable para calcular la complejidad
        com1 = lambda n: fondo
        com2 = lambda m: accion
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