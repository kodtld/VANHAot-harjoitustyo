import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

# Alkutilanne

    def test_alkusaldo_oikea(self):
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100000)

    def test_lounaiden_maara_alussa(self):
        self.assertEqual(int(self.kassa.edulliset + self.kassa.maukkaat),0)




# ----- KÄTEISMAKSUT -----

# ----- Edulliset -----

### Riittävä käteismaksu

    def test_edullinen_jos_kateismaksu_riittava_kassa_kasvaa(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100240)

    def test_edullinen_jos_kateismaksu_riittava_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(300), 60)

    def test_edullinen_jos_kateismaksu_riittava_lounaiden_maara_kasvaa(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(int(self.kassa.edulliset), 1)

### Vajaa käteismaksu

    def test_edullinen_jos_kateismaksu_vajaa_kassa_ei_kasva(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100000)

    def test_edullinen_jos_kateismaksu_vajaa_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200), 200)

    def test_edullinen_jos_kateismaksu_vajaa_lounaiden_maara_ei_kasvaa(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(int(self.kassa.edulliset), 0)           

# ----- Maukkaat -----

### Riittävä käteismaksu    
    
    def test_maukas_jos_kateismaksu_riittava_kassa_kasvaa(self):
        self.kassa.syo_maukkaasti_kateisella(600)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100400)

    def test_maukas_jos_kateismaksu_riittava_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(600), 200)

    def test_maukas_jos_kateismaksu_riittava_lounaiden_maara_kasvaa(self):
        self.kassa.syo_maukkaasti_kateisella(600)
        self.assertEqual(int(self.kassa.maukkaat), 1)

### Vajaa käteismaksu

    def test_maukas_jos_kateismaksu_vajaa_kassa_ei_kasva(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100000)

    def test_maukas_jos_kateismaksu_vajaa_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(200), 200)

    def test_maukas_jos_kateismaksu_vajaa_lounaiden_maara_ei_kasvaa(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(int(self.kassa.maukkaat), 0)    

# ----- KORTTIMAKSUT -----