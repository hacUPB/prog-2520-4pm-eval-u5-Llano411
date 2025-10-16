fp = open("C:\\Users\\aleja\OneDrive\Desktop\\texto.txt","r")
datos = fp.read(5)
print(datos)
datos = fp.read(5)
print(datos)
fp.close() 

'''
Responde las siguientes preguntas:

1. ¿Cuál es la diferencia entre la primera y la segunda llamada al método `read()`? R// El primero lee hasta el caracter 5 y luego sigue a partir de ahi 
2. ¿Por qué no se imprimen los mismos datos, si el código es el mismo en ambas operaciones de lectura?R// Porque El primero imprime solo hasta el quinto caracter y el otro empieza a partir de ahi 
3. ¿Por qué debo escribir `fp` antes de llamar al método `read()`?R// Porque fp es el objeto que almacena el archivo   
'''