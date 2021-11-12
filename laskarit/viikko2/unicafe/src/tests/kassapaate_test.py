import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

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

# ----- Edulliset -----

### Riittävä korttimaksu

    def test_edullinen_jos_korttimaksu_riittava_korttia_veloitetaan(self):
        self.kortti = Maksukortti(400)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(int(self.kortti.saldo), 160)

    def test_edullinen_jos_korttimaksu_riittava_true(self):
        self.kortti = Maksukortti(400)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti),True)

    def test_edullinen_jos_korttimaksu_riittava_lounaiden_maara_kasvaa(self):
        self.kortti = Maksukortti(400)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(int(self.kassa.edulliset), 1)

    def test_edullinen_jos_korttimaksu_riittava_kassa_ei_kasva(self):
        self.kortti = Maksukortti(400)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100000)
    

### Vajaa korttimaksu

    def test_edullinen_jos_korttimaksu_vajaa_korttia_ei_veloiteta(self):
        self.kortti = Maksukortti(140)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(int(self.kortti.saldo), 140)

    def test_edullinen_jos_korttimaksu_vajaa_false(self):
        self.kortti = Maksukortti(140)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti),False)

    def test_edullinen_jos_korttimaksu_vajaa_lounaiden_maara_ei_kasva(self):
        self.kortti = Maksukortti(140)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(int(self.kassa.edulliset), 0)

    def test_edullinen_jos_korttimaksu_vajaa_kassa_ei_kasva(self):
        self.kortti = Maksukortti(140)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100000)


# ----- Maukkaat -----

### Riittävä korttimaksu

    def test_maukas_jos_korttimaksu_riittava_korttia_veloitetaan(self):
        self.kortti = Maksukortti(600)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(int(self.kortti.saldo), 200)

    def test_maukas_jos_korttimaksu_riittava_true(self):
        self.kortti = Maksukortti(600)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti),True)

    def test_maukas_jos_korttimaksu_riittava_lounaiden_maara_kasvaa(self):
        self.kortti = Maksukortti(600)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(int(self.kassa.maukkaat), 1)

    def test_maukas_jos_korttimaksu_riittava_kassa_ei_kasva(self):
        self.kortti = Maksukortti(600)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100000)

### Vajaa korttimaksu

    def test_maukas_jos_korttimaksu_vajaa_korttia_ei_veloiteta(self):
        self.kortti = Maksukortti(140)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(int(self.kortti.saldo), 140)

    def test_maukas_jos_korttimaksu_vajaa_false(self):
        self.kortti = Maksukortti(140)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti),False)

    def test_maukas_jos_korttimaksu_vajaa_lounaiden_maara_ei_kasva(self):
        self.kortti = Maksukortti(140)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(int(self.kassa.maukkaat), 0)

    def test_maukas_jos_korttimaksu_vajaa_kassa_ei_kasva(self):
        self.kortti = Maksukortti(140)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100000)

# ----- SALDON LATAAMINEN KORTILLE -----

### Positiivinen saldolataus

    def test_positiivinen_saldolataus_saldo_kasvaa(self):
        self.kortti = Maksukortti(100)
        self.kassa.lataa_rahaa_kortille(self.kortti,300)
        self.assertEqual(int(self.kortti.saldo), 400)

    def test_positiivinen_saldolataus_kassa_kasvaa(self):
        self.kortti = Maksukortti(100)
        self.kassa.lataa_rahaa_kortille(self.kortti,300)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100300)

### Negatiivinen saldolataus

    def test_negatiivinen_saldolataus_saldo_ei_kasva(self):
        self.kortti = Maksukortti(100)
        self.kassa.lataa_rahaa_kortille(self.kortti,-300)
        self.assertEqual(int(self.kortti.saldo), 100)

    def test_negatiivinen_saldolataus_kassa_ei_kasva(self):
        self.kortti = Maksukortti(100)
        self.kassa.lataa_rahaa_kortille(self.kortti,-300)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100000)