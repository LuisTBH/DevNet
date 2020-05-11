######################################
#                                    #
# BECA CISCO DEVNET 2020             #
# alumno: Luis García Gómez          #
# email: luisgarciatbh@gmail.com     #
#                                    #
######################################

#1 - Crear un programa que permita conectarse con el controlador APIC-EM de Cisco 
#2 - El usuario tendrá que escoger la opción que quiera (no tendrá que especificar la url a mano)
#3 - Añadir, como mínimo, 4 funcionalidades

import requests
import json
from tabulate import *
from my_apic_em_functions import *


bienvenida = "Bienvenido al programa para manejar el APIC-EM."

print(len(bienvenida)*'=')
print(bienvenida)
print(len(bienvenida)*'=')

# no se han implementado el path trace ni nada de topology porque estaban estas APIS deshabilitadas.
# mande mensaje y deje constancia de foto correspondiente de no existir dichas opciones
# por eso se han buscado otras alternativas viables para ver que el concepto se entiende
fallo = True
#opcion = input("\nEleccion: ")

while(fallo):

    print("\nElija una de estas opciones: \n")
    print("1 - Print Hosts")
    print("2 - Print Devices")
    print("3 - Number of Devices")
    print("4 - All Interfaces")
    print("5 - Tags")
    print("6 - IP Geolocation")
    print("0 - Exit")

    opcion = input("\nEleccion: ")
    print(opcion)
    # de esta forma obligamos a solos digitos y tampoco numeros negativos con el chr - ;)
    if not opcion.isdigit():
        print("Introduce un valor numerico, por favor.")
        #opcion = input("Eleccion: ")
    elif int(opcion) > 6:
        print("Introduce una opción válida, por favor.")
        #opcion = input("Eleccion: ")
    elif int(opcion) == 0:
        print("Hasta pronto. Goodbye. Ciao.\nGracias por usar este script.")
        break
    else:
        opcion = int(opcion)
##        print("OK")
##        print(opcion)
        if opcion == 1: # tb nos serviria poner if opcion: (el True es como un 1 ;))
            print_hosts()
            #fallo = False       

        if opcion == 2: 
            print_devices()
            #fallo = False
        
        if opcion == 3: 
            print_network_devices_count()
            #fallo = False

        if opcion == 4: 
            print_All_interfaces()  #Gets all available interfaces with a maximum limit of 500
            #fallo = False
            
        if opcion == 5: 
            tags()
            #fallo = False
            
        if opcion == 6: 
            location_ip()
            #fallo = False

        
        


        
        

        
    ##get_ticket()
    ##print_hosts()
