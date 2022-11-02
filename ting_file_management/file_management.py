import sys


def txt_importer(path_file):
    if ".txt" not in path_file[-4:]:
        print("Formato inválido", file=sys.stderr)
        return

    try:
        with open(path_file) as file:
            return [line.replace('\n', '') for line in file.readlines()]

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
