ruta = "c:\\Users\\aleja\\Downloads"
file_name = "aviones2.txt"

modo = "x"
fp = open(ruta+"\\"+file_name, modo, encoding="utf-8")
data = input("ingrese el nombre de un avion: ")
peso = int(input("ingrese el peso del avion: "))
velocidad = float(input("Velocidad maxima: "))

fp.write(data+"\n")
fp.write(str(peso)+"\n")
fp.write(str(velocidad)+"\n\n")
fp.close()