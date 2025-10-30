lista = ["Everything_stays", "Alejandro", "invisible", "Hai_Yorokonde", "Stay_with_me"]
ruta = "c:\\Users\\aleja\\Downloads"
file_name = "canciones.txt"
file_info = ruta+"\\"+file_name
modo = "w"

'''
for i in range(len(lista)): #Coloca un enter despues de cada elemento de la lista 
    lista[i] += "\n\n"
'''
 
fp = open(file_info,modo,encoding="utf-8")
# fp.writelines(lista)
#Otra solucion
for cancion in lista:
    fp.write(cancion+"\n")
fp.close()