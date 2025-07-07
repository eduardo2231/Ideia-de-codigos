
print('''----------Desafio----------''')

def numbr(st):
    sting = st
    return sting[::-1]

enter = input("Numeros:")
resultado = numbr(enter)
print(f"Resultado invertido: {resultado}.")

#112233

# Quando usamos reversed(string), o Python retorna um objeto iterador,
# que não é uma string pronta para mostrar. Por isso, precisamos usar
# ''.join(...) para transformar esse iterador em uma string de verdade.

# Já o slicing com string[::-1] cria e retorna uma nova string invertida
# diretamente, sem precisar de transformação extra.

# Por isso, para inverter uma string e imprimir o resultado, usar string[::-1]
# é mais simples e direto.

