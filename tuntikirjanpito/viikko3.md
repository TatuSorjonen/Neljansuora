# Viikko3 Neljänsuora

1. Olen tehnyt peliin voittologiikan ja minimax algoritmin aluilleen. Ei ole buustattua versiota eikä nappuloilla ole vielä kunnollista logiikkaa mihin ne
priorisoituvat laudalle.
2. Sunnuntaina ja maanantaina minulla meni voittologiikan keksimiseen noin 4h per päivä. Tiistain pidin vapaata. Keskiviikkona ja torstaina aloitin minimax
algoritmia. Tein molempina päivinä muutaman tunnin ajan. Perjantaina huomasin ongelman ja jouduin muuttamaan todella paljon koodissa, jotta sain toimimaan vihdoin
minimax algoritmin edes jollain tasolla. Minulla meni tähän koko päivä ja yö. Eli taukojen kanssa noin 10-15h. Lauantaina tein testejä ja kommentoin
koodia selkeämmäksi ja otin suurimman osan debugista pois, mutta jätin vielä pari. Yhteensä käytin siis tällä viikolla aikaa noin 25h.

## Seuraavaksi

Teen minimaxille buustauksen ja tämän jälkeen alan miettimään teoriaa, miten saisin tekoälyn mahdollisimman hyväksi.

## Testaus

1. Tein oleellisimmat yksikkötestaukset. Jätin vielä minimaxin testaamatta ja sitä kutsuvan funktion, sillä tiedän näihin tulevan vielä kohtapuoliin muutoksia
2. Koodissa on kaksi ohjelmalle turhaa tiedostoa, testi.py ja lautaa.py. Pidän näissä nopeasti backup koodia, jotta ei tarvitse jokainen kerta käydä hakemassa koodia toisesta
kansiosta missä pidän backuppia. Tämän takia coverage antaa näille kahdelle 0% testausta.

![](/kuvat/Coverage_raportti.png)
