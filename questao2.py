import unittest

def verbing(s):
    if len(s) >= 3: # Se possui mais que 3 letras:.
        if s[-3:] != 'ing': # Se os últimos 3 caracteres forem difentes de 'ing', adicionará 'ing'.
            s += 'ing'
        elif s[-3:] == 'ing': # Se os 3 últimos caracteres forem iguais a 'ing', adicionará 'ly'.
            s += 'ly'
    return s



# Dado um astring, procurar a primeira ocorrência da substring 'not' e 'bad'
# Se 'bad' vier após o 'not'
# substituir todo o trecho "not ... bad" por 'good'
# Retorne a string resultante.
def not_bad(s):
    notx = s.find('not')    # Armazenando o índice da substring 'not' em uma determinada frase.
    badx = s.find('bad')    # Armazenando o índice da substring 'bad' em uma determinada frase.
    if badx > notx: # Se a susbtring 'bad' vier após 'not'
        s = s.replace(s[notx:badx + 3], 'good') # s será relocado de not até bad +3 para incluir a substring 'bad'.
    return s

# Considere dividir uma string em duas metades.
# Se o comprimento for par, a parte da frente (front) e a parte de trás (back) são do mesmo tamanho.
# Se o comprimento for ímpar, o caracter extra irá para a parte da frente.
#
# Dado 2 strings, 'a' e 'b', retornar um string na forma
# a front + b front + a back + b back
def front_back(a, b):
    a_meio = (len(a) + 1) // 2
    b_meio = (len(b) + 1) // 2
    return a[:a_meio] + b[:b_meio] + a[a_meio:] + b[b_meio:]

class MyTest(unittest.TestCase):

  def test_verbing(self):
    self.assertEqual(verbing('hail'), 'hailing')
    self.assertEqual(verbing('swiming'), 'swimingly')
    self.assertEqual(verbing('do'), 'do')

  def test_not_bad(self):
    self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good')
    self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
    self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")


  def test_front_back(self):
    self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
    self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
    self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  unittest.main()