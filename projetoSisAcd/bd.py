from tinydb import TinyDB

def addData(file, dict):
    """funcao que cria um banco de dados e adciona dados ao mesmo

    Args:
        file (str): Nome do banco de dados, com a extensao json
        dict (dict): Dicionario com os dados a serem adicionados
    """
    new = TinyDB(file, indent=6)
    new.insert(dict)