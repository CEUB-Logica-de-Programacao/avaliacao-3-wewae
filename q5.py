# ## Questão 5
#
# Sherlock considera uma string válida se todos os caracteres dela aparecerem o mesmo número de vezes.
# Também é válida se ele puder remover apenas um caractere, e os caracteres restantes aparecerem o
# mesmo número de vezes. Dada uma cadeia de caracteres, determine se ela é válida. Se for o caso, retorne `True`, caso
# contrário retorne `False`.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# aabbcd
# ```
#
# A saída deve ser:
#
# ```
# False
# ```
#
# Isso porque não é possível remover apenas um caractere para tornar a string válida.
#
# Para a entrada:
#
# ```
# abc
# ```
#
# A saída deve ser:
#
# ```
# True
# ```
#
# Isso porque é possível remover apenas um caractere para tornar a string válida.
#
# Para a entrada:
#
# ```
# abcc
# ```
#
# A saída deve ser:
#
# ```
# True
# ```
#
# Isso porque é possível remover apenas um caractere para tornar a string válida.
#
# Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

def q5(s):
    # Escreva seu código aqui
    return False
CHARS = 26


	
def isValidString(str):

	freq = [0]*CHARS

	
	for i in range(len(str)):
		freq[ord(str[i])-ord('a')] += 1


	freq1 = 0
	count_freq1 = 0
	for i in range(CHARS):
	
		if (freq[i] != 0):
		
			freq1 = freq[i]
			count_freq1 = 1
			break


	freq2 = 0
	count_freq2 = 0
	for j in range(i+1,CHARS):
	
		if (freq[j] != 0):
	
			if (freq[j] == freq1):
				count_freq1 += 1
			else:
			
				count_freq2 = 1
				freq2 = freq[j]
				break


	for k in range(j+1,CHARS):
	
		if (freq[k] != 0):
		
			if (freq[k] == freq1):
				count_freq1 += 1
			if (freq[k] == freq2):
				count_freq2 += 1

			
			else:
				return False

	
		if (count_freq1 > 1 and count_freq2 > 1):
			return False

	
	return True


if __name__ == "__main__":
	str= "aabbcd"

	if (isValidString(str)):
		print("True")
	else:
		print("False")
		

if __name__ == '__main__':
    print(q5('abcc'))
