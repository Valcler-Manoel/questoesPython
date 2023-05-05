import unittest

# Dado um lista de strings `words`, retornar o total de strings
# se cada palavra for maior ou igual a dois e
# se o primeiro caracter coincidir com o último
def match_ends(words):
  total = 0 # Definindo o valor inicial da varíavel 'total' para 0.
  for palavra in words:
    quantidadeLetras = len(palavra) # Leitura da quantidade de caracteres
    if quantidadeLetras >= 2: # Se a quantidade for maior ou igual a 2,
      primeiraletra = palavra[0] # Armazene o primeiro e o último caractere.
      ultimaLetra = palavra[-1]
      if primeiraletra == ultimaLetra: # Se o primeiro e último caractere forem iguais,
        total = total + 1              # igualará as duas variáveis 'total', que, inicialmente
                                       # seu valor é 0 e acrescentará +1 caso a igualdade ocorrer.
  return total

# Dado uma lista de strings, retornar uma lista de string ordenadas,
# exceto todo grupo de strings que comece com "x" virá primeiro.
#
# Dica: isto pode ser feito com 2 listas ordenando cada uma delas e
# depois combinado-as. Veja os testes para maiores detalhes.
def front_x(words):
  listaX = [] # Lista criada para armazenar as strings com X
  lista2 = [] # Lista para armazenar o resto
  for palavra in words:
    if palavra.startswith('x'):
      listaX.append(palavra)
    else:
      lista2.append(palavra)
  return sorted(listaX) + sorted(lista2) # Ordenação e combinação das listas.

# Dado uma lista de tuplas não vazias, retornar uma lista ordenada
# pelo último elemento de cada tupla.
#
# Dica: use um função personalizada `last()` para extrair
# o último elemento, ela deve ser passada no segundo parâmetro
# da função sorted()
def sort_last(tuples):
  return sorted(tuples, key=last) # Retorno da lista ordenada pelo último elemento de cada tupla
                                  # por meio do método key, fazendo justamente essa comparação em cada
                                  # componente da lista.
def last(a):
  return a[-1] # Retorno do último elemento

class MyTest(unittest.TestCase):
  def test_match_ends(self):
    self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1)


  def test_front_x(self):
    self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

  def test_sort_last(self):
     self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
     self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
     self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

if __name__ == '__main__':
  unittest.main()