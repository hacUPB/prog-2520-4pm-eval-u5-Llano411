#1. abrir el archivo
fp = open("C:\\Users\\aleja\OneDrive\Desktop\\texto_random.txt","r", encoding="utf-8")
#2. leer el archivo
#datos = fp.read(20) 
#datos = fp.read()
#fp.readline()
#fp.readline()
#fp.read(5)
#datos = fp.readline(7)
#3. Cerrar el archivo 

#cadena = "hola"
#cadena[1]

for linea in fp:
    print(linea[0], end="") #para quitar el enter extra 

fp.close()

#print(datos)