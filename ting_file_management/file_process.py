import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file: str, instance: Queue):
    for item in instance.list:
        if item['nome_do_arquivo'] == path_file:
            print('Esse arquivo já foi listado')
            return

    file_content_list = txt_importer(path_file)
    result = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file_content_list),
        'linhas_do_arquivo': file_content_list
    }

    instance.enqueue(result)
    print(result, file=sys.stdout)


def remove(instance: Queue):
    if len(instance) == 0:
        print('Não há elementos')
        return

    dequeued = instance.dequeue()
    file_name = dequeued['nome_do_arquivo']
    print(f'Arquivo {file_name} removido com sucesso')


def file_metadata(instance, position):
    try:
        target = instance.search(position)
        print(target)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
