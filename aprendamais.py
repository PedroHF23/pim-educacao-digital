import json
import os

arquivos_usuario = "usuarios.json"
cursos = ["Python", "TIC", "Cybersegurança", "LGPD"]

def pega_os_usuarios():
    if os.path.exists(arquivos_usuario):
        with open(arquivos_usuario, "r") as arquivo:
            try:
                dados = json.load(arquivo)
            except json.JSONDecodeError:
                return []
        return dados
    else:
        return []

def salva_os_usuarios(a_lista):
    with open(arquivos_usuario, "w") as arquivo:
        json.dump(a_lista, arquivo)

def cria_novo_usuario():
    nome_do_aluno = input("Qual seu nome? ")
    email = input("Seu e-mail, por favor: ")
    senha = input("Cria uma senha aí: ")

    alunos_cadastrados = pega_os_usuarios()

    for usuario in alunos_cadastrados:
        if usuario.get("email") == email:
            print("Opa, esse e-mail já tá cadastrado!")
            return

    novo_usuario = {
        "nome": nome_do_aluno,
        "email": email,
        "senha": senha,
        "progresso": {curso: "Não iniciado" for curso in cursos}
    }

    alunos_cadastrados.append(novo_usuario)
    salva_os_usuarios(alunos_cadastrados)
    print("Beleza! Usuário cadastrado com sucesso!")

def fazer_login():
    email = input("Qual seu e-mail? ")
    senha = input("E a senha? ")

    alunos = pega_os_usuarios()

    for um_usuario in alunos:
        if um_usuario.get("email") == email and um_usuario.get("senha") == senha:
            print("Aí sim! Login feito.")
            area_do_usuario(um_usuario, alunos)
            return
    print("Hmm, e-mail ou senha incorretos. Tenta de novo?")

def area_do_usuario(usuario_logado, lista_de_todos):
    while True:
        print("\n~~~ Área do aluno ~~~")
        print("1. Ver os cursos")
        print("2. Marcar um curso como concluído")
        print("3. Sair ")

        opcao_escolhida = input("O que você quer fazer? ")

        if opcao_escolhida == "1":
            print("\nSeus cursos:")
            for curso, status in usuario_logado.get("progresso", {}).items():
                print(f"- {curso}: {status}")

        elif opcao_escolhida == "2":
            qual_curso = input("Qual o nome do curso que você terminou? ")
            if qual_curso in usuario_logado.get("progresso", {}):
                usuario_logado["progresso"][qual_curso] = "Concluído!"
                salva_os_usuarios(lista_de_todos)
                print("Show! Curso marcado como concluído.")
            else:
                print("Esse curso não tá na sua lista.")

        elif opcao_escolhida == "3":
            print("Obrigado por estudar conosco, até a próxima!")
            break
        else:
            print("Essa opção não existe. Escolha outra.")

def principal():
    while True:
        print("\n   Plataforma Aprenda+   ")
        print("1. Cadastrar")
        print("2. Entrar")
        print("3. Sair")

        escolha_principal = input("O que você vai fazer agora? ")

        if escolha_principal == "1":
            cria_novo_usuario()
        elif escolha_principal == "2":
            fazer_login()
        elif escolha_principal == "3":
            print("Falou! Até mais.")
            break
        else:
            print("Essa não vale! Escolhe 1, 2 ou 3.")

if __name__ == "__main__":
    principal()
