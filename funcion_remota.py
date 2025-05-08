def ejecutar_programa():
    import pandas as pd
    from openpyxl import load_workbook
    import os

    def cargar_datos():
        archivo_txt = input("Introduce el nombre del archivo .txt: ")

        if not os.path.exists(archivo_txt):
            print(f"El archivo {archivo_txt} no existe.")
            return

        try:
            df = pd.read_csv(archivo_txt, delimiter="\t")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return

        archivo_excel = archivo_txt.replace(".txt", ".xlsx")
        df.to_excel(archivo_excel, index=False)
        print(f"El archivo Excel {archivo_excel} ha sido creado.")

    def crear_tabla_dinamica():
        archivo_excel = input("Introduce el nombre del archivo Excel: ")
        
        if not os.path.exists(archivo_excel):
            print(f"El archivo {archivo_excel} no existe.")
            return

        try:
            wb = load_workbook(archivo_excel)
            ws = wb.active

            # Aquí deberías construir la tabla dinámica con openpyxl o pandas
            # Pero openpyxl no soporta tablas dinámicas como Excel. Esto es simbólico.
            print("Simulación de tabla dinámica creada.")

            wb.save(archivo_excel)
            print("Archivo Excel guardado con supuestos cambios.")
        except Exception as e:
            print(f"Error al modificar el archivo Excel: {e}")

    print("✔️ Acceso concedido. Ejecutando programa...")
    cargar_datos()
    crear_tabla_dinamica()
