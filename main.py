print("                                                                                         ")
print("                                SAYDER & CO S.A.S                                        ")  
print("                               NIT: 800.123.456-7                                        ")
print("                   AV. El Sol #33 - 90 CC PLAZA NORTE LOCAL 8                            ")
print("                                                                                         ")
print("     -------------------------------------------------------------------------------     ")
print("                                                                                         ")
print("                               FACTURA ELECTRÓNICA                                       ")
print("                              No: F0201-00085230001                                      ")
print("                                                                                         ")
print("                                                                                         ")
print("                                                                                         ")

nombre_cliente = input("Ingrese el nombre del cliente: ")
print("                                                                                         ")
documento_cliente = input("Ingrese el numero de documento del cliente:")
print("                                                                                         ")
print(f"¡Hola {nombre_cliente}! Bienvenido a nuestra tienda. ¿En qué podemos ayudarte hoy?")
print("                                                                                         ")
print("1. Registrar una compra")
print("2. Salir")
print("                                                                                         ")


opcion = input("Seleccione una opción: ")

if opcion == "1":


    print("                                                                                         ")

    print("¡Genial! Vamos a registrar tu compra.")
    
    print("                                                                                         ")


if opcion == "1":

    producto = input("Ingrese el nombre del producto: ")

    print("                                                                                         ")

    cantidad = int(input("Ingrese la cantidad del producto: "))

    print("                                                                                         ")

    precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    
    print("                                                                                         ")
    
    
    print("                                                                                         ")
    
    total = cantidad * precio_unitario
    print(f"El total de tu compra es: {total}")

    """elif opcion == "2":
    
    print("¡Gracias por visitarnos! ¡Hasta luego!")"""""
    




"""total = cantidad * precio_unitario"""










#membresia = input("es cliente con membresia? (si/no):  ")
#if membresia == "si":
#    print("tiene un descuento del 10%")
#    descuento = total * 0.10
#    precio_final = total - descuento
#    print("el precio final es: ", precio_final)
#else:    print("no tiene descuento")#