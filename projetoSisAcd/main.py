from adminScreen import mainSearch, mainReg, allocation, delete
from os import system


print('olá, bem vindo ao sistema academico!')
studentOrTeacher = input('Você é um professor (P) ou um aluno (A)? ')
system('cls')
_ = True
if studentOrTeacher == 'professor' or 'P':
    while _:
        system('cls')
        print('ok, você está logado como professor')
        choice = input('Qual operação deseja fazer? \nPesquisa (P), Registrar (R), Alocar (A), Deletar (D) ou Sair (S)? ')
        system('cls')
        if choice.lower() == 'p':
            mainSearch()
            retry = input('Quer fazer mais uma ação?(s/n) ')
            if retry.lower() == 'n':
                _ = False
                print('Ok, Até mais ver!')
            else:
                continue
        elif choice.lower() == 'r':
            mainReg()
            retry = input('Quer fazer mais uma ação?(s/n) ')
            if retry.lower() == 'n':
                _ = False
                print('Ok, Até mais ver!')
            else:
                continue
        elif choice.lower() == 'a':
            allocation()
            retry = input('Quer fazer mais uma ação?(s/n) ')
            if retry.lower() == 'n':
                _ = False
                print('Ok, Até mais ver!')
            else:
                continue
        elif choice.lower() == 'd': 
            while _:
                choicedelete = input('deseja uma disciplina (D) ou uma turma (T)? ')
                if choicedelete.lower() == 'd':
                    delete('disciplinas')
                elif choicedelete.lower() == 't':
                    delete('Turmas')
                else:
                    print('operação invalida')
                    continue
                retry = input('Quer fazer mais uma ação?(s/n) ')
                if retry.lower() == 'n':
                    _ = False
                    print('Ok, Até mais ver!')
                else:
                    continue
        elif choice.lower() == 's':
            system('cls')
            print('até logo!')
            _ = False
           
        else:
            print('operação inválida')
            continue
elif studentOrTeacher == 'aluno' or 'A':
    print('bem vindo!')
    while _:
        choice = input('Deseja pesquisar algo? (s/n)')
        if choice == 's':
            mainSearch()
            retry = input('Quer fazer mais uma ação?(s/n) ')
            if retry.lower() == 'n':
                _ = False
                print('Ok, Até mais ver!')
            else:
                continue    
        else:
            print('ok, até mais ver!')
            _ = False