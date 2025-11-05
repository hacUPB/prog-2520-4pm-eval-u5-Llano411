import csv
import os
import matplotlib.pyplot as plt 
import numpy as np 

def listar_archivos():
    """Función que lista los archivos en una ruta especificada o en la ruta actual."""
    print("\n" + "┌" + "─"*48 + "┐")
    print("│" + " "*15 + "LISTAR ARCHIVOS" + " "*17 + "│")
    print("├" + "─"*48 + "┤")
    print("│  [1] Listar archivos en la ruta actual      │")
    print("│  [2] Listar archivos en la carpeta 'archivos'│")
    print("│  [3] Ingresar una ruta personalizada        │")
    print("└" + "─"*48 + "┘")
    opcion = input("\n➤ Selecciona una opción (1-3): ")
    
    if opcion == '1':
        ruta = os.getcwd()  # os.getcwd() -> Obtiene el directorio de trabajo actual
        print(f"\nListando archivos en la ruta actual: {ruta}")
    elif opcion == '2':
        ruta = r"C:\Users\aleja\Documents\Programacion\prog-2520-4pm-eval-u5-Llano411\Reto\archivos"
        print(f"\nListando archivos en la carpeta 'archivos': {ruta}")
    elif opcion == '3':
        ruta = input("Ingresa la ruta donde deseas buscar archivos: ")
    else:
        print("Opción no válida.")
        return
    
    # os.listdir() -> Obtiene una lista con todos los nombres de archivos y carpetas en la ruta
    elementos = os.listdir(ruta)
    
    archivos = []
    carpetas = []
    
    for elemento in elementos:
        ruta_completa = os.path.join(ruta, elemento)  # os.path.join() -> Une la ruta con el nombre del elemento
        if os.path.isfile(ruta_completa):  # os.path.isfile() -> Verifica si es un archivo
            archivos.append(elemento)
        elif os.path.isdir(ruta_completa):  # os.path.isdir() -> Verifica si es una carpeta
            carpetas.append(elemento)
    
    print("\n" + "="*50)
    if carpetas:
        print(f"\nCARPETAS ({len(carpetas)}):")
        for carpeta in sorted(carpetas):
            print(f"  📁 {carpeta}")
    
    if archivos:
        print(f"\nARCHIVOS ({len(archivos)}):")
        for archivo in sorted(archivos):
            print(f"  📄 {archivo}")
    
    print("\n" + "="*50)
    print(f"Total: {len(carpetas)} carpeta(s) y {len(archivos)} archivo(s)")

def contar_palabras_caracteres():
    """Función que cuenta palabras y caracteres en un archivo de texto."""
    print("\n" + "╔" + "═"*48 + "╗")
    print("║" + " "*8 + "CONTAR PALABRAS Y CARACTERES" + " "*12 + "║")
    print("╚" + "═"*48 + "╝")
    ruta_archivo = r"C:\Users\aleja\Documents\Programacion\prog-2520-4pm-eval-u5-Llano411\Reto\archivos\Texto.txt"
    
    archivo = open(ruta_archivo, 'r', encoding='utf-8')
    contenido = archivo.read() 
    archivo.close()  
    
    caracteres_con_espacios = len(contenido)
    caracteres_sin_espacios = 0
    
    for caracter in contenido:
        if caracter != ' ' and caracter != '\n' and caracter != '\t':
            caracteres_sin_espacios += 1
    
    numero_palabras = 1  
    for caracter in contenido:
        if caracter == ' ' or caracter == '\n' or caracter == '\t':
            numero_palabras += 1
    
    print("\n" + "="*50)
    print(f"Número de palabras: {numero_palabras}")
    print(f"Número de caracteres (con espacios): {caracteres_con_espacios}")
    print(f"Número de caracteres (sin espacios): {caracteres_sin_espacios}")
    print("="*50)

def reemplazar_palabra():
    """Función que reemplaza una palabra por otra en un archivo de texto."""
    print("\n" + "╔" + "═"*48 + "╗")
    print("║" + " "*14 + "REEMPLAZAR PALABRA" + " "*16 + "║")
    print("╚" + "═"*48 + "╝")
    ruta_archivo = r"C:\Users\aleja\Documents\Programacion\prog-2520-4pm-eval-u5-Llano411\Reto\archivos\Texto.txt"
    
    archivo = open(ruta_archivo, 'r', encoding='utf-8')
    contenido = archivo.read()
    archivo.close()
    
    palabra_buscar = input("Ingresa la palabra que deseas buscar: ")
    palabra_reemplazar = input("Ingresa la palabra de reemplazo: ")
    
    contador = contenido.count(palabra_buscar)
    
    if contador == 0:
        print(f"\n❌ La palabra '{palabra_buscar}' no se encontró en el archivo.")
    else:
        contenido_nuevo = contenido.replace(palabra_buscar, palabra_reemplazar)
        
        archivo = open(ruta_archivo, 'w', encoding='utf-8')
        archivo.write(contenido_nuevo)
        archivo.close()
        
        print(f"\n✅ ¡Éxito! Se reemplazaron {contador} palabra(s) de '{palabra_buscar}' por '{palabra_reemplazar}'.")

def histograma_vocales():
    """Función que cuenta las vocales y muestra un histograma gráfico."""
    print("\n" + "╔" + "═"*48 + "╗")
    print("║" + " "*13 + "HISTOGRAMA DE VOCALES" + " "*14 + "║")
    print("╚" + "═"*48 + "╝")
    ruta_archivo = r"C:\Users\aleja\Documents\Programacion\prog-2520-4pm-eval-u5-Llano411\Reto\archivos\Texto.txt"
    
    archivo = open(ruta_archivo, 'r', encoding='utf-8')
    contenido = archivo.read()
    archivo.close()
    
    contenido_minusculas = contenido.lower()
    
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0
    
    for caracter in contenido_minusculas:
        if caracter == 'a':
            contador_a += 1
        elif caracter == 'e':
            contador_e += 1
        elif caracter == 'i':
            contador_i += 1
        elif caracter == 'o':
            contador_o += 1
        elif caracter == 'u':
            contador_u += 1
    
    print("\n" + "="*50)
    print("CONTEO DE VOCALES")
    print("="*50)
    print(f"A: {contador_a}")
    print(f"E: {contador_e}")
    print(f"I: {contador_i}")
    print(f"O: {contador_o}")
    print(f"U: {contador_u}")
    print("="*50)
    total_vocales = contador_a + contador_e + contador_i + contador_o + contador_u
    print(f"Total de vocales: {total_vocales}")
    
    vocales = ['A', 'E', 'I', 'O', 'U'] 
    conteos = [contador_a, contador_e, contador_i, contador_o, contador_u] 
    
    # plt.bar() -> Crea el gráfico de barras con las vocales y sus conteos
    plt.bar(vocales, conteos)
    
    # plt.xlabel() -> Etiqueta del eje X (horizontal)
    plt.xlabel('Vocales')
    
    # plt.ylabel() -> Etiqueta del eje Y (vertical)
    plt.ylabel('Frecuencia')
    
    # plt.title() -> Título del gráfico
    plt.title('Histograma de Vocales')
    
    plt.show()
    
    print("\nEl histograma gráfico se ha mostrado en una ventana separada.")

def submenu_texto():
    """Función que muestra el submenú para procesar archivos de texto."""
    while True:
        print("\n" + "┌" + "─"*52 + "┐")
        print("│" + " "*12 + "SUBMENÚ ARCHIVOS DE TEXTO" + " "*15 + "│")
        print("├" + "─"*52 + "┤")
        print("│  [1] 🔢 Contar número de palabras y caracteres    │")
        print("│  [2] 🔄 Reemplazar una palabra por otra           │")
        print("│  [3] 📈 Histograma de ocurrencia de las vocales   │")
        print("│  [4] ⬅️  Volver al menú principal                  │")
        print("└" + "─"*52 + "┘")
        opcion = input("\n➤ Selecciona una opción (1-4): ")
        
        if opcion == '1':
            contar_palabras_caracteres()
        elif opcion == '2':
            reemplazar_palabra()
        elif opcion == '3':
            histograma_vocales()
        elif opcion == '4':
            print("\nVolviendo al menú principal...")
            break
        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")

def mostrar_primeras_filas():
    """Función que muestra las primeras 15 filas de un archivo CSV."""
    print("\n" + "╔" + "═"*48 + "╗")
    print("║" + " "*10 + "MOSTRAR PRIMERAS 15 FILAS" + " "*13 + "║")
    print("╚" + "═"*48 + "╝")
    ruta_archivo = r"C:\Users\aleja\Documents\Programacion\prog-2520-4pm-eval-u5-Llano411\Reto\archivos\info_satena.csv"
    
    delimitador = input("Ingresa el delimitador del archivo (ejemplo: ; o , o |): ")
    
    archivo = open(ruta_archivo, 'r', encoding='utf-8-sig')  # utf-8-sig elimina el BOM automáticamente (IA)
    lector_csv = csv.reader(archivo, delimiter=delimitador)  # csv.reader() -> Lee el archivo CSV
    
    print("\n" + "="*100)
    contador = 0
    for fila in lector_csv:
        if contador < 15:
            for elemento in fila:
                print(elemento, end=" | ")
            print() 
            contador += 1
        else:
            break
    
    print("="*100)
    print(f"\nSe mostraron las primeras {contador} filas del archivo.")
    archivo.close()

def calcular_estadisticas():
    """Función que calcula estadísticas de una columna específica del CSV."""
    print("\n" + "╔" + "═"*48 + "╗")
    print("║" + " "*12 + "CALCULAR ESTADÍSTICAS" + " "*15 + "║")
    print("╚" + "═"*48 + "╝")
    ruta_archivo = r"C:\Users\aleja\Documents\Programacion\prog-2520-4pm-eval-u5-Llano411\Reto\archivos\info_satena.csv"
    
    delimitador = input("Ingresa el delimitador del archivo (ejemplo: ; o , o |): ")
    
    archivo = open(ruta_archivo, 'r', encoding='utf-8-sig') 
    lector_csv = csv.reader(archivo, delimiter=delimitador)
    
    encabezados = next(lector_csv)  # next() -> Lee la siguiente línea del archivo
    
    print("\nColumnas disponibles:")
    for i in range(len(encabezados)):
        print(f"{i}: {encabezados[i]}")
    
    archivo.close()
    
    columna_seleccionada = int(input("\nIngresa el número de la columna que deseas analizar: "))
    
    archivo = open(ruta_archivo, 'r', encoding='utf-8')
    lector_csv = csv.reader(archivo, delimiter=delimitador)
    next(lector_csv)  # Salta los encabezados
    
    valores = []
    for fila in lector_csv:
        try:
            valor = float(fila[columna_seleccionada])
            valores.append(valor)
        except:
            pass  # Si no es número o no existe, lo ignora
    
    archivo.close()
    
    if len(valores) == 0:
        print("\nNo se encontraron valores numéricos en esa columna.")
        return
    
    numero_datos = len(valores)
    
    suma = 0
    for valor in valores:
        suma += valor
    promedio = suma / numero_datos
    
    valor_max = max(valores)
    
    valor_min = min(valores)
    
    mediana = np.median(valores)  # np.median() -> Calcula la mediana de los valores
    
    desviacion_estandar = np.std(valores)  # np.std() -> Calcula la desviación estándar
    
    print("\n" + "="*50)
    print(f"ESTADÍSTICAS DE: {encabezados[columna_seleccionada]}")
    print("="*50)
    print(f"Número de datos: {numero_datos}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Desviación estándar: {desviacion_estandar:.2f}")
    print(f"Valor máximo: {valor_max:.2f}")
    print(f"Valor mínimo: {valor_min:.2f}")
    print("="*50)

def graficar_columna():
    """Función que grafica una columna del archivo CSV."""
    print("\n" + "╔" + "═"*48 + "╗")
    print("║" + " "*15 + "GRAFICAR COLUMNA" + " "*17 + "║")
    print("╚" + "═"*48 + "╝")
    ruta_archivo = r"C:\Users\aleja\Documents\Programacion\prog-2520-4pm-eval-u5-Llano411\Reto\archivos\info_satena.csv"
    
    delimitador = input("Ingresa el delimitador del archivo (ejemplo: ; o , o |): ")
    
    archivo = open(ruta_archivo, 'r', encoding='utf-8-sig') 
    lector_csv = csv.reader(archivo, delimiter=delimitador)
    encabezados = next(lector_csv)
    
    print("\nColumnas disponibles:")
    for i in range(len(encabezados)):
        print(f"{i}: {encabezados[i]}")
    
    archivo.close()
    
    columna_seleccionada = int(input("\nIngresa el número de la columna para graficar: "))
    
    archivo = open(ruta_archivo, 'r', encoding='utf-8')
    lector_csv = csv.reader(archivo, delimiter=delimitador)
    next(lector_csv)
    
    valores = []
    for fila in lector_csv:
        try:
            valor = float(fila[columna_seleccionada])
            valores.append(valor)
        except:
            pass 
    
    archivo.close()
    
    if len(valores) == 0:
        print("\nNo se encontraron valores numéricos en esa columna.")
        return
    
    print("\n" + "┌" + "─"*45 + "┐")
    print("│" + " "*14 + "TIPO DE GRÁFICO" + " "*16 + "│")
    print("├" + "─"*45 + "┤")
    print("│  [1] 📍 Gráfico de Dispersión (puntos)  │")
    print("│  [2] 📊 Gráfico de Barras               │")
    print("│  [3] 🔄 Ambos gráficos                  │")
    print("└" + "─"*45 + "┘")
    tipo_grafico = input("\n➤ Selecciona el tipo de gráfico (1-3): ")
    
    if tipo_grafico == '1':
        plt.scatter(range(len(valores)), valores)  # plt.scatter() -> Gráfico de puntos
        plt.title('Grafico de Dispersion')
        plt.show()
        print("\nEl gráfico de dispersión se mostró correctamente.")
        
    elif tipo_grafico == '2':
        plt.bar(range(15), valores[:15])  # plt.bar() -> Gráfico de barras
        plt.title('Grafico de Barras (Primeros 15 valores)')
        plt.show()
        print("\nEl gráfico de barras se mostró correctamente.")
        
    elif tipo_grafico == '3':
        plt.scatter(range(len(valores)), valores)
        plt.title('Grafico de Dispersion')
        plt.show()
        
        plt.bar(range(15), valores[:15])
        plt.title('Grafico de Barras (Primeros 15 valores)')
        plt.show()
        print("\nAmbos gráficos se mostraron correctamente.")
        
    else:
        print("\nOpción no válida.")

def submenu_csv():
    """Función que muestra el submenú para procesar archivos CSV."""
    while True:
        print("\n" + "┌" + "─"*52 + "┐")
        print("│" + " "*14 + "SUBMENÚ ARCHIVOS CSV" + " "*18 + "│")
        print("├" + "─"*52 + "┤")
        print("│  [1] 👁️  Mostrar las 15 primeras filas             │")
        print("│  [2] 📊 Calcular estadísticas de una columna      │")
        print("│  [3] 📈 Graficar una columna completa             │")
        print("│  [4] ⬅️  Volver al menú principal                  │")
        print("└" + "─"*52 + "┘")
        opcion = input("\n➤ Selecciona una opción (1-4): ")
        
        if opcion == '1':
            mostrar_primeras_filas()
        elif opcion == '2':
            calcular_estadisticas()
        elif opcion == '3':
            graficar_columna()
        elif opcion == '4':
            print("\nVolviendo al menú principal...")
            break
        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")

def mostrar_menu(): 
    print("\n" + "╔" + "═"*50 + "╗")
    print("║" + " "*15 + "MENÚ PRINCIPAL" + " "*21 + "║")
    print("╠" + "═"*50 + "╣")
    print("║  [1] 📂 Listar archivos en una ruta" + " "*13 + "║")
    print("║  [2] 📝 Procesar archivo de texto (.txt)" + " "*9 + "║")
    print("║  [3] 📊 Procesar archivo de excel (.csv)" + " "*9 + "║")
    print("║  [4] 🚪 Salir" + " "*36 + "║")
    print("╚" + "═"*50 + "╝")

def main(): 
    print("\n" + "="*52)
    print("  🎯 BIENVENIDO AL SISTEMA DE GESTIÓN DE ARCHIVOS 🎯")
    print("="*52)
    
    while True:
        mostrar_menu()
        opcion = input("\n➤ Selecciona una opción (1-4): ")

        if opcion == '1':
            listar_archivos()
        
        elif opcion == '2':
            submenu_texto()

        elif opcion == '3':
            submenu_csv()

        elif opcion == '4':
            print("\n" + "="*52)
            print("  👋 ¡Gracias por usar la aplicación! ¡Hasta pronto! 👋")
            print("="*52)
            break 
        
        else:
            print("\n❌ Opción no válida. Por favor, intenta de nuevo con un número del 1 al 4.")

main()

'''
Uso de IA
Se uso la ia para mejorar la presentacion del codigo a nivel visual, tambien se uso para identificar algunos errores de presentacion y descubrir
metodos de simplificacion o mejora tales como el uso de la "r"

'''