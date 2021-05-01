"""
Layouts for the GUI are defined in this module
"""
import PySimpleGUI as sg
import os
from application.strings import Keys
from application.strings import Strings
from application import explorer


# ---- LAYOUTS ---- #

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

# ---- WINDOWS ---- #


"""
Windows are supposed to be 'smaller' than layouts and be self-contained. 
They usually directly return values necessary to other functions, while layouts are meant to be re-usable.
"""


def edit_settings_window() -> (str, str):
    excel_filetypes = (("File Excel", "*.xlsx"), ("File Excel old", "*.xls"), ("File CSV", "*.csv"))
    layout = [
        [sg.Input(key="a", readonly=True), sg.FolderBrowse(Strings.CHOOSE_FOLDER_SUBJECTS, key=Keys.SUBJECTSFOLDER)],
        [sg.Input(key="b", readonly=True), sg.FileBrowse(Strings.CHOOSE_EXCEL_FILE, file_types=excel_filetypes, key=Keys.EXCELFILE)],
        [sg.Button(Strings.CONFIRM, key=Keys.CONFIRM)],
        [sg.Text(Strings.FILL_CONFIG, visible=False, key=Keys.FILLCONFIGTEXT)]
    ]

    window = sg.Window(Strings.CONFIGURATION, layout=layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            quit()  # User doesn't want to use the software

        if event == Keys.CONFIRM:
            excel_file = values[Keys.EXCELFILE]
            subj_folder = values[Keys.SUBJECTSFOLDER]
            if not (excel_file and subj_folder):
                window[Keys.FILLCONFIGTEXT].update(visible=True)
            else:
                if os.path.isdir(subj_folder) and os.path.isfile(excel_file):
                    return subj_folder, excel_file
                else:
                    sg.popup(Strings.CONFIG_NOT_EXISTS)
