# Manipular el archivo.

# Eliminar líneas vacías
def clean_lines(raw_archive):
    lines = raw_archive.splitlines()
    non_empty_lines = []
    for line in lines:
        if line.strip() != "":
            non_empty_lines.append(line)
    return non_empty_lines

# Creo una lista de listas. Cada lista será un resaltado, con su Título, Metadatos, Resaltados
def parse_info(non_empty_lines):
    highlights = []
    current_block = []

    for line in non_empty_lines:

        if line.startswith("=========="):
            # Como siempre llega hasta acá, el bloque está completo
            highlights.append(current_block)
            current_block = []
        else:
            current_block.append(line)

    return highlights

# Cada uno de esos bloque anteriores, los agrupo según el libro, creando un diccionario por libro
def group_by_book(highlights):
    highlights_by_book = {}

    for lista in highlights:
        title = lista[0]

        highlight = {
            "title": lista[0],
            "metadata": lista[1],
            "highlight": lista[2]
        }

        if title not in highlights_by_book:
            highlights_by_book[title] = []

        highlights_by_book[title].append(highlight)

    return highlights_by_book
