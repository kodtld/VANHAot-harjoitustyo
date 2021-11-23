# Opintojen seuranta työkalu
Sovelluksen tarkoitus on pitää kirjaa käyttäjän:
- Viikottaisista kurssipalautuksista
- Viikkottaisista vertaisarviointien palautuksista
- Oppilaan keskiarvosta

Käyttäjä näkee pääsivulla kuluvan viikon palautuspäivät tehtävien ja vertaisarviointien osalta.
Lisäksi pääsivulla esitetään käyttäjän keskiarvo.
Pääsivulta pääsee napin lävitse joko lisäämään uuden kurssin, tai katselemaan aktiivisia kursseja (ja lisäämään saadun arvosanan menneille kursseille).

Sovellus tarjoaa yhden käyttäjäroolin, joka on normaali käyttäjä. Normaalit käyttäjät jakavat samat oikeudet keskenään. 

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/kodtld/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusm%C3%A4%C3%A4rittely.md)
- [Työaikakirjanpito](https://github.com/kodtld/ot-harjoitustyo/blob/master/dokumentaatio/ty%C3%B6aikakirjanpito.md)

## Asennus
Asenna tarvittavat riippuvuudet komennolla: 
```bash
poetry install
```
## Suoritus
Sovelluksen voi suorittaa komentoriviltä komennolla:
```bash
poetry run invoke start
```
Tai mikäli invoke tuottaa ongelmia, voi ohjelman käynnistää "manuaalisesti" komennolla:
```bash
python3 src/Login_Screen.py
```

## Testaus
Testit voi ajaa komennolla:
```bash
poetry run invoke test
```
Tällä hetkellä suotuisia testejä ei vielä löydy, mutta testejä lisätään paraa'aikaa.

Testikattavuusraportin voi puolestaan generoida komennolla:
```bash
poetry run invoke coverage-report
```

