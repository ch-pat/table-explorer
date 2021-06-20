import random
import pandas

"""
Running this script will generate a 3000 rows excel file for testing purposes
"""


headers = [
    "Nome",
    "Cognome",
    "Codice Fiscale",
    "Indirizzo",
    "CAP",
    "Comune",
    "Provincia",
    "Telefono 1",
    "Telefono 2",
    "E-mail 1",
    "E-mail 2",
    "Persone Collegate",
    "Rapporto",
    "Servizio CAF",
    "Servizio Patronato",
    "Prodotto Finanziario",
    "Note",
    "Dettagli Aggiuntivi",
    "Data Tesseramento",
    "Tipo Tessera",
    "Numero Ricevuta",
    "Contributo Volontario",
    "Uscita"
    ]
df = pandas.DataFrame()
for h in headers:
    col = [h + str(n) for n in range(1000)]
    random.shuffle(col)
    df[h] = col

df.to_excel("D:\\test-data.xlsx", index=False)
