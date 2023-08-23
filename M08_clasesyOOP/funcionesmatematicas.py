class Funcionesmatematicas:

    def __init__(self,listadonumeros): 
        self.listado=listadonumeros

    #función que verifica dentro de la lista si un número es primo

    def verifica_si_es_primo(self):
        for i in self.listado:
            if (self.__verifica_si_es_primo(i)):
                print (i,"es un número primo")
            else:
                print (i,"no es un número primo")

    # función que convierte los grados del listado de números asignado

    def calcular_temperatura(self,medida_origen,medida_destino):
        for i in self.listado:
            print(i,"grados",medida_origen,"equivale a:",self.__calcular_temperatura(i,medida_origen,medida_destino),"grados",medida_destino)

    # función que calcula el factorial del listado asignado
            
    def factorial(self):
        for i in self.listado:
            print("el factorial de",i,"es",self.__factorial(i))

    #demás funciones
            
    def __verifica_si_es_primo(self,numero):
        primo=True
        for i in range(2,numero):
            if numero%i==0:
                primo=False
                break
        return primo

    # función que verifica el modal

    def valor_modal(self):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.listado) == 0:
            return None
        for elemento in self.listado:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo

    # función que convierte los grados

    def __calcular_temperatura(self,valor,medida_origen,medida_destino):
        if medida_origen=="C"  and medida_destino=="F":
            conversion=(valor*9/5)+32
            print(valor,"C equivale a", conversion,"F")
        elif medida_origen=="C" and medida_destino=="K":
            conversion=valor+273.15
            print(valor,"C equivale a", conversion,"K")
        elif medida_origen=="F" and medida_destino=="C":
            conversion=(valor-32)*5/9
            print(valor,"F equivale a", conversion,"C")
        elif medida_origen=="F" and medida_destino=="K":
            conversion=((valor-32)*5/9)+273.15
            print(valor,"F equivale a", conversion,"K")
        elif medida_origen=="K" and medida_destino=="C":
            conversion=valor-273.15
            print(valor,"K equivale a", conversion,"C")
        elif medida_origen=="K" and medida_destino=="F":
            conversion=((valor-273.15)*9/5)+32
            print(valor,"K equivale a", conversion,"F")
        elif medida_origen==medida_destino:
            print("se ha ingresado el mismo tipo de medida origen y medida destino, por lo tanto no se puede procesar la conversión")
        else:
            print("no se ha ingresado datos válidos para realizar la conversión, recuerda usar para gardos celsius:C, para grados Farenheit:F y para grados Kelvin:K")


    # función factorial
            
    def __factorial(self,n):
        if (type(n) == int):
            if (n > 0):
                factorial = n
                while (n > 2):
                    n = n - 1
                    factorial = factorial * n
                print('El factorial es', factorial)
            else:
                print('La variable no es mayor a cero')
        else:
            print('La variable no es un entero')