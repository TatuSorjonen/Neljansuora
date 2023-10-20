# Testausdokumentti

Ohjelmaa testataan yksikkötesteillä unittestin avustuksella, sekä olen testannut myös manuaalisesti eri vaihtoehtoja.

Voit tehdä yksikkötestit seuraavilla komennoilla (huom: ota lainausmerkit pois eli komennot ovat lainausmerkkien sisällä muodossa 'komento':
1. Käytä komentoa 'poetry shell'
2. Tämän jälkeen aja testit komennolla 'pytest src'
3. Tämän jälkeen voit poistua poetry shellistä komennolla 'exit'

Voit halutessasi saada coverage -raportin komentosarjalla:
1. 'coverage run --branch -m pytest src'
2. Saat raportin äsken tehdystä komennolla 'coverage report -m'
3. Jos haluat html -raportin voit käyttää komentoa 'coverage html'. Löydät raportin kansiosta tiha/htmlcov/index.html

## Yksikkötestaus

1. Yksikkötestit löytyvät täältä (tee linkki, -Tatu).
2. Yksikkötestit on tehty kaikille Lauta -luokan funktioille. Minimaxille on tehty muutama eri
testi. Löytää voiton yhden ja muutaman siirron päässä alhaisella syvyydellä. Testattu myös isommalla syvyydellä. Tässä tapauksessa syvyydellä 7. Isomman syvyyden testiin on tehty välivaiheet ja toisen siirto laitetaan manuaalisesti parhaan mahdolliseen paikkaan. Olisi mennyt liian kauan aikaa yhteen testiin. Tällä hetkellä menee fuksiläppärillä yli minuutti. Minimaxille on myös tarkastettu tasapelin löytyminen ja vastustajan voiton estäminen muutaman syvyyden päästä.
3. Tiedostoja neljansuora.py ja maarittely.py ei testata, sillä nämä ovat osa käyttöliittymää, jota ei tarvinnut testata.
4. Alla coverage -raportti kokonaisuudessaan (Muista laittaa myöhemmin -Tatu). 
