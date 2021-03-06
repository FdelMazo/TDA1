import unittest
from verificacionDeRotacionCiclica import hayRotacionCiclica
from verificacionDeRotacionCiclicaConKMP import hayRotacionCiclicaConKMP
from verificacionDeRotacionCiclicaMejorada import hayRotacionCiclicaMejorada

class PruebaEsRotacionCiclica(unittest.TestCase):

	def test_dos_cadenas_que_no_son_de_rotacion_ciclica_no_son_rotacion_ciclica(self):
		self.assertFalse(hayRotacionCiclica("ja","je"))

	def test_dos_cadenas_que_no_son_de_rotacion_ciclica_no_son_rotacion_ciclica2(self):
		self.assertFalse(hayRotacionCiclica("a","b"))
	
	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica(self):
		self.assertTrue(hayRotacionCiclica("DABRAABRACA","ABRACADABRA"))  

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica2(self):
		self.assertTrue(hayRotacionCiclica("hola","ahol")) 
		
	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica3(self):
		self.assertTrue(hayRotacionCiclica("ABRACADABRA","DABRAABRACA"))  

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica4(self):
		self.assertTrue(hayRotacionCiclica("ahol","hola")) 

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica5(self):
		self.assertTrue(hayRotacionCiclica("jaja","ajaj"))

	def test_rotacion_ciclica_acepta_iguales(self):
		self.assertTrue(hayRotacionCiclica("nombre","nombre"))

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica6(self):
		self.assertTrue(hayRotacionCiclica("abcdef","defabc"))

	def test_dos_cadenas_que_no_son_de_rotacion_ciclica_no_son_rotacion_ciclica3(self):
		self.assertFalse(hayRotacionCiclica("cabdef","abcdef"))
		
	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica7(self):
		self.assertTrue(hayRotacionCiclica("rotado","adorot"))
	
	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica8(self):
		self.assertTrue(hayRotacionCiclica("abracadabra","cadabraabra"))

	def test_dos_cadenas_que_no_son_de_rotacion_ciclica_no_son_rotacion_ciclica4(self):
		self.assertFalse(hayRotacionCiclica("abracadabra","dacabraarba"))

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica9(self):
		self.assertTrue(hayRotacionCiclica("parador","dorpara"))

	def test_rotacion_ciclica_no_acepta_anagramas(self):
		self.assertFalse(hayRotacionCiclica("raymaginer","imaginary"))


class PruebaEsRotacionCiclicaConKRM(unittest.TestCase):
	
	def test_dos_cadenas_que_no_son_de_rotacion_ciclica_no_son_rotacion_ciclica(self):
		self.assertFalse(hayRotacionCiclicaConKMP("ja","je"))

	def test_dos_cadenas_que_no_son_de_rotacion_ciclica_no_son_rotacion_ciclica2(self):
		self.assertFalse(hayRotacionCiclicaConKMP("a","b"))
	
	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica(self):
		self.assertTrue(hayRotacionCiclicaConKMP("DABRAABRACA","ABRACADABRA"))  

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica2(self):
		self.assertTrue(hayRotacionCiclicaConKMP("hola","ahol")) 
		
	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica3(self):
		self.assertTrue(hayRotacionCiclicaConKMP("ABRACADABRA","DABRAABRACA"))  

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica4(self):
		self.assertTrue(hayRotacionCiclicaConKMP("ahol","hola")) 

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica5(self):
		self.assertTrue(hayRotacionCiclicaConKMP("jaja","ajaj"))

	def test_rotacion_ciclica_acepta_iguales(self):
		self.assertTrue(hayRotacionCiclicaConKMP("nombre","nombre"))

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica6(self):
		self.assertTrue(hayRotacionCiclicaConKMP("abcdef","defabc"))

	def test_dos_cadenas_que_no_son_de_rotacion_ciclica_no_son_rotacion_ciclica3(self):
		self.assertFalse(hayRotacionCiclicaConKMP("cabdef","abcdef"))
		
	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica7(self):
		self.assertTrue(hayRotacionCiclicaConKMP("rotado","adorot"))
	
	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica8(self):
		self.assertTrue(hayRotacionCiclicaConKMP("abracadabra","cadabraabra"))

	def test_dos_cadenas_que_no_son_de_rotacion_ciclica_no_son_rotacion_ciclica4(self):
		self.assertFalse(hayRotacionCiclicaConKMP("abracadabra","dacabraarba"))

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica9(self):
		self.assertTrue(hayRotacionCiclicaConKMP("parador","dorpara"))

	def test_rotacion_ciclica_no_acepta_anagramas(self):
		self.assertFalse(hayRotacionCiclicaConKMP("raymaginer","imaginary"))
	
	
class PruebaEsRotacionCiclicaMejorada(unittest.TestCase):
	def test_dos_cadenas_que_no_son_de_rotacion_ciclica_no_son_rotacion_ciclica(self):
		self.assertFalse(hayRotacionCiclicaMejorada("ja","je"))

	def test_dos_cadenas_que_no_son_de_rotacion_ciclica_no_son_rotacion_ciclica2(self):
		self.assertFalse(hayRotacionCiclicaMejorada("a","b"))
	
	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica(self):
		self.assertTrue(hayRotacionCiclicaMejorada("DABRAABRACA","ABRACADABRA"))  

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica2(self):
		self.assertTrue(hayRotacionCiclicaMejorada("hola","ahol")) 
		
	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica3(self):
		self.assertTrue(hayRotacionCiclicaMejorada("ABRACADABRA","DABRAABRACA"))  

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica4(self):
		self.assertTrue(hayRotacionCiclicaMejorada("ahol","hola")) 

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica5(self):
		self.assertTrue(hayRotacionCiclicaMejorada("jaja","ajaj"))

	def test_rotacion_ciclica_acepta_iguales(self):
		self.assertTrue(hayRotacionCiclicaMejorada("nombre","nombre"))

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica6(self):
		self.assertTrue(hayRotacionCiclicaMejorada("abcdef","defabc"))

	def test_dos_cadenas_que_no_son_de_rotacion_ciclica_no_son_rotacion_ciclica3(self):
		self.assertFalse(hayRotacionCiclicaMejorada("cabdef","abcdef"))
		
	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica7(self):
		self.assertTrue(hayRotacionCiclicaMejorada("rotado","adorot"))
	
	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica8(self):
		self.assertTrue(hayRotacionCiclicaMejorada("abracadabra","cadabraabra"))

	def test_dos_cadenas_que_no_son_de_rotacion_ciclica_no_son_rotacion_ciclica4(self):
		self.assertFalse(hayRotacionCiclicaMejorada("abracadabra","dacabraarba"))

	def test_dos_cadenas_de_rotacion_ciclica_son_rotacionCiclica9(self):
		self.assertTrue(hayRotacionCiclicaMejorada("parador","dorpara"))

	def test_rotacion_ciclica_no_acepta_anagramas(self):
		self.assertFalse(hayRotacionCiclicaMejorada("raymaginer","imaginary"))

'''Forma de ejecutar según la doc. de python'''  
if __name__ == '__main__':
	unittest.main()
	'''suite = unittest.TestLoader().loadTestsFromTestCase(PruebaEsRotacionCiclica)
	unittest.TextTestRunner(verbosity=2).run(suite)'''
	
