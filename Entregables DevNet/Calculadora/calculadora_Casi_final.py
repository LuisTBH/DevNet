
######################################
#                                    #
# BECA CISCO DEVNET 2020             #
# alumno: Luis García Gómez          #
# email: luisgarciatbh@gmail.com     #
#                                    #
######################################

# Calculadora en Python
from my_calculator_functions import *

print("\n" + "="*35 + " CURSO DEVNET CISCO 2020 " + "="*35 + "\n")
print("*"*96)
print("*  BIENVENIDO A LA CALCULADORA EN PYTHON DE LUIS GARCIA GOMEZ PARA DEVNET DE CISCO 20/01/2020  *");
print("*"*96);
###EL MENU HAY QUE PONERLO EN UNA FUNCION Y HACER UN WHILE(TRUE) PARA QUE SEA EL MENU PRINCIPAL CON UN EXIT()
##print("\nElige la opcion de calculo que quieres usar (por el momento solo estan disponibles las funciones\nbásicas: Sumar, Restar, Multiplicar y Dividir):\n");
##print("1-) SUMAR")
##print("2-) RESTAR")
##print("3-) MULTIPLICAR")
##print("4-) DIVIDIR\n")
##print("0-) SALIR\n")
##opcion = int(input("OPERACION ELEGIDA: ")); #CUALQUIER OTRA COSA DEBERIA DAR ERROR Y REINICIAR EL PROCESO, FATLTA HACER ESA EXCEPCIÓN O CONTROL
escape=True

while(escape): 

    print("\nElige la opcion de calculo que quieres usar: \n");
    print("1-) SUMAR")
    print("2-) RESTAR")
    print("3-) MULTIPLICAR")
    print("4-) DIVIDIR")
    print("5-) EXPONENCIAL")
    print("6-) RAIZ CUADRADA")
    print("0-) SALIR\n")
    

    opcion = input("\nEleccion: ")
    
    # de esta forma obligamos a solos digitos y tampoco numeros negativos con el chr - ;)
    if not opcion.isdigit():
        print("Introduzca un valor numerico, por favor.")
        #opcion = input("Eleccion: ")        
    elif int(opcion) > 10:
        print("Introduzca una opción válida, por favor.")
        #opcion = input("Eleccion: ")
    elif int(opcion) == 0:
        print("Hasta pronto. Goodbye. Ciao.\nGracias por usar este la calculadora.")
        break
    else:
        opcion = int(opcion)

        if opcion == 1: # tb nos serviria poner if opcion: (el True es como un 1 ;))
        
            sumar()           
            #fallo = False       

        if opcion == 2: 
            restar()
            #fallo = False
        
        if opcion == 3: 
            multiplicar()
            #fallo = False

        if opcion == 4: 
            dividir()  
            #fallo = False
            
        if opcion == 5: 
            exponencial()
            #fallo = False

        if opcion == 6: 
            raiz_cuadrada()
            #fallo = False
            
        if opcion == 7:
            get_interface_stats(sshCli)            
            #fallo = False

        if opcion == 8:
            get_routing_table(sshCli)            

        if opcion == 9: 
            get_interfaces_netconf()









    
    
##    opcion = int(input("OPERACION ELEGIDA: ")); #CUALQUIER OTRA COSA DEBERIA DAR ERROR Y REINICIAR EL PROCESO, FATLTA HACER ESA EXCEPCIÓN O CONTROL
##    if int(opcion) == 0:
##        escape=False




#FUNCION SUMAR
def sumar():
    print("SUMA --> Introduce los 2 valores a sumar")
    valorSuma1 = int(input("Introduce el primer valor a sumar: "))
    valorSuma2 = int(input("Introduce el segundo valor a sumar: "))
    sumaTotal = valorSuma1 + valorSuma2
    print("Resultado de " + str(valorSuma1) + " + " + str(valorSuma2) + " = " + str(sumaTotal));
    #escape = input("Quieres realizar alguna operación más? (yes or y is acepted)")


#FUNCION RESTAR
def restar():
    print("RESTA --> Introduce los 2 valores a restar")
    valorResta1 = int(input("Introduce el primer valor a restar: "))
    valorResta2 = int(input("Introduce el segundo valor a restar: "))
    RestaTotal = valorResta1 - valorResta2
    print("Resultado de " + str(valorResta1) + " - " + str(valorResta2) + " = " + str(RestaTotal));
    #escape = input("Quieres realizar alguna operación más? (yes or y is acepted)")    

#FUNCION MULTIPLICAR
def multiplicar():
   print("MULTIPLICACION --> Introduce los 2 valores a multiplicar")
   valorMultiplicacion1 = int(input("Introduce el primer valor a multiplicar: "))
   valorMultiplicacion2 = int(input("Introduce el segundo valor a multiplicar: "))
   MultiplicacionTotal = valorMultiplicacion1 * valorMultiplicacion2
   print("Resultado de " + str(valorMultiplicacion1) + " * " + str(valorMultiplicacion2) + " = " + str(MultiplicacionTotal));
   #escape = input("Quieres realizar alguna operación más? (yes or y is acepted)")

# FUNCION DIVIDIR
def dividir():
    print("DIVISIÓN --> Introduce el dividendo y el divisor (NOTA: No dividir por zero sin execepciones ni control)")
    valorDivision1 = int(input("Introduce el dividendo: "))
    valorDivision2 = int(input("Introduce el divisor: "))
    DivisionTotal = valorDivision1 / valorDivision2
    DivisionTotalEntera = int(valorDivision1 / valorDivision2)
    print("Resultado de " + str(valorDivision1) + " / " + str(valorDivision2) + " forma decimal = " + str(DivisionTotal));
    print("Resultado de " + str(valorDivision1) + " / " + str(valorDivision2) + " forma entera = " + str(DivisionTotalEntera));
    #Hay que controlar la division por zero!!!
    #escape = input("Quieres realizar alguna operación más? (yes or y is acepted)")

