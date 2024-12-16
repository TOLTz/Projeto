from os import system
import string
import random
from bd import addData


teacher = [] # lista usada para armazenar os dados dos professores, se der tempo transformar em banco de dados mais complexo


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
            print(f'Matricula: {idReg}')
            birthday = input('Digite a data de nascimento: ')
            noneWord(birthday)
            gender = input('Digite o genero: ')
            noneWord(gender)
            address = input('Digite o Endereco: ')
            noneWord(address)
            cel = input('Digite o telefone (apenas numeros): ')
            noneWord(cel)
            email = input('Digite o Email: ')
            noneWord(email)
            disciplina = input('Digite a disciplina: ')
            noneWord(disciplina)
        except:
            system('cls')
            print("digite uma palavra")
            continue
        finally:
            _ = False
    return {'Nome': name, 'Matricula': idReg, 'DataAniversario': birthday, 'genero': gender, 'Endereco': address, 'Telefone': cel, 'Email': email, 'disciplina': disciplina}


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
    if args == '':
        raise

def registration():
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
            _ = False
            return print('salvo com sucesso')
        elif confirm.upper() == 'N':
            system('cls')
            _ = False
            return print('cancelado!')
        else:
            print('opcao invalida')
            continue
        
registration()