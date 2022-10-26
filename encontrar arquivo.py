import os

caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo: ')

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    
    if tamanho < kilo:
        texto = 'Bites'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'Kbites'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'Megabites'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'GigaBites'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'Terabites'
                
    tamanho = round(tamanho, 3)
    return f'{tamanho} {texto}'.replace('.', ',')
        

contador = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contador = contador + 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
            
                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão: ', ext_arquivo)
                print('Tamanho: ', tamanho)
                print('Tamanho Formatado: ', formata_tamanho(tamanho))
            except PermissionError as e:
                print('Sem permissões.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido: ', e)
print()
print(f'{contador} arquivo(s) encontrado(s).') 