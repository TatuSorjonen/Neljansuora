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

