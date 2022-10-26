while True:
    select_temp = input('Informe qual temperatura deseja calcular: Kº, Cº ou Fº ? ')

    if select_temp == 'C'.lower():
        temp_f = int(input('Informe a temperatura em Fº: '))
        temp_c = ( temp_f - 32 ) / 1.8
        print(f'Sua temperatura em Celsius é de {temp_c:.2f}º')

    elif select_temp == 'F'.lower():
        temp_c = int(input('Informe a temperatura em Cº: '))
        temp_f = ( temp_c * 1.8) + 32
        print(f'Sua temperatura em Fahrenheit é de {temp_f:.2f}º')

    elif select_temp == 'K'.lower():
        temp_c = int(input('Informe a temperatura em Cº: '))
        temp_k = temp_c + 273.73
        print(f'Sua temperatura em Kelvin é {temp_k:.2f}º')
    else:
        print('Selecione somente uma das opções exibidas.')