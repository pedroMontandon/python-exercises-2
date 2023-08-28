from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for number in range(len(instance)):
        file = instance.search(number)
        if file["nome_do_arquivo"] == path_file:
            return

    txt_array = txt_importer(path_file)

    txt_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_array),
        "linhas_do_arquivo": txt_array
    }

    instance.enqueue(txt_dict)
    sys.stdout.write(f"{txt_dict}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
