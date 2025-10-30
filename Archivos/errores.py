try:
    entero=int(input("ingrese un numero: "))
except ValueError: 
    print("Eso no es un numero")
else:
    print("la operacion se realizo correctamente")
finally: 
    print("Puedes continuar")