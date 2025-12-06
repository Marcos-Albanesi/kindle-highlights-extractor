# Función para abrir, leer el archivo y retornarlo.

def open_txt(txt_kindle):
    try:
        with open(txt_kindle, "r", encoding="utf-8") as raw_archive:
            return raw_archive.read()
    except FileNotFoundError:
        print("No se encontró el txt.")
        return None
