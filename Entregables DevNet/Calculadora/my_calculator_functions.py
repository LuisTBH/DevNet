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

    # FUNCION EXPONENCIAL
def exponencial():
    print("EXPONENCIAL --> Introduce el valor y luego el exponente")
    valorExp1 = int(input("Introduce el valor: "))
    valorExp2 = int(input("Introduce el exponent: "))
    expTotal = valorExp1 ** valorExp2
    
    print("Resultado de " + str(valorExp1) + " ** " + str(valorExp2) + " =", expTotal);
        #Hay que controlar la division por zero!!!
    #escape = input("Quieres realizar alguna operación más? (yes or y is acepted)")

    # FUNCION RAIZ
def raiz_cuadrada():
    print("RAIZ CUADRADA--> Introduce el valor: ")
    valorRaiz1 = int(input("Introduce el valor: "))
    
    raizTotal = valorRaiz1 ** (1/2)
    
    print("Resultado de la raiz cuadrada de " + str(valorRaiz1) + " =", raizTotal);
        #Hay que controlar la division por zero!!!



