try:
    num=int(input("Ingrese un numero: "))
    print(1/num)
except ZeroDivisionError:
    print("No puedes dividir entre cero duhhhh")
except ValueError: 
    print("Que parte de numero no entendiste????")
except Exception as e: 
    print(f"Ocurrio un error de tipo {e}")
finally:
    print('Ya le sabes al "Try"...... espero')