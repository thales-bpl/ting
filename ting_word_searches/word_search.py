from ting_file_management.queue import Queue


def exists_word(word, instance):
    """Aqui irá sua implementação"""


def search_by_word(word, instance: Queue):
    result = []
    for item in instance.list:
        ocurred = False
        parcial = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [],
            }
        for index, line in enumerate(item["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                ocurred = True
                parcial["ocorrencias"].append(
                    {"linha": index + 1, "conteudo": line}
                )

        if ocurred:
            result.append(parcial)

    return result
