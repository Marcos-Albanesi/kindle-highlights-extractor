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
    book_highlights = []

    for each_list in highlights:
        dictionary = {
            "title": each_list[0],
            "metadata": each_list[1],
            "highlight": each_list[2]
        }
        book_highlights.append(dictionary)

    highlights_by_book = {}
    
    for book in book_highlights:
        title = book["title"]

        if title not in highlights_by_book:
            highlights_by_book[title] = []
        
        highlights_by_book[title].append(book)
    
    return highlights_by_book
