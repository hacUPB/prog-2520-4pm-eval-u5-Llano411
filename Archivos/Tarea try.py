try:
    num=int(input("Ingrese un numero: "))
    print(1/num)
except ZeroDivisionError:
    print("No puedes dividir en tre cero duhhhh")
except ValueError: 
    print("Que parte de numero no entendiste????")
except Exception: 
    print("Algo salio mal..... no se el que")
finally:
    print('Ya le sabes al "Try"...... espero')