# ## Questão 4
#
# Você receberá uma string em [CamelCase](https://en.wikipedia.org/wiki/CamelCase). Ela possuí as seguintes propriedades:
#
# * É a concatenação de uma ou mais palavras, onde a primeira letra de cada palavra é maiúscula, e as demais são
#   minúsculas.
# * Não contém espaços, números ou caracteres especiais.
#
# Você deverá retornar o número de palavras na string.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# hexaVemEsseAno
# ```
#
# A saída deve ser:
#
# ```
# 4
# ```
#
# Isso porque a string possui 4 palavras: ``hexa``, ``Vem``, ``Esse`` e ``Ano``.
#
# Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

def q4(s):
    L = list(s)
    if len(L) == 0:
        return 0
    C = 1 
    for I in range(len(L)):
        if L[I].isupper():
            C = C + 1
        if L[I] == ' ':
            C = C - 1
    return C

if __name__ == '__main__':
    print(q4('hexaVemEsseAno'))
