from googlesearch import search
import openpyxl

slowa = 'autokar', 'autokary', 'bus', 'busy', 'transport autokarem', 'przewoznicy autokarowi', 'przewoznik autokarowy', 'przewoźnik autokarowy', 'przewoźnicy autokarowi',\
        'przewóz krajowy autokarem', 'przewóz zagraniczny autokarem', 'tabor autokarów', 'flota autokarów', 'przewóz krajowy autokary', 'przewóz zagraniczny autokary'
# wojewodztwo = 'zachodniopomorskie', 'pomorskie', 'lubuskie', 'wielkopolskie', 'kujawsko-pomorskie', 'warmińsko-mazurskie', 'podlaskie', 'mazowieckie', 'łódzkie',\
#               'dolnośląskie', 'opolskie', 'śląskie', 'świętokrzyskie', 'lubelskie', 'podkarpackie', 'małopolskie'

wojewodztwo = "gdańsk", "pomorskie"

wyszukiwarka = []

for i in slowa:
    for y in wojewodztwo:
        wyszukiwarka.append(y + ' ' + i)

autokary = []

for pyt in wyszukiwarka:
    for url in search(pyt, tld='pl', lang='pl', stop=50):
        autokary.append(url)

autokar = openpyxl.Workbook()
zakladka = autokar.active

for link in autokary:
    zakladka.append([link])

autokar.save(r'\\serwer\\pub\\DZIAŁ ORGANIZACJI\\Słoma\\Sezony\\LATO 2020\\baza_autokary_pomorskie.xlsx')
