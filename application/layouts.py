"""
Layouts for the GUI are defined in this module
"""
import PySimpleGUI as sg
import pandas as pd
from application.strings import Keys
from application.strings import Strings
from application import explorer


def main_layout() -> list:
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
    ]  # TODO: either keep hard-coded (for the specific person) or grab from the above file

    layout = [
        [sg.Input(key=Keys.SEARCHINPUT), sg.Button(Strings.SEARCH, key=Keys.SEARCH)],
        [sg.Table(values=explorer.TABLE.view,
                  headings=headers,
                  display_row_numbers=False,
                  auto_size_columns=False,
                  num_rows=min(25, len(explorer.TABLE.view)),
                  enable_events=True,
                  key="-A-")]
    ]
    return layout
