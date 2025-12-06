from reader import open_txt
from parser import clean_lines, parse_info, group_by_book
from markdown_writer import export_markdown_files

def main():
    # 1. Leer el archivo del Kindle
    raw = open_txt("my_clippings.txt")  
    if raw is None:
        return  # No se puede seguir

    # 2. Eliminar líneas vacías
    non_empty = clean_lines(raw)

    # 3. Convertir a bloques
    highlights = parse_info(non_empty)

    # 4. Agrupar por libro
    grouped = group_by_book(highlights)

    # 5. Exportar los Markdown
    export_markdown_files(grouped)

if __name__ == "__main__":
    main()
