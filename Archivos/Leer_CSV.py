import csv
humedad= []
temperatura= []
presion = []
with open("C:\\Users\\aleja\\OneDrive\\Desktop\\Variables.csv","r") as csvfile:
    lector = csv.reader(csvfile, delimiter= ';') # metodo reader
    encabezado = next(lector) #next lo que hace es que salta a la siguiente linea o guarda esa linea en una variable 

    for fila in lector:  #se usa un bucle para leer el objeto 
        dato = int(fila[1])
        data = fila[2]
        temp = int(fila [0])
        try:
            data = float(data.replace(",", ".")) #Sirve para cambiar una cadena de caracteres por otra o un caracter por otro 
        except:
            print("Dato no encontrado")
            data = 0.0
        humedad.append(dato) 
        presion.append(data)
        temperatura.append(temp)
        
print(encabezado[0])
print(temperatura)
print(encabezado[1])
print(humedad)
print(encabezado[2])
print(presion)

# La funcion seek sirve para ubicar el puntero del archivo en una posicion especifica del archivo 