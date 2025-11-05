lista = ["Everything_stays", "Alejandro", "invisible", "Hai_Yorokonde", "Stay_with_me"]
ruta = "c:\\Users\\aleja\\Downloads"
file_name = "canciones.txt"
file_info = ruta+"\\"+file_name
modo = "r"

with open(file_info,modo, encoding="utf-8") as archivo:
    for dato in archivo:
        print(dato,end= "") 
# Hacer operaciones con el archivo
# El archivo se cierra automáticamente al salir del bloque with