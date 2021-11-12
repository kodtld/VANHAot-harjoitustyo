import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10.00)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_saldon_lisääminen_onnistuu(self):
        self.maksukortti.lataa_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.15")

    def test_saldon_ottaminen_onnistuu_jos_raha_riittaa(self):
                
        self.assertTrue(self.maksukortti.ota_rahaa(5))

    def test_saldo_ei_vahene_jos_raha_ei_riita(self):
       
        self.assertFalse(self.maksukortti.ota_rahaa(12))

