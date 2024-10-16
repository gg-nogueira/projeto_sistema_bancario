from criar_usuario import criar_usuario
from exibir_menu import exibir_menu
from movimentar_conta import depositar, sacar, exibir_extrato

# Programa principal
usuarios = {}

while True:
    print("""\n=== Bem-vindo ao Banco GAN ===
    1- Criar conta
    2- Acessar conta
    3- Encerrar\n""")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == '1':
        criar_usuario(usuarios)

    elif opcao == '2':
        cpf = input("Digite o CPF do usuário: ").strip()

        if cpf not in usuarios:
            print("Erro! Usuário não encontrado.")
        else:
            senha = input("Digite sua senha: ").strip()
            if senha != usuarios[cpf]['senha']:
                print("Erro! Senha incorreta.")
            else:
                print(f"Bem-vindo, {usuarios[cpf]['nome']}. Acessando sua conta...")
                conta = usuarios[cpf]['conta']
                confirmacao=usuarios[cpf]['senha']

                while True:
                    escolha = exibir_menu()
                    if escolha == '1':
                        depositar(conta, confirmacao)
                    elif escolha == '2':
                        sacar(conta, confirmacao)
                    elif escolha == '3':
                        exibir_extrato(conta)
                    elif escolha == '4':
                        print("Encerrando o acesso à conta.")
                        break
                    else:
                        print("Opção inválida!")

    elif opcao == '3':
        print("Obrigado por usar o Banco GAN. Até mais!")
        break

    else:
        print("Opção inválida!")
