import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")


    def test_konstruktori_asettaa_saldon_oikein(self):
        kortti = Maksukortti(10)

        vastaus = str(kortti)

        self.assertEqual(vastaus, "Kortilla on rahaa 10 euroa")


    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(10)

        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 7.5 euroa")
