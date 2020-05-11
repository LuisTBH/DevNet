######################################
#                                    #
# BECA CISCO DEVNET 2020             #
# alumno: Luis García Gómez          #
# email: luisgarciatbh@gmail.com     #
#                                    #
######################################

# Crear un script que permita conectarnos a nuestro Router CSR1000v y que, a través de un menú,
# nos aparezcan una serie de opciones que nos permita realizar las siguientes tareas:
    # 1 - Conectar a CSR1kv
    # 2 - Menú para elegir la opción
    # 3 - Obtener listado interfaces router
    # 4 - Crear interfaces
    # 5 - Borrar interfaces
    # 6 - Obtener tabla de routing
    # 7 - Implementar 2 peticiones diferentes a YANG


import json
from tabulate import *
from netmiko import ConnectHandler
from my_csr1kv_functions import *



sshCli = get_conecction()
##get_interfaces_list(sshCli)
### send some simple "exec" commands and display the returned output
##print("Sending 'sh ip int brief'.")
##output = sshCli.send_command("show ip int brief")
##print(output)
###Si hay varios dispositivos usamos esta forma
##print("show ip int brief:\n{}\n".format(output))


bienvenida = "Bienvenido al programa para manejar el Router CSR100kv."

print(len(bienvenida)*'=')
print(bienvenida)
print(len(bienvenida)*'=')


fallo = True
#opcion = input("\nEleccion: ")

while(fallo):
###### No se si me gusta mas de esta forma o como esta hecho.
##    bienvenida = "Bienvenido al programa para manejar el Router CSR100kv."
##
##    print(len(bienvenida)*'=')
##    print(bienvenida)
##    print(len(bienvenida)*'=')
##    print()

    print("\nElija una de estas opciones: \n")
    print(" 1 - Listado Interfaces (CLI)")
    print(" 2 - Listado Interfaces (RESTCONF)")
    print(" 3 - Crear Interface (CLI con netmiko)")
    print(" 4 - Crear | Modificar Interface (RESTCONF)")     # Tb sirve para modificar
    print(" 5 - Borrar Interface (RESTCONF)")
    print(" 6 - Lista de Capacidades (NETCONF)")
    print(" 7 - Estadisticas de Interfaces (NETCONF)")
    print(" 8 - Tabla de Routing")    
    print(" 9 - Configuracion en ejecución")
    print("10 - Tabla ARP")
    print(" 0 - Exit")

    opcion = input("\nEleccion: ")
    
    # de esta forma obligamos a solos digitos y tampoco numeros negativos con el chr - ;)
    if not opcion.isdigit():
        print("Introduzca un valor numerico, por favor.")
        #opcion = input("Eleccion: ")        
    elif int(opcion) > 10:
        print("Introduzca una opción válida, por favor.")
        #opcion = input("Eleccion: ")
    elif int(opcion) == 0:
        print("Hasta pronto. Goodbye. Ciao.\nGracias por usar este script.")
        break
    else:
        opcion = int(opcion)

        if opcion == 1: # tb nos serviria poner if opcion: (el True es como un 1 ;))
            get_interface_list_table(sshCli)
            print()
            get_interfaces_list(sshCli)           
            #fallo = False       

        if opcion == 2: 
            get_interfaces_restconf()
            #fallo = False
        
        if opcion == 3: 
            create_interface(sshCli)
            #fallo = False

        if opcion == 4: 
            create_interface_restconf()  
            #fallo = False
            
        if opcion == 5: 
            delete_interface_restconf()
            #fallo = False

        if opcion == 6: 
            list_capabilities()
            #fallo = False
            
        if opcion == 7:
            get_interface_stats(sshCli)            
            #fallo = False

        if opcion == 8:
            get_routing_table(sshCli)            

        if opcion == 9: 
            get_interfaces_netconf()

        if opcion == 10:            
            show_ARP_table(sshCli)

