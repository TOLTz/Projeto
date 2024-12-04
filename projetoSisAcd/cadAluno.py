from os import system
import string
import random

student = [] # lista usada para armazenar os dados dos alunos, se der tempo transformar em banco de dados mais complexo


def cadStudent():
    """ Cadastra um novo aluno

    Returns:
        dict: Retorna um dicionario
    """
    name = input('Digite o nome: ')
    registration = print(f'Matricula: {registrationNum()}')
    birthday = input('Digite a data de nascimento: ')
    gender = input('Digite o genero: ')
    address = input('Digite o Endereco: ')
    cel = input('Digite o telefone (apenas numeros): ')
    email = input('Digite o Email: ')
    return {'Nome': name, 'Matricula': registration, 'DataAniversario': birthday, 'genero': gender, 'Endereco': address, 'Telefone': cel, 'Email': email}


def registrationNum():
    """Gera uma sequencia de 8 numeros e uma letra aleatoria para a matricula do aluno.

    Returns:
        Str: retorna uma string com a matricula.
    """
    # gera uma sequencia de 8 numreos aleatorios (a quantidade de numeros e definida pelo 'k')
    # e o os numeros sao definidos pelo 'string.digits')
    num = ''.join(random.choices(string.digits, k= 8))
    letterUpper = random.choice(string.ascii_uppercase) # ascii_uppercase gera letras maiusculas
    registrationId = num + letterUpper 
    return registrationId
    

def registration():
    """Adiciona um novo aluno ao sistema, com os dados fornecidos pela funcao
    cadStudent(). Alem de fazer a verificacao se o aluno esta com os dados corretos.
    """
    _ = True
    _student = cadStudent()
    while _:
        print(_student)
        confirm = input('confirmar? (S/N): ')
        if confirm.upper() == 'S':
            system('cls')
            student.append(_student)
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
        
    
