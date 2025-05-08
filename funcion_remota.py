def ejecutar_programa():
    import pandas as pd
    from openpyxl import Workbook, load_workbook
    import os

    def cargar_datos():
        """
        Carga un archivo .txt, lo procesa y lo convierte en un archivo de Excel.
        """
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
        """
        Crea una tabla dinámica en un archivo Excel dado.
        """
        archivo_excel = input("Introduce el nombre del archivo Excel: ")

        if not os.path.exists(archivo_excel):
            print(f"El archivo {archivo_excel} no existe.")
            return

        wb = load_workbook(archivo_excel)
        ws = wb.active

        # No se puede crear una tabla dinámica real sin Excel, pero simulamos
        print("Simulación de tabla dinámica realizada.")
        wb.save(archivo_excel)

    print("Acceso permitido. Ejecutando programa...")
    cargar_datos()
    crear_tabla_dinamica()
