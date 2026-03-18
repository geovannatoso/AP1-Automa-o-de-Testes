import unittest

def verificar_imc(nome, peso, altura):

    if not isinstance(peso, (int, float)):
        raise TypeError('Peso só pode ser número: inteiro ou ponto flutuante.')

    if not isinstance(altura, (int, float)):
        raise TypeError('Altura só pode ser número: inteiro ou ponto flutuante.')

    imc = peso / (altura ** 2)

    if imc < 18.5:
        return (f'{nome} está abaixo do peso.')
    elif imc < 25:
        return (f'{nome} está com peso normal.')
    elif imc < 30:
        return (f'{nome} está com sobrepeso.')
    elif imc < 35:
        return (f'{nome} está com obesidade grau I.')
    elif imc < 40:
        return (f'{nome} está com obesidade grau II.')
    else:
        return (f'{nome} está com obesidade grau III.')

class Avaliar_imc(unittest.TestCase):

    def test_erro_peso_str(self):
        with self.assertRaises(TypeError):
            (verificar_imc('Geovanna','52.8',165.8), 'Peso só pode ser número: inteiro ou ponto flutuante.')
    
    def test_erro_altura_str(self):
        with self.assertRaises(TypeError):
            (verificar_imc('Geovanna',52.8,'165.8'), 'Altura só pode ser número: inteiro ou ponto flutuante.')

    def test_abaixo_do_peso(self):
        self.assertEqual(verificar_imc('Geovanna',52.8,165.8), 'Geovanna está abaixo do peso.')

    def test_peso_normal(self):
        self.assertEqual(verificar_imc('Geovanna', 60, 1.65), 'Geovanna está com peso normal.')

    def test_sobrepeso(self):
        self.assertEqual(verificar_imc('Geovanna', 78, 1.70), 'Geovanna está com sobrepeso.')

    def test_obesidade_gau1(self):
        self.assertEqual(verificar_imc('Geovanna', 92, 1.70), 'Geovanna está com obesidade grau I.')

    def test_obesidade_grau2(self):
        self.assertEqual(verificar_imc('Geovanna', 105, 1.70), 'Geovanna está com obesidade grau II.')
    
    def test_obesidade_grau3(self):
        self.assertEqual(verificar_imc('Geovanna', 120, 1.70), 'Geovanna está com obesidade grau III.')

if __name__ == '__main__':
    unittest.main()

