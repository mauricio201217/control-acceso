import pandas as pd
import requests
from openpyxl import Workbook, load_workbook
import os

# URL del archivo de control de acceso en GitHub
url = "https://raw.githubusercontent.com/mauricio201217/control-acceso/main/acceso.txt"

def comprobar_acceso(): 
    """
    Comprueba el acceso al programa leyendo el archivo 'acceso.txt' desde GitHub.
    Si el archivo contiene 'DENEGADO', bloquea el acceso.
    """
    try:
        # Obtener el contenido del archivo de acceso desde GitHub
        response = requests.get(url, timeout=10)  # Asegúrate de usar el parámetro timeout
        
        if response.status_code == 200:
            estado_acceso = response.text.strip()  # Eliminar espacios en blanco

            if estado_acceso == "DENEGADO":
                print("Acceso denegado.")
                return False
            elif estado_acceso == "PERMITIDO":
                print("Acceso permitido.")
                return True
            else:
                print("Estado de acceso desconocido.")
                return False
        else:
            print(f"Error al obtener el archivo de acceso (Status: {response.status_code}).")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar: {e}")
        return False

# Resto del código donde procesas los datos
def cargar_datos():
    """
    Función para cargar un archivo .txt, procesarlo y convertirlo a un archivo de Excel.
    """
    archivo_txt = input("Introduce el nombre del archivo .txt: ")

    # Comprobar si el archivo .txt existe
    if not os.path.exists(archivo_txt):
        print(f"El archivo {archivo_txt} no existe.")
        return

    # Cargar los datos desde el archivo .txt
    try:
        df = pd.read_csv(archivo_txt, delimiter="\t")  # Asumiendo que el archivo está tabulado
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    # Crear un archivo Excel y guardar los datos
    archivo_excel = archivo_txt.replace(".txt", ".xlsx")
    df.to_excel(archivo_excel, index=False)
    print(f"El archivo Excel {archivo_excel} ha sido creado.")

def crear_tabla_dinamica():
    """
    Crear una tabla dinámica en un archivo Excel dado.
    """
    archivo_excel = input("Introduce el nombre del archivo Excel: ")
    
    if not os.path.exists(archivo_excel):
        print(f"El archivo {archivo_excel} no existe.")
        return

    # Cargar el archivo Excel
    wb = load_workbook(archivo_excel)
    ws = wb.active

    # Crear la tabla dinámica
    tabla_dinamica = ws.tables.add('TablaDinamica', range(ws.dimensions))
    print("Tabla dinámica creada correctamente.")
    
    # Guardar el archivo con la tabla dinámica
    wb.save(archivo_excel)

def procesar_datos():
    """
    Función principal que ejecuta todo el flujo de procesamiento.
    """
    if not comprobar_acceso():
        return  # Detener ejecución si el acceso está denegado
    
    cargar_datos()  # Cargar y convertir el archivo .txt a Excel
    crear_tabla_dinamica()  # Crear tabla dinámica en el archivo Excel

# Ejecutar el proceso principal
procesar_datos()
