fichero = open("C:\\Users\\aleja\OneDrive\Desktop\\texto.txt","r")
linea = fichero.readline()
print(linea)
linea = fichero.readline()
print(linea)
linea = fichero.readlines() #Crea una lista con todas las lineas de el archivo 
print(linea)
fichero.close()

'''
Responde las siguientes preguntas:

1. ¿Por qué es importante utilizar el método `close()`?
'''