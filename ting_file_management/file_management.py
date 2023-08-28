import sys


def txt_importer(path_file):
    if path_file[-4:] != ".txt":
        return sys.stderr.write("Formato inválido")

    text_file = []

    try:
        with open(path_file, "r") as file:
            for line in file:
                text_file.append(line.strip())
    except (FileNotFoundError, FileExistsError):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    return text_file
