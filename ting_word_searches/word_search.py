def exists_word(word, instance):
    data = []
    for n in range(len(instance)):
        file = instance.search(n)
        f_name = file["nome_do_arquivo"]
        lines = file["linhas_do_arquivo"]
        c = 0
        for index, line in enumerate(lines):
            if word.lower() in line.lower() and c == 0:
                data.append(
                    {
                        "palavra": word,
                        "arquivo": f_name,
                        "ocorrencias": [{"linha": index + 1}]
                        }
                    )
                c += 1
            elif word.lower() in line.lower():
                data[-1]["ocorrencias"].append({"linha": index + 1})
                c += 1
    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
