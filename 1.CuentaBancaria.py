"""
Programa que permite crear una cuenta en la empresa "Invierte Fácil EC", ingresadno el nombre,
cédula, edad y opcionalmente un depósito en dólares.

Autor: Marco Vinicio Esparza

Versión: v3.3.8
"""
# importar librerías necesarias
import random
import big_o

class CuentaInvierteFacilEC:
    
    cuentas = []

    def __init__(self):
        """
        Función que se encarga de inicializar las variables de instancia de una clase en vacío
        o cero, y se ejecuta automáticamente cuando se crea una nueva instancia de esta clase.
        Parámetros:
        --------------
        Si, recibe la referencia al objeto actual implícitamente, conocido como self.

        Retorna:
        --------------
        No retorna ningún valor.
        """
        # Nombre del usuario
        self.nombre = ""
        # Número de cédula del usuario
        self.cedula = ""
        # Edad del usuario
        self.edad = 0
        # Saldo actual del usuario
        self.saldo = 0

    def crear_cuenta(self):
        """
        Proceso que permite a un usuario crear una cuenta ingresando su nombre, cédula y edad.
        Luego valida si la cuenta es válida y si es así, se agrega a una lista de cuentas y se
        imprime un mensaje de éxito. Si no es válida, se imprime un mensaje indicando que no
        se pudo crear la cuenta.
        Parámetros:
        --------------
        Si, recibe como parámetro self que hace referencia al objeto de la clase actual.

        Retorna:
        --------------
        No retorna ningún valor ya que su función es modificar el estado del objeto.
        """
        # Ingreso del nombre del usuario
        self.nombre = input("Ingrese su nombre: ")
        # Ingreso de la cédula (verificando que sea de 10 caracteres)
        while len(self.cedula) != 10:
            self.cedula = input("Ingrese su cédula (10 caracteres): ")
        # Ingreso de la edad del usuario
        self.edad = int(input("Ingrese su edad: "))
        # Validación de la cuenta
        if self.validar_cuenta():
            print("La cuenta se ha creado exitosamente!")
            # Agregar la cuenta a la lista de cuentas
            self.__class__.cuentas.append(self)
        else:
            print("No se pudo crear la cuenta.")
        # Realizar una transacción
        self.realizar_transaccion()

    def validar_cuenta(self):
        """
        Proceso que verifica si los datos ingresados para crear una cuenta son válidos.
        Parámetros:
        --------------
        Si, recibe como parámetro self que hace referencia al objeto de la clase actual.

        Retorna:
        --------------
        Si, retorna un valor booleano, True si la cuenta es válida y False si no lo es.
        """
        # Verificar que el nombre no esté vacío y que la edad sea mayor a 18
        if len(self.nombre) == 0 or self.edad < 18:
            return False
        # Si se cumplen las condiciones, la cuenta es válida
        else:
            return True

    # Método para ver las cuentas existentes
    @classmethod
    def ver_cuentas(cls):
        """
        Proceso que permite ver una lista de cuentas existentes.
        Parámetros:
        --------------
        Si, recibe como parámetro cls que hace referencia a la clase actual

        Retorna:
        --------------
        No, retorna ningún valor.
        """
        # Generar un número aleatorio de cuenta
        num = [1,2,3,4,5,6,7,8,9,0]
        # Recorrer cada cuenta en la lista de cuentas
        for cuenta in cls.cuentas:
            # Imprimir la información de la cuenta
            print(f"Número de Cuenta: {''.join(str(i) for i in random.sample(num, 8))}, Nombre: {cuenta.nombre}, Cédula: {cuenta.cedula}, Edad: {cuenta.edad}, Saldo: {cuenta.saldo}")

    def realizar_transaccion(self):
        """
        Proceso que permite al usuario realizar una transacción en su cuenta, en este caso, depositar dinero.
        Parámetros:
        --------------
        Si, recibe como parámetro cls que hace referencia a la clase actual

        Retorna:
        --------------
        No, retorna ningún valor.
        """
        # Preguntar si se desea depositar dinero
        transaccion = input("¿Desea depositar dinero? (si/no): ")
        # Si se desea depositar
        if transaccion == 'si':
            # Ingresar el monto a depositar
            monto = float(input("Ingrese el monto a depositar: "))
            # Aumentar el saldo de la cuenta
            self.saldo += monto
            # Mostrar el nuevo saldo
            print(f"Deposito realizado. Nuevo saldo: {self.saldo}")
        # Si no se desea depositar
        else:
            # Mostrar un mensaje de que no se realizó ninguna transacción
            print("No se realizó ninguna transacción.")

if __name__ == '__main__':
    # inicializar el programa
    print("********* CUENTA INVIERTE FÁCIL EC *********")
    # iniciar bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        while True:
            # declarar una variable global
            cuenta = CuentaInvierteFacilEC()
            cuentacreada = cuenta.crear_cuenta()
            nuevo_usuario = input("¿Desea ingresar a otro usuario? (si/no): ")
            if nuevo_usuario == 'no':
                break
        ver_db = input("¿Desea ver la base de datos de cuentas? (si/no): ")
        if ver_db == 'si':
            CuentaInvierteFacilEC.ver_cuentas()
        
        # Variable para calcular la complejidad
        com1 = lambda n: cuenta
        com2 = lambda m: cuentacreada
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