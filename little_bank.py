import time
cuenta ={
    "Nombre" : "JUAN",
    "Cantidad" : 500,
    "dep_max" : 5000,
    "ret_max" : 2000,
    "transf_max" : 2500
}


def depositar():
    cantidad_dep = int(input("Ingresa la cantidad a depositar:\n"))
    if cantidad_dep < cuenta["dep_max"]:
        for _ in range(5):
            time.sleep(0.7)
            print(".", end=" ", flush=True)
        cuenta["Cantidad"] = cantidad_dep + cuenta["Cantidad"]
        print( f"\nTu nuevo saldo es {cuenta['Cantidad']}")
    else:
        raise ValueError("No se puede depositar este monto") 


def retirar():
    cantidad_ret = int(input("Ingresa la cantidad a retirar:\n"))
    if cantidad_ret > cuenta["Cantidad"]:
        raise ValueError("El retiro supera tu monto maximo")
    else:
        if cantidad_ret < cuenta["ret_max"]:
            for _ in range(5):
                time.sleep(0.7)
                print(".", end=" ", flush=True)
            cuenta["Cantidad"] = cuenta["Cantidad"] - cantidad_ret
            print( f"\nTu nuevo saldo es ${cuenta['Cantidad']}MXN")
        else:
            raise ValueError(f"No se puede retirar este monto, intenta un monto mas pequeño, la cantidad maxima es de {cuenta['ret_max']}")

def ver_saldo():
    if cuenta["Cantidad"] < 100:
        print("Revisando saldo:\n\n")
        for _ in range(5):
            time.sleep(0.7)
            print(".", end=" ", flush=True)
        print("\nTu saldo es menor a 100")
        print( f"\n ${cuenta["Cantidad"]}MXN")
    else:
        print("Revisando saldo:\n\n")
        for _ in range(5):
            time.sleep(0.9)
            print(".", end=" ", flush=True)
        print( f"\nTu saldo es:\n ${cuenta["Cantidad"]}MXN")


def transferir():
    cant_transf = int(input("Ingresa la cantidad que quieres transferir:\n"))
    if cant_transf < cuenta["transf_max"]:
        if cant_transf < cuenta["Cantidad"]:
            CLABE = str(input("Ingresa la cuenta CLABE:\n"))
            if len(CLABE) == 16:
                beneficiario = input("Escribe el nombre del beneficiario:\n")
                print(f"La cantidad de ${cant_transf} ha sido enviada exitosamente a {beneficiario}")
                cuenta["Cantidad"] = cuenta["Cantidad"] - cant_transf
                print(f"Tu nuevo saldo es\n {cuenta['Cantidad']}")
            else:
                raise ValueError("La CLABE debe de tener 16 dígitos, intente nuevamente")
        else: 
            raise ValueError("Fondos insuficientes. Deposite para poder transferir")
    else:
        raise ValueError(f"Intenta con una cantidad mas pequeña, la cantidad maxima de transferencia es {cuenta["transf_max"]}")

def login():
    nombre = input("Bienvenido, escribe tu nombre:\n")
    if nombre.upper() == cuenta["Nombre"]:
        print ("Bienvenido", cuenta["Nombre"].upper())

        while True:
            print ("Selecciona una opcion")
            print("1. Depositar")
            print("2. Retirar")
            print("3. Ver saldo")
            print("4. Transferir a otra cuenta")
            print("Salir")
            op = int(input())
            if op == 1:
                depositar()
            elif op == 2:
                retirar()
            elif op == 3:
                ver_saldo()
            elif op == 4:
                transferir()
            else:
                break

    else:
        raise ValueError("Usuario incorrecto")

__name__ = login()




