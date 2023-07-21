# CALCULADORA V.3 - prueba
#Sumar
import asyncio
def suma () :
    print("Cuando ya no desees sumar más pon un ( = ) ")
    c = 0
    cantidad = True
    while cantidad :
        a = input("{ ")
        if a != "=" :
            c += int(a)
        else :
            cantidad = False
    print(f"El resultado de la suma es {c}")
#Restar
def resta () :
    print("Cuando ya no desees restar más pon un ( = ) ")
    c = input("{ ")
    cantidad = True
    while cantidad :
        a = input("{ ")
        if a != "=" :
            c = float(c)
            c -= float(a)            
        else :
            cantidad = False
    print(f"El resultado de la resta es {c} ")
#multiplicar
def multiplicacion () :
    print("Cuando ya no desees multiplicar más pon un ( = ) ")
    c = input("{ ")
    cantidad = True
    while cantidad :
        a = input("{ ")
        if a != "=" :
            c = float(c)
            c = c * float(a)            
        else :
            cantidad = False
    print(f"El resultado de la multiplicacion es  {c} ")
#Dividir
def division () :
    print("Cuando ya no desees dividir más pon un ( 0 ) ")
    c = int(input("{ "))
    cantidad = True
    while cantidad :
        a = int(input("{ "))
        if not a == 0 and not c == 0 :
            c = float(c)
            c = c / float(a)            
        else :
            cantidad = False
    print(f"El resultado de la division es {c} ")
async def espera():
    print('Espere\n')
    await asyncio.sleep(3)
    print('Hecho')

#peticion
p = input("Suma(+), Resta(-),Multiplicacion(*), Division(/)            Ingrese el simbolo de la operación que desea realizar: ") 
while p != "+" and p != "-" and p != "*" and p != "/" :
    p = input("Suma(+), Resta(-),Multiplicacion(*), Division(/)            Ingrese el simbolo de la operación que desea realizar: ") 
if p == "+":
    suma()
if p == "-":
    resta()
if p == "*":
    multiplicacion()
if p == "/":
    division()
print()
asyncio.run(espera())

# Hecho