from os import system
import string
import random
from bd import addData
from tinydb import TinyDB, Query


def cadTeacher():
    """ Cadastra um novo professor

    Returns:
        dict: Retorna um dicionario
    """
    _ = True
    idReg = registrationNum()
    while _:
        try:
            name = input('Digite o nome: ')
            noneWord(name)
            name = name.title()
            print(f'Matricula: {idReg}')
            birthday = input('Digite a data de nascimento: ')
            noneWord(birthday)
            gender = input('Digite o genero: ')
            noneWord(gender)
            address = input('Digite o Endereco: ')
            noneWord(address)
            cel = input('Digite o telefone (apenas numeros): ')
            noneWord(cel)
            email = input('Digite o Email: ').lower()
            noneWord(email)
        except:
            system('cls')
            print("digite uma palavra")
            continue
        finally:
            _ = False
    return {'Nome': name.replace(' ', '_'), 'Matricula': idReg, 'DataAniversario': birthday, 'genero': gender, 'Endereco': address, 'Telefone': cel, 'Email': email, 'disciplina': []}


def registrationNum():
    """Gera uma sequencia de 6 numeros e uma letra aleatoria para a matricula.

    Returns:
        Str: retorna uma string com a matricula.
    """
    # gera uma sequencia de 6 numreos aleatorios (a quantidade de numeros e definida pelo 'k')
    # e o os numeros sao definidos pelo 'string.digits')
    num = ''.join(random.choices(string.digits, k= 6))
    letterUpper = random.choice(string.ascii_uppercase) # ascii_uppercase gera letras maiusculas
    registrationId = letterUpper + num 
    return registrationId

def noneWord(args):
    """Verifica se o argumento contem palavras caso contrario levanta um erro

    Args:
        args (str): Palavra para verificar se é uma palavra
    """
    if args == '':
        raise

def registrationTeacher():
    """Adiciona um novo professor ao sistema, com os dados fornecidos pela funcao
    cadStudent(). Alem de fazer a verificacao se o professor esta com os dados corretos.
    """
    _ = True
    _teacher = cadTeacher()
    while _:
        print(_teacher)
        confirm = input('confirmar? (S/N): ')
        if confirm.upper() == 'S':
            system('cls')
            addData('Teacher.json', _teacher)
            retry = input('quer tentar novament? ')
            if retry.upper() == 'N':
                _ = False
                system('cls')
                print('ok, até mais!')
            else:
                system('cls')
                continue
        elif confirm.upper() == 'N':
            system('cls')
            _ = False
            print('cancelado!')
            retry = input('quer tentar novament? ')
            if retry.upper() == 'N':
                system('cls')
                print('ok, até mais!')
            else:
                system('cls')
                continue
        else:
            print('opcao invalida')
            continue
        
def searchTeacher():
    """Funcao que busca o professor pelo nome, matricula ou pela disciplina

    Returns:
        List : lista com os dados do professor
    """
    query = Query()
    teacher = TinyDB('Teacher.json')
    chooseItem = input('deseja pesquisar por: \nNome (N), Matricula (M) ou Disciplina (D)? ')
    if chooseItem.upper() == 'N':
        searchName = input('digite o nome do Professor: ')
        searchName = searchName.title()
        searchName = searchName.replace(' ', '_')
        searched = teacher.search(query.Nome.search(searchName))
        if searched == []:
            print('Professor nao encontrado')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchTeacher()
            else:
                return print('Ok, até mais!')
        else:
            print(searched)
    elif chooseItem.upper() == 'M':
        searchRegistration = input('digite a matricula do Professor: ')
        searchRegistration = searchRegistration.upper()
        searched = teacher.search(query.Matricula.search(searchRegistration))
        if searched == []:
            print('Professor nao encontrado')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchTeacher()
            else:
                return print('Ok, até mais!')
        else:
            print(searched)
    elif chooseItem.upper() == 'D':
        searchSupplies = input('digite a Disciplina do Professor: ')
        searchSupplies = searchSupplies.capitalize()
        searched = teacher.search(query.disciplina.search(searchSupplies))
        if searched == []:
            print('Professor nao encontrado')
            return searchTeacher()
        else:
            print(searched)
    else:
        print('opcao invalida')
        return searchTeacher()

