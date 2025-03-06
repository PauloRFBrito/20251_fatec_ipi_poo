def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / belse:
    return "Divisão por 0 não permitida!"

def menu():
    while True:
        print("Escolha uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")

        opcao = input("Digite apenas o número da opção desejada: ")

        if opcao == '0':
            print("Obrigado por utilizar o software!")
            break

        if opcao in ['1', '2', '3', '4']:
            try:
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))

               if opcao == '1':
                    print(f"O resultado da soma é: {somar(n1, n2)}")
                elif opcao == '2':
                    print(f"O resultado da subtração é: {subtrair(n1, n2)}")
                elif opcao == '3':
                    print(f"O resultado da multiplicação é: {multiplicar(n1, n2)}")
                elif opcao == '4':
                    print(f"O resultado da divisão é: {dividir(n1, n2)}")
        
            except ValueError:
            print("Insira valores válidos!")
        else:
            print("Opção inválida, execute o software novamente.") 

menu()