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

## Diagrammi pelin kulusta, kun on yksinpeli ja pelaajan aloitus

Peli alkaa, kun pelaaja on painanut aloitusikkunasta nappia, 'Aloita peli'.
Aluksi piirretään pelilauta, jonka jälkeen tarkastetaan onko aloittajana tekoäly tai onko pelimuotona demo. Tässä tapuksessa ei ole ja heti painalluksesta tarkastetaan mihin kohtaan pelilautaa on painettu funktiota tarkista_hiiren_painallus käyttäen. Jos pelilautaa on painettu, niin pelaa pelaajan vuoron, jos siirto on mahdollinen. Tämän jälkeen tarkistaa heti tilanteen ja jos ei ole löytynyt voittajaa, niin alkaa pelaamaan tekoälyn siirtoa käyttämällä funktiota lisaa_paras_siirto. Tämä jatkuu kunnes jompikumpi voittaa tai tulee tasapeli.

```mermaid
sequenceDiagram
  actor Pelaaja 1
  actor Pelaaja 2
  participant Neljansuora
  participant Lauta
  Neljansuora->> Neljansuora: aloita_peli()
  Neljansuora->> Neljansuora: piirra_ikkuna()
  Neljansuora->> Neljansuora: tarkista_tekoaly()
  loop
  Pelaaja 1->> Neljansuora: tarkista_hiiren_painallus(hiiri_x, hiiri_y)
  Neljansuora->> Neljansuora: Tarkistaa onko lautaa tai nappia painettu
  Neljansuora->> Neljansuora: Jos on painettu laudalle, niin käytetään funktiota aseta_merkki
  Neljansuora->> Neljansuora: pelaa_pelaaja()
  Neljansuora->> Lauta: lisaa_nappula(sarake, lauta.ruudukko)
  Neljansuora->> Lauta: tarkista_tilanne()
  Neljansuora->> Neljansuora: pelaa_tekoaly()
  Neljansuora->> Lauta: lisaa_paras_siirto(syvyys)
  end
```

## Diagrammi funktiosta lisaa_paras_siirto ja minimaxista sekä tämän heuristiikasta

```mermaid
sequenceDiagram
  participant Neljansuora
  participant Lauta
  participant Lauta luokan minimax
  participant Lauta luokan arvioi_asema
  Neljansuora->> Lauta: lisaa_paras_siirto(syvyys)
  loop
  Lauta->> Lauta: Käydään läpi kaikki mahdolliset siirrot
  Lauta->> Lauta: kopioi laudan
  Lauta->> Lauta: vapaa_rivi_sarakkeessa(sarake, kopioitu lauta) palauttaa rivin
  Lauta->> Lauta: jos rivi ei ole -1 (eli on vapaa) lisaa_nappula(sarake, kopioitu lauta)
  Lauta->> Lauta: minimax(syvyys, toisen vuoro, kopioitu lauta, miinus ääretön, plus ääretön)
  Lauta->> Lauta luokan minimax: tarkista_tilanne(kopioitu lauta)
  Lauta luokan minimax->> Lauta luokan minimax: Jos jompikumpi voittaa, palauttaa tuloksen riippuen voittajasta
  Lauta luokan minimax->> Lauta luokan minimax: Jos ei löytynyt voittajaa ja syvyys ei ole 0, kulkeutuu if-else haarassa parhaaseen mahdolliseen itsellä tai parhaaseen mahdolliseen vastustajalla riippuen vuorosta ja lisää tämän uudelle laudan kopiolle
  Lauta luokan minimax->> Lauta luokan minimax: minimax(syvyys-1, toisen vuoro, kopioitu lauta, miinus ääretön, plus ääretön)
  Lauta luokan minimax->> Lauta luokan minimax: Jos syvyys on 0 ja ei löytynyt voittajaa, tarkistaa onko tullut tasapeli ja jos ei ole niin arvioi parhaan mahdollisen aseman arvioi_asema(kopioitu lauta)
  Lauta luokan minimax->> Lauta luokan arvioi_asema: Jos syvyys on 0 ja ei löydy voittajaa arvioi parhaan aseman. arvioi_asema(kopioitu taulukko)
  Lauta luokan arvioi_asema->> Lauta luokan arvioi_asema: pisteyta_voittomahdollisuudet(kopioitu lauta, rivi, sarake, pisteet)
  Lauta luokan arvioi_asema->> Lauta luokan arvioi_asema: pisteyta_nappula_sijainti(rivi, sarake)
  Lauta luokan arvioi_asema->> Lauta: Jos vuoro on keltaisen ja syvyys ei ole jaollinen kahdella tai vuoro on punaisen ja syvyys on jaollinen kahdella pisteet_keltainen - pisteet_punainen. Muulloin pisteet_punainen - pisteet_keltainen
  Lauta->> Lauta: Tarkastaa siirron pisteet ja jos on paras siirto niin pistää muistiin
  end
  Lauta->> Neljansuora: Palauttaa parhaan siirron kaikkien mahdollisten siirtojen jälkeen
```
