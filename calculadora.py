while True:
    print('Seja bem vindo a calculadora !!')
    num1 = int(input('Por favor, digite um valor: '))
    num2 = int(input('Agora, digite outro valor: '))
    print()

    print('[1] Adição::       \n[2] Multiplicação::'
        '\n[3] Divisão::      \n[4] Subtração::'
        '\n[5] Novos números::\n[6] Sair do programa::')

    menu = input('Selecione uma dessa opções, por favor: ')
    print()
    
    if menu == '5':
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
        print('[1] Adição::       \n[2] Multiplicação::'
            '\n[3] Divisão::      \n[4] Subtração::'
            '\n[5] Novos números::\n[6] Sair do programa::')

    menu = input('Selecione uma dessa opções, por favor: ')
    print()

    if menu == '1':
        print(f'O resultado é {num1 + num2}.')
        print()
    if menu == '4':
        print(f'O resultado é {num1 - num2}.')
        print()
    if menu == '2':
        print(f'O resultado é {num1 * num2}.')
        print()
    if menu == '3':
        print(f'O resultado é {num1 / num2}.')
        print()

    if menu == '6':
        print('Obrigado por ter utilizado.')     
        break