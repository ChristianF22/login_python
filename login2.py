usuarios = {}

def cadastrar():
    global usuarios
    usuario = input("Digite um nome de usuário: ")

   
    if usuario in usuarios:
        print("Usuário já existe. Tente outro nome de usuário.")
        return

    senha1 = input("Digite sua senha: ")
    senha2 = input("Confirme sua senha: ")

    if senha1 == senha2:
        usuarios[usuario] = senha1
        print("Cadastro realizado com sucesso!")
    else:
        print("As senhas não coincidem. Tente novamente.")

def login():
    global usuarios
    usuario = input("Digite seu nome de usuário: ")

    if usuario not in usuarios:
        print("Usuário não encontrado. Cadastre-se primeiro.")
        return

    senha_correta = usuarios[usuario]
    tentativas = 0

    while tentativas < 3:
        senha = input("Digite sua senha: ")

        if senha == senha_correta:
            print("Login bem-sucedido!")
            return
        else:
            tentativas += 1
            print(f"Senha incorreta. Tentativas restantes: {3 - tentativas}")

    print("Você excedeu o número máximo de tentativas. Sua conta está bloqueada.")
    del usuarios[usuario]  

while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")
    opcao = input()

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        login()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")