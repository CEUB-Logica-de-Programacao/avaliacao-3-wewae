# Avaliação 3

## Questão 1

Você foi contratado pela seleção brasileira para fazer uma análise sobre as seleções adversárias. Sua primeira tarefa
consiste em realizar uma contagem de quantos jogadores possuem a altura máxima.

### Exemplo

Para a entrada:

```
[180, 166, 170, 180]
```

A saída deve ser:

```
2
```

Isso porque existem dois jogadores com altura máxima (180).

Para obter a nota máxima dessa questão, deve-se utilizar apenas um ``for`` e nenhuma função pronta do Python.

## Questão 2

Estão testando seus conhecimentos matemáticos. Você irá receber um valor de começo e um valor de fim. Você deve
encontrar todos os números que são quadrados perfeitos entre esses valores. Um quadrado perfeito é um número inteiro
que pode ser expresso como o quadrado de outro número inteiro. Por exemplo, 9 é um quadrado perfeito, pois 3² = 9.

### Exemplo

Para a entrada:

```
1 9
```

A saída deve ser:

```
1 4 9
```

Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

## Questão 3

Dado uma sequência de números inteiros, uma trinca a[i], a[j], a[k] é perfeita se:

* a[i] < a[j] < a[k]
* a[j] - a[i] = a[k] - a[j] = d

Dado um valor de ``d``, você deve encontrar a quantidade de trincas perfeitas.

### Exemplo

Para a entrada:

```
arr = [1, 2, 4, 5, 7, 8, 10]
d = 3
```

A saída deve ser:

```
3
```

Isso porque existem apenas três trincas perfeitas:

* (1, 4, 7)
* (2, 5, 8)
* (4, 7, 10)

Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

## Questão 4

Você receberá uma string em [CamelCase](https://en.wikipedia.org/wiki/CamelCase). Ela possuí as seguintes propriedades:

* É a concatenação de uma ou mais palavras, onde a primeira letra de cada palavra é maiúscula, e as demais são
  minúsculas.
* Não contém espaços, números ou caracteres especiais.

Você deverá retornar o número de palavras na string.

### Exemplo

Para a entrada:

```
hexaVemEsseAno
```

A saída deve ser:

```
4
```

Isso porque a string possui 4 palavras: ``hexa``, ``Vem``, ``Esse`` e ``Ano``.

Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

## Questão 5

Sherlock considera uma string válida se todos os caracteres dela aparecerem o mesmo número de vezes.
Também é válida se ele puder remover apenas um caractere, e os caracteres restantes aparecerem o
mesmo número de vezes. Dada uma cadeia de caracteres, determine se ela é válida. Se for o caso, retorne `True`, caso
contrário retorne `False`.

### Exemplo

Para a entrada:

```
aabbcd
```

A saída deve ser:

```
False
```

Isso porque não é possível remover apenas um caractere para tornar a string válida.

Para a entrada:

```
abc
```

A saída deve ser:

```
True
```

Isso porque é possível remover apenas um caractere para tornar a string válida.

Para a entrada:

```
abcc
```

A saída deve ser:

```
True
```

Isso porque é possível remover apenas um caractere para tornar a string válida.

Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

## Desafio

Dados ``n`` pares de parênteses, escreva uma função para gerar todas as combinações de parênteses bem formados.

### Exemplo

Para a entrada:

```
n = 3
```

A saída deve ser:

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.