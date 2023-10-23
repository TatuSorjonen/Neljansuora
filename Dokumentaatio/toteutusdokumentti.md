# Toteutusdokumentti

## Käyttöliittymä

Sovelluksen käyttöliittymä on jaettu kahteen eri pääluokkaan. Aloitusikkunnaan joka löytyy samasta
tiedostosta kuin Maarittely luokka eli maarittely.py ja Neljansuora luokkaan, joka löytyy tiedostosta
neljansuora.py

- Pelin aloitusruutu (Aloitusikkuna)
- Neljänsuora peli (Neljansuora)

Peli alkaa kutsumalla Neljansuora luokan lue_maaritykset funktiota. Funktio avaa aloitusikkunan
Aloitusikkuna luokan avustuksella, jossa pelaaja voi valita pelimuodon, sekä kumpi pelaaja aloittaa
riippuen valitusta pelimuodosta. Peli alkaa painamalla aloita peli nappulaa ja alustetaan peli
annetujen arvojen mukaan. Pelissä pelaaja voi omalla vuorollaan, joko pelata nappulan tai painaa
ylhäällä olevista 'aloita alusta' tai 'sulje' nappuloista. Jos painetaan etukäteen, niin pelaajan siirto
tai nappulan painallus tehdään heti tekoälyn lopetettua vuoronsa. 'Aloita alusta' nappi alustaa pelin
ja avaa aloitusikkunan uudelleen. 'Sulje' nappi sulkee ohjelman.

## Diagrammi pelin alustamisesta ja aloittamisesta

Peli aloitetaan indeksi.py tiedostosta ja käynnistetään funktiolla lue_maaritykset().
Aloitusikkuna luodaan Aloitusikkuna luokan funktiota käyttäen lue_pelitapa(). Tämä luo aloitusikkunan, jossa käyttäjä voi valita pelimuodon sekä aloittajan, pelimuodosta riippuen ja palauttaa nämä. Neljansuora luokassa alustetaan peli uudestaan käyttäen kyseistä pelimuotoa ja mahdollista aloittajaa. Tämän jälkeen aloitetaan peli käyttäen funktiota aloita_peli().

```mermaid
sequenceDiagram
  participant indeksi.py
  participant Neljansuora
  participant Aloitusikkuna
  indeksi.py->> Neljansuora: lue_maaritykset()
  Neljansuora->> Aloitusikkuna: lue_pelitapa()
  Aloitusikkuna->> Neljansuora: pelimuoto ja aloittaja
  Neljansuora->> Neljansuora: alusta_peli(pelimuoto, aloittaja)
  Neljansuora->> Neljansuora: aloita_peli()
```

## Diagrammi pelin kulusta

```mermaid
sequenceDiagram
  actor Pelaaja 1
  actor Pelaaja 2
  participant Neljansuora
  participant Lauta
  Neljansuora->> Neljansuora: aloita_peli()
  Neljansuora->> Neljansuora: piirra_ikkuna()
  Neljansuora->> Neljansuora: tarkista_tekoaly()
  Pelaaja 1->> TicTacToe: tarkista_hiiren_painallus(hiiri_x, hiiri_y)
  Neljansuora->> Neljansuora: Tarkistaa onko lautaa tai nappia painettu
  Neljansuora->> Neljansuora: Jos on painettu nappia 'Aloita alusta', niin alustetaan peli uudelleen funktiolla lue_maaritykset()
  Neljansuora->> Neljansuora: Jos on painettu 'Sulje' nappia, niin sulkee pelin
  Neljansuora->> Neljansuora: Jos on painettu laudalle, niin käytetään funktiota aseta_merkki
```
