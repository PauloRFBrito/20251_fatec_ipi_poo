import calculadora

def menu():
    while True:
        print("\n---- MENU ----")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")

        opcao = input("Selecione uma opção: \n")

        if opcao == "0":
            print("Encerando a aplicação!")
            break
    
         if opcao in ["1", "2", "3", "4"]:
            try:
                a = float(input("Digite o primeiro valor: \n"))
                b = float(input("Digite o segundo valor: \n"))

                if opcao == "1":
                    print("Resultado: \n", calculadora.somar(a, b))
                elif opcao == "2":
                    print("Resultado: \n", calculadora.subtrair(a, b))
                elif opcao == "3":
                    print("Resultado: \n", calculadora.multiplicar(a, b))
               
        else:
            print("Opção inválida, tente novamente!\n")

