# Neljänsuora

Neljänsuora on peli, jossa pelataan 6x7 laudalla eli 6 riviä ja 7 saraketta, ja yritetään saada neljänsuora ihan mihin suuntaan katsottuna tahansa. Neljänsuora on hyvin saman kaltainen peli kuin mitä ristinolla on, mutta tässä pystymme ainoastaan laittamaan nappulan alimmalle vapaalle riville sarakkeessa. Työssäni on 4 eri pelimuotoa. Yksinpeli, helppo yksinpeli, kaksinpeli sekä demo. Yksinpelissä pelaat tekoälyä vastaan, joka on alpha-beta pruningin avulla buustattu minimax-algoritmi. Tässä tekoäly pelaa lähes täydellisesti ja sitä on vaikea voittaa edes täydellisellä pelaamisella. Helpossa yksinpelissä pelaat todella helppoa tekoälyä vastaan, joka laittaa ainaostaan satunnaisesti nappuloita laudalle. Kaksinpelissä voit pelata kahdella eri pelaajalla. Demossa minimax tekoäly pelaa itseään vastaan.

## Komennot

1. Lataa sovellus itsellesi, joko kloonaamalla komennolla git clone 'työn linkki' tai lataamalla [täältä](https://github.com/TatuSorjonen/Tiha/releases/tag/Loppupalautus)

2. Mene hakemistoon Tiha

3. Lataa poetry: 'poetry install'

4. Pelin aloittaminen: 'python3 src/indeksi.py'.
Huom. toimii myös komennolla 'poetry run python3 src/indeksi.py', mutta tämä ei ole suositeltavaa. Toimii huonommin.

5. Testien suorittaminen: 'poetry run pytest src'

6. Coverage raportin testeistä saadaan komennoilla.
   1. coverage run --branch -m pytest src
   2. coverage report -m
   3. coverage html

## Dokumentaatio

[Määrittelydokumentti](https://github.com/TatuSorjonen/Tiha/blob/master/Dokumentaatio/maarittelydokumentti.md)

[Tuntikirjanpito/loppupalautus](https://github.com/TatuSorjonen/Tiha/blob/master/Dokumentaatio/tuntikirjanpito/loppupalautus.md)

[Käyttöohje](https://github.com/TatuSorjonen/Tiha/blob/master/Dokumentaatio/kayttoohje.md)

[Testausdokumentti](https://github.com/TatuSorjonen/Tiha/blob/master/Dokumentaatio/testausdokumentti.md)

[Toteustusdokumentti](https://github.com/TatuSorjonen/Tiha/blob/master/Dokumentaatio/toteutusdokumentti.md)
