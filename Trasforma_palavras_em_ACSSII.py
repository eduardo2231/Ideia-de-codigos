import pyfiglet

print(pyfiglet.FigletFont.getFonts())

storage = dict()

def salvar(nomes, fontes):
    storage[nomes] = fontes                    # storage.get(nomes, fontes) Isso esta errado. O get estava pegando um valor e nao atribuia nada nada

while True:
    print('Digite "Quit" para sair ou "Ver" para ver seus saves.')

    name = input("Digite seu nome: ")
    if name.lower == 'Quit': break
    if name.lower == 'Ver':
        print(storage)
        continue

    font = input("Digite sua fonte: ")
    if font.lower == 'quit': break

    ascii_art = pyfiglet.figlet_format(name, font)
    print(ascii_art)

    salvar_fonte_name = input('Deseja salvar: Y/N ')

    if salvar_fonte_name == 'Y' or salvar_fonte_name == 'y':
        print('Salvando...')
        salvar(name, font)
    elif salvar_fonte_name == 'N' or salvar_fonte_name == 'n':
        print('Saindo...')
        break


