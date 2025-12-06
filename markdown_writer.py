# Función para crear los MD por libro.

def export_markdown_files(highlights_by_book):
    for title, highlights in highlights_by_book.items():
        filename = title.replace(":", "").replace("?", "").replace("/", "_") + ".md"

        content = f"# {title}\n\n"

        for item in highlights:
            content += item["highlight"] + "\n"

        try:
            with open(filename, "x", encoding="utf-8") as f:
                f.write(content)
            print(f"Archivo creado: {filename}.")
        except FileExistsError:
            print(f"El resumen del libro {filename} ya existe.")
