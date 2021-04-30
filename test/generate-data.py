import random
import pandas

"""
Running this script will generate a 3000 rows excel file for testing purposes
"""


headers = [
    "nome",
    "cognome",
    "Codice Fiscale",
    "indirizzo",
    "cap",
    "comune",
    "prov",
    "telefono 1",
    "telefono 2",
    "mail 1",
    "mail 2",
    "persone collegate",
    "rapporto",
    "servizio CAF",
    "servizio Patronato",
    "prodotto Finanziario",
    "Note"
    ]
df = pandas.DataFrame()
for h in headers:
    col = [h + str(n) for n in range(3000)]
    random.shuffle(col)
    df[h] = col

df.to_excel("D:\\test-data.xlsx", index=False)
