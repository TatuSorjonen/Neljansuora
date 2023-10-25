# Neljänsuora

## Komennot

1. Lataa sovellus itsellesi, joko kloonaamalla komennolla git clone 'työn linkki' tai lataamalla tästä (tee linkki -Tatu)

1. Mene hakemistoon Tiha

2. Lataa poetry: 'poetry install'

3. Pelin aloittaminen: 'python3 src/indeksi.py'.
Huom. toimii myös komennolla 'poetry run python3 src/indeksi.py', mutta tämä ei ole suositeltavaa. Toimii huonommin.

5. Testien suorittaminen: 'poetry run pytest src'

6. Coverage raportin testeistä saadaan komennoilla.
   1. coverage run --branch -m pytest src.
   2. coverage report -m
   3. coverage html

## Dokumentaatio

[Määrittelydokumentti](https://github.com/TatuSorjonen/Tiha/blob/master/maarittelydokumentti.md)

[Tuntikirjanpito/viikko6](https://github.com/TatuSorjonen/Tiha/blob/master/Dokumentaatio/tuntikirjanpito/viikko6.md)

[Käyttöohje](https://github.com/TatuSorjonen/Tiha/blob/master/Dokumentaatio/kayttoohje.md)

[Testausdokumentti](https://github.com/TatuSorjonen/Tiha/blob/master/Dokumentaatio/testausdokumentti.md)

[Toteustusdokumentti](https://github.com/TatuSorjonen/Tiha/blob/master/Dokumentaatio/toteutusdokumentti.md)
