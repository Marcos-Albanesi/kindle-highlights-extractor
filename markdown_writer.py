# Función para crear los MD por libro.

def export_markdown_files(highlights_by_book):
    for title, highlights in highlights_by_book.items():
        filename = title.replace(":", "").replace("?", "").replace("/", "_") + ".md"

        content = f"# {title}\n\n"

        first_metadata = highlights[0]["metadata"]
        last_metadata = highlights[-1]["metadata"]

        first_highlight = first_metadata[first_metadata.rfind("|") + 2:]
        last_highlight = last_metadata[last_metadata.rfind("|") + 2:]

        content += f"Fecha de inicio: {first_highlight}.\n"
        content += f"Fecha de fin: {last_highlight}.\n\n"

        for item in highlights:
            content += item["highlight"] + "\n"

        try:
            with open(filename, "x", encoding="utf-8") as f:
                f.write(content)
            print(f"Archivo creado: {filename}.")
        except FileExistsError:
            print(f"El resumen del libro {filename} ya existe.")
