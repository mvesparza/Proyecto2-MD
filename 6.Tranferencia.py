"""
Programa que sirve para simular tranferencias de dinero de una cuenta a otra.

Autor: Marco Vinicio Esparza

Versión: v2.3.1
"""

import big_o

class CuentaBancaria:
    def __init__(self, nombre, numero_cuenta, saldo):
        """
        Método "init" que se utiliza para inicializar los atributos de una clase cuando se crea una nueva instancia de esa clase.
        Parámetros:
        --------------
        Si, recibe tres argumentos como parámetros: "nombre", "numero_cuenta", y "saldo".

        Retorna:
        --------------
        No retorna ningún valor
        """
        #Asignar valores de argumentos a los atributos de la clase
        self.nombre = nombre
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def transferir(self, destinatario, monto):
        """
        Método de la clase que se utiliza para transferir dinero de una cuenta a otra.
        Parámetros:
        --------------
        Si, recibe dos argumentos:
        destinatario: es una instancia de la clase a la que se transferirá el dinero.
        monto: es el monto a ser transferido.

        Retorna:
        --------------
        No retorna ningún valor
        """
        #Verifica que el saldo actual sea suficiente para la transferencia
        if self.saldo < monto:
            print("Error: fondos insuficientes")
            return
        #Disminuye el saldo de la cuenta actual
        self.saldo -= monto
        #Aumenta el saldo de la cuenta destinataria
        destinatario.saldo += monto
        #Imprime un mensaje de confirmación de la transferencia
        print("Se ha transferido $%.2f de la cuenta %s a la cuenta %s" % (monto, self.numero_cuenta, destinatario.numero_cuenta))

if __name__ == "__main__":
    # inicializar el programa
    print("********* TRANSFERENCIA DE DINERO *********")
    # iniciar bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        # Pedir al usuario que ingrese la información de la cuenta 1
        nombre1 = input("Ingrese el nombre del titular de la cuenta 1: ")
        numero_cuenta1 = input("Ingrese el numero de cuenta 1: ")
        saldo1 = float(1000.37)

        # Pedir al usuario que ingrese la información de la cuenta 2
        nombre2 = input("Ingrese el nombre del titular de la cuenta 2: ")
        numero_cuenta2 = input("Ingrese el numero de cuenta 2: ")
        saldo2 = float(1000.50)

        # Crear las cuentas con la información ingresada
        cuenta1 = CuentaBancaria(nombre1, numero_cuenta1, saldo1)
        cuenta2 = CuentaBancaria(nombre2, numero_cuenta2, saldo2)

        # Pedir al usuario el monto a transferir
        monto = float(input("Ingrese el monto a transferir: "))

        # Realizar la transferencia
        cuenta1.transferir(cuenta2, monto)

        # Mostrar el saldo de cada cuenta
        print("Nuevo saldo de cuenta de", cuenta1.nombre, ":", cuenta1.saldo)
        print("Nuevo saldo de cuenta de", cuenta2.nombre, ":", cuenta2.saldo)

        # Variable para calcular la complejidad
        com1 = lambda n: cuenta1
        com2 = lambda m: cuenta2
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