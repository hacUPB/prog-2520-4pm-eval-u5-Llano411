import matplotlib.pyplot as plt
import numpy as np
import math
# Datos
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
x = []
y=[]
for i in range(100):
    dato = i/100
    x.append(dato)
for j in range(len(x)):
    dato = math.cos(2*math.pi*x[j])
    y.append(dato)
#x=[1,3,45,67]
#y=[3,5,7,4]

# Crear la gráfica
plt.plot(x, y) #Hace la grafica con lineas 
plt.scatter(x,y) #Hace la grafica con puntos

# Agregar título y etiquetas
plt.title('Gráfica de Coseno')
plt.xlabel('X')
# plt.ylabel('sin(X)')
plt.ylabel('cos(X)')

# Mostrar la gráfica
plt.show()


# Activar el entorno virtual: source ./.venv/Scripts/activate