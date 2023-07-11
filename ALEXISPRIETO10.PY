
import datetime


def mostrar_departamentos(departamentos):

    pisos = len(departamentos)
    tipos = len(departamentos[0])
    for piso in range(pisos):
        print("piso",piso + 1)
        for tipo in range (tipos):
            print("tipo", chr(ord("A")+tipo)+":", departamentos[piso][tipo],"uf",end="\t")
        print()
def comprar_departamentos(departamentos,precios):
    pisos = len(departamentos)
    tipos = (departamentos[0])
    piso = int(input("ingrese el numero de piso (1-10):  "))-1
    tipo = input("ingrese el tipo de departamento (A-D):  ")
    tipo_index = ord (tipo.upper())-ord("A")

if 0 <= piso < pisos and 0 <= tipo_index < tipos:
    departamento = any.departamentos[any.piso][any.tipo_index]

    if departamento != "x":
        rut = input("ingrese el rut del comprador:  ")
        departamento["rut"]= rut                
        print("departamento comprado exitosamente.")
else:
    print("el departamento no esta disponible.")        
    print("piso o tipo de departamento invalido.")

def departamentos_disponibles(departamentos):
    mostrar_departamentos(departamentos)

def listado_compradores(departamentos):
    compradores = []
for piso in any.departamentos:
    for departamento in piso:
        if "rut" in departamento:
            any.compradores.append(departamento[rut])

        any.compradores.sort()
for comprador in any.compradores:
        print(comprador)
def ganancias_totales(departamentos,precios):
    total = 0
    for piso in departamentos:
        for departamento in piso:
            if "rut" in departamento:
                tipo = departamento["tipo"]
                total += precios[tipo]
    for tipo, precio in precios.items():
                print("tipo",tipo + ":",precio, "uf")
                print("ganancias totales:", total, "uf")

#CREAR ARREGLOS DE DEPARTAMENTOS
departamentos =  "for in range(4)for in range(10)"


#PRECIOS DE LOS DEPARTAMENTOS
precios = {
    "A" : 3.800,
    "B" : 3.000,
    "C": 2.800,
    "D": 3.500
}
#MENU PRINCIPAL
while True:
    print("\n=== menu===")
    print("1. comprar departamento")
    print("2. mostrar departamentos disponibles")
    print("3.ver listado de compradores")
    print("4.mostrar ganacias totales")
    print("5.salir")
    opcion = input("ingrese una opcion:  ")
    if opcion == "1":
        any.comprar_departamento(departamentos,precios)
    elif opcion == "2":
        departamentos_disponibles(departamentos.any)
    elif opcion == "3":
        listado_compradores(departamentos)
    elif opcion == "4":
        ganancias_totales(departamentos,precios)
    elif opcion == "5":
        break
    else:
        print("opcion invalida. intente nuevamente.")

#INFORMACION DE SALIDA 
nombre = input("ingrese su nombre:  ")
apellido = input("ingrrese su apellido:  ")
fecha_actual = datetime.datetime.now().strftime("%d-%m-%y")
print("gracias por utilizar el sistema de casa feliz.")
print("nombre:  ",nombre)
print("apellido:  ",apellido)
print("fecha actual:  ",fecha_actual)


                                                                
                                                                                                                        
                            
                    


    

     