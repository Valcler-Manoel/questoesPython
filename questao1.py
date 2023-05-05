import unittest

# Dado um `count` como sendo o números de donuts, retornar uma string
# na forma "Número de donuts: <count>", caso `count` seja
# maior ou igual a 10 retornar "many".
def donuts(count):
    if count >= 10: # Informando uma condição para a quantidade de donuts.
        return 'Number of donuts: many' # Retornará many caso o valor for maior ou igual a 10.
    else:
        return f'Number of donuts: {count}' # Retornará o valor de count

# Outra versão
def donutsV2(count):
    return f'Number of donuts: {count if count < 10 else "many"}' # Versão reduzida da primeira forma

# Dado uma string qualquer `s`, retonar uma string
# composta dos 2 primeiros e os 2 últimos caracteres, exemplo:
#
# panela ----> pala
# bala   ----> bala
# mao    ----> maao
# ja     ----> jaja
#
# Caso a string `s` contenha menos que 2 caracteres,
# retornar "" (string de cumprimento zero).
def both_ends(s):
    if len(s) < 2: # Se a string conter menos de 2 letras, retorne 0.
        return ""
    else:
        doisprimeiros = s[:2] # Coletará os dois primeiros caracteres.
        doisultimos = s[-2:] # Coletarará os dois últimos caracteres.
        return doisprimeiros + doisultimos # Retornara os caracteres coletados anteriormente.

# Dado uma string `s`, retornar uma string onde
# todas as ocorrências de seu primeiro caractere
# seja alterado para '*', exceto o primeiro caracter. Exemplo:
#
# babble ---> ba**le
#
# Presuma que o tamanho da string seja 1 ou mais.
# Dica: s.replace (strA, strB) retorna uma versão da string s
def fix_start(s):
    primeiro = s[0] # Armazenará o primeiro caractere.
    resto = s[1:] # Resto dos caracteres.
    stringfinal = resto.replace(primeiro, '*') # Usará a função replace para adicionar o sinal '*'.
    return primeiro + stringfinal


# Dado duas string `a` e `b`,  trocar os 2 primeiros caracteres entre as variáveis
# e retornar uma única string separada por espaço como no exemplo:
#
# "pezzy", "firm" ----> "fizzy perm"
def mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    result = new_a + ' ' + new_b
    return result




class MyTest(unittest.TestCase):

    def test_donuts(self):
      self.assertEqual(donuts(4), 'Number of donuts: 4')
      self.assertEqual(donuts(9), 'Number of donuts: 9')
      self.assertEqual(donuts(10), 'Number of donuts: many')
      self.assertEqual(donuts(99), 'Number of donuts: many')


    def test_fix_start(self):
      self.assertEqual(both_ends('xy'), 'xyxy')
      self.assertEqual(fix_start('babble'), 'ba**le')
      self.assertEqual(fix_start('aardvark'), 'a*rdv*rk')
      self.assertEqual(fix_start('google'), 'goo*le')
      self.assertEqual(fix_start('donut'), 'donut')


    def test_mix_up(self):
       self.assertEqual(mix_up('mix', 'pod'), 'pox mid')
       self.assertEqual(mix_up('dog', 'dinner'), 'dig donner')
       self.assertEqual(mix_up('gnash', 'sport'), 'spash gnort')
       self.assertEqual(mix_up('pezzy', 'firm'), 'fizzy perm')



if __name__=="__main__":
    #Questão 1
    unittest.main()