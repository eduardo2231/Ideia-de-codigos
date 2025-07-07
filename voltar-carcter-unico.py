

print('''----------Desafio----------''')

def contar_unicos(valor):
    dic = dict()
    palavra = list(valor)
    for i in palavra:
        dic[i] = dic.get(i, 0) + 1
    unicos = 0
    for letra, contagem in dic.items():
        if contagem == 1:
            unicos += 1
    print(f"Número de caracteres únicos: {unicos}")
    return unicos


helo = input("Digite algo: ")
contar_unicos(helo)


# contar_unicos("banana")  # Deve retornar 1, porque só o "b" aparece uma vez.
# contar_unicos("abcabc")  # Deve retornar 0, todos aparecem mais de uma vez.
# contar_unicos("python")  # Deve retornar 6, todos aparecem só uma vez.
