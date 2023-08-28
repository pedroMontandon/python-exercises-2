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
    data = instance.dequeue()
    if data is None:
        sys.stdout.write("Não há elementos\n")
    else:
        file_name = data["nome_do_arquivo"]
        sys.stdout.write(f'Arquivo {file_name} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        sys.stdout.write(f"{instance.search(position)}")
    except IndexError:
        sys.stderr.write("Posição inválida")
