import unittest
from HUMANGI import *
from Excepciones import *
import main

"""
ESTE TESTING FUE PROBADO CON LOS DATOS DEL TEST 0

"""



class Chequeos(unittest.TestCase):

    def setUp(self):
        self.nombres = todos
        self.todo = self.nombres[0]

    def tearDown(self):
        pass

    def test_ascendencia(self):
        self.assertIsInstance(ascendencia(self.nombres[0]), list)
        self.assertNotIsInstance(ascendencia(self.nombres[0]), int)

    def test_indice_de_tamano(self):
        self.assertAlmostEqual(indice_de_tamano(self.nombres[0]),
                                                [0.5883484054145521])

    def test_pariente_de(self):
        self.assertIsNotNone(pariente_de(0, "Hernán Valdivieso"))

    def test_gemelo_genetico(self):
        self.assertEqual(gemelo_identico("Hernán Valdivieso"), 'Marcelo Lagos')

    def test_valor_caracteristica(self):
        self.assertEqual(valor_caracteristica("AAG", self.nombres[0]), 1.75)

    def test_maximo(self):
        self.assertNotEqual(maximo('CTC'), 50)

    def test_minimo(self):
        self.assertEqual(minimo("AAG"), 1.4)

    def test_promedio(self):
        self.assertAlmostEqual(prom("AAG"), 1.72222222222222)
        self.assertNotIsInstance(ascendencia(self.nombres[0]), str)

    def test_BadRequest(self):
        with self.assertRaises(BadRequest):
            bad("asendenc")

    def test_NotFound(self):
        with self.assertRaises(NotFound):
            notf("ascendencia", "Pedro", "Altura")
        
    def test_NotAcceptable(self):
        with self.assertRaises(NotAcceptable):
            nota("El Chuña")
        
    def test_GenomeError(self):
        with self.assertRaises(GenomeError):
            geno("AACTAAACF")


suite = unittest.TestLoader().loadTestsFromTestCase(Chequeos)
unittest.TextTestRunner().run(suite)