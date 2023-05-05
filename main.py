import unittest

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
def both_ends(both_ends):
    both_ends [0:2] + both_ends[-2] + both_ends[-1]
    return {both_ends}



def test_fix_start(self):
 self.assertEqual(both_ends('xy'), 'xyxy')

 if __name__ == "__main__":
  # Questão 1
  unittest.main()