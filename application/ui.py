"""
Layouts for the GUI are defined in this module
"""
import PySimpleGUI as sg
import os
from codicefiscale import codicefiscale
from application.strings import Keys
from application.strings import Strings
from application import explorer

# ---- LAYOUTS ---- #


def main_layout() -> list:
    w, h = width, height
    table_and_search = [
        [sg.Menu(menu_layout())],
        [
            sg.Button(Strings.RELOAD, key=Keys.RELOAD),
            sg.Text("🔍"),
            # Search input boxes
            sg.Text("Nome:"), sg.Input(key=Keys.SEARCHINPUTNOME, change_submits=True, size=(10, 1)),
            sg.Text("Cognome:"), sg.Input(key=Keys.SEARCHINPUTCOGNOME, change_submits=True, size=(10, 1)),
            sg.Text("CF:"), sg.Input(key=Keys.SEARCHINPUTCF, change_submits=True, size=(10, 1)),
         ],
        [sg.Column([
            [sg.Table(values=explorer.TABLE.view,
                      headings=explorer.TABLE.view_headings,
                      # Allows for only one item to be selected at a time and causes an event on single click
                      select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                      display_row_numbers=False,
                      auto_size_columns=True,
                      vertical_scroll_only=True,
                      justification="left",
                      alternating_row_color='light gray',
                      num_rows=35,
                      enable_events=True,
                      key=Keys.MAINTABLE)]
            ], size=(w*4/9, h*7/9), element_justification="left", expand_x=True, expand_y=True)],
        [sg.Button(Strings.ADD_NEW, key=Keys.ADD)]
    ]

    fields_and_buttons = [
        [sg.Text("Modifica riga selezionata", justification='left'),
         sg.Button(Strings.DELETE_ROW, button_color='red', key=Keys.DELETE),
         sg.Button(Strings.SAVE_CHANGES, key=Keys.SAVE),
         sg.Text("Sono presenti modifiche non salvate!", visible=False)
         ],
        [sg.Column(edit_fields(), scrollable=True, vertical_scroll_only=True, expand_y=True)],
    ]

    layout = [
        [sg.Column(table_and_search), sg.Column(fields_and_buttons, expand_x=True, expand_y=True)]
    ]
    return layout


def menu_layout() -> list:
    menu = [
        ["Configurazione",
            ["Cambia file Excel::MENUCHANGEEXCELFILE", "Cambia cartella soggetti::CHANGESUBJECTSFOLDER", "Crea cartelle soggetti::MENUCREATEFOLDERS"]]
    ]
    return menu


def labelled_input(label: str, key: str = None, size: tuple = (20, 1)) -> sg.Column:
    if not key:
        key = label
    col = sg.Column([
        [sg.Text(label, justification="left")],
        [sg.Input(key=key, size=size)]
    ], scrollable=False, element_justification='left', justification='left')
    return col


def edit_fields() -> list:
    """ Returns the layout containing all fields for table row editing """
    # "nome", "cognome", "Codice Fiscale",
    # "indirizzo", "cap", "comune", "prov",
    # "telefono 1", "telefono 2",
    # "mail 1", "mail 2",
    # "persone collegate", "rapporto", "VAI"
    # "servizio CAF", "servizio Patronato",
    # "prodotto Finanziario",
    # "Note",
    # "Dettagli Aggiuntivi",
    # "Data Tesseramento",
    # "Tipo Tessera",
    # "Numero Ricevuta",
    # "Contributo Volontario",
    # "Uscita"

    layout = [
        [sg.Frame('Dati Anagrafici', [
            [labelled_input('Nome', key=Keys.EDITNOME), labelled_input('Cognome', key=Keys.EDITCOGNOME),
             labelled_input('Codice Fiscale', size=(18, 1), key=Keys.EDITCODICEFISCALE)],
            [labelled_input('Indirizzo', size=(20, 1), key=Keys.EDITINDIRIZZO),
             labelled_input('CAP', size=(7, 1), key=Keys.EDITCAP), labelled_input('Comune', key=Keys.EDITCOMUNE),
             labelled_input('Provincia', size=(10, 1), key=Keys.EDITPROV)]
        ]), sg.Button(Strings.OPEN_FOLDER, key=Keys.OPENFOLDER)],

        [sg.Frame('Contatti', [
            [labelled_input('Telefono 1', key=Keys.EDITTELEFONO1), labelled_input('Telefono 2', key=Keys.EDITTELEFONO2),
             labelled_input('E-mail 1', size=(20, 1), key=Keys.EDITMAIL1),
             labelled_input('E-mail 2', size=(20, 1), key=Keys.EDITMAIL2)]
        ])],

        [sg.Frame('Persone Collegate', [
            [labelled_input('Persone Collegate', key=Keys.EDITCOLLEGATE),
             labelled_input('Rapporto', key=Keys.EDITRAPPORTO), sg.Button("Vai a soggetto", key=Keys.EDITVAI)]
        ])],

        [sg.Frame('Servizi & Prodotti', [
            [labelled_input('Servizio CAF', key=Keys.EDITCAF),
             labelled_input('Servizio Patronato', key=Keys.EDITPATRONATO),
             labelled_input('Prodotto Finanziario', key=Keys.EDITFINANZIARIO)]
        ])],

        [sg.Frame('Dati Tesseramento', [
            [labelled_input('Data Tesseramento', key=Keys.EDITDATATESSERA),
             labelled_input('Tipo Tessera', key=Keys.EDITTIPOTESSERA),
             labelled_input('Numero Ricevuta', key=Keys.EDITRICEVUTA)],
            [labelled_input('Contributo Volontario', key=Keys.EDITCONTRIBUTO),
             labelled_input('Uscita', key=Keys.EDITUSCITA)]
        ])],

        [sg.Column([
            [sg.Text("Note", justification="left")],
            [sg.Multiline(size=(40, 3), key=Keys.EDITNOTE)]
        ], scrollable=False, element_justification='left', justification='left'),
            sg.Column([
                [sg.Text("Dettagli Aggiuntivi", justification="left")],
                [sg.Multiline(size=(40, 3), key=Keys.EDITDETTAGLI)]
            ], scrollable=False, element_justification='left', justification='left')
        ]
    ]
    return layout


# ---- WINDOWS ---- #


"""
Windows are supposed to be 'smaller' than layouts and be self-contained. 
They usually directly return values necessary to other functions, while layouts are meant to be re-usable.
"""
excel_filetypes = (("File Excel", "*.xlsx"), ("File Excel old", "*.xls"), ("File CSV", "*.csv"))


def edit_settings_window() -> (str, str):
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
                    window.close()
                    del window
                    return subj_folder, excel_file
                else:
                    sg.popup(Strings.CONFIG_NOT_EXISTS)


def yes_no_window(text: str) -> bool:
    """
    Provides a window with the text specified and a 'cancel or confirm' prompt
    Returns True if confirm, False otherwise
    """
    layout = [
        [sg.Text(text)],
        [sg.Button(Strings.CANCEL), sg.Button(Strings.CONFIRM)]
    ]

    window = sg.Window(text, layout=layout, modal=True)

    while True:
        event, _ = window.read()

        if event in (sg.WINDOW_CLOSED, Strings.CANCEL):
            answer = False
            break

        if event == Strings.CONFIRM:
            answer = True
            break

    window.close()
    del window
    return answer


def edit_subjects_folder_window():
    """
    Asks for a new location for the subjects directory
    Return the specified directory or None
    """

    layout = [
        [sg.Text(f"La cartella attualmente in uso come cartella Soggetti (ovvero la cartella contenente le cartelle "
                 f"codici fiscali) è: {sg.user_settings()['subjects_folder']}\n\n"
                 f"Se si desidera modificare la cartella Soggetti, selezionarla e confermare, altrimenti annullare.")],
        [sg.Input(readonly=True), sg.FolderBrowse(Strings.CHOOSE_FOLDER_SUBJECTS, key=Keys.SUBJECTSFOLDER)],
        [sg.Text(Strings.FILL_TEXT, visible=False, key=Keys.FILLCONFIGTEXT)],
        [sg.Button(Strings.CANCEL), sg.Button(Strings.CONFIRM)]
    ]

    window = sg.Window("Modifica Cartella Soggetti", layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, Strings.CANCEL):
            break

        if event == Strings.CONFIRM:
            subj_folder = values[Keys.SUBJECTSFOLDER]
            if not subj_folder:
                window[Keys.FILLCONFIGTEXT].update(visible=True)
            else:
                if os.path.isdir(subj_folder):
                    window.close()
                    del window
                    return subj_folder
                else:
                    sg.popup(Strings.CONFIG_NOT_EXISTS)

    window.close()
    del window


def edit_excel_file_window():
    """
    Asks for a new location excel file
    Return the specified file or None
    """

    layout = [
        [sg.Text(f"Il file Excel in uso come database è: {sg.user_settings()['excel_file']}\n\n"
                 f"Se si desidera modificare il file Excel di riferimento selezionarlo e confermare, "
                 f"altrimenti annullare.")],
        [sg.Input(readonly=True), sg.FileBrowse(Strings.CHOOSE_EXCEL_FILE, file_types=excel_filetypes,
                                                key=Keys.EXCELFILE)],
        [sg.Text(Strings.FILL_TEXT, visible=False, key=Keys.FILLCONFIGTEXT)],
        [sg.Button(Strings.CANCEL), sg.Button(Strings.CONFIRM)]
    ]

    window = sg.Window("Modifica file Excel", layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, Strings.CANCEL):
            break

        if event == Strings.CONFIRM:
            excel_file = values[Keys.EXCELFILE]
            if not excel_file:
                window[Keys.FILLCONFIGTEXT].update(visible=True)
            else:
                if os.path.isfile(excel_file):
                    window.close()
                    del window
                    return excel_file
                else:
                    sg.popup(Strings.CONFIG_NOT_EXISTS)

    window.close()
    del window


def add_new_row_window() -> dict:
    """
    Provides a window with forms to fill to add a new row to the database
    :return: A dict containing {dataframe_column: content}
    """
    layout = [
        [sg.Frame('Dati Anagrafici', [
            [labelled_input('Nome', key=Keys.ADDNOME), labelled_input('Cognome', key=Keys.ADDCOGNOME),
             labelled_input('Codice Fiscale', size=(18, 1), key=Keys.ADDCODICEFISCALE)],
            [labelled_input('Indirizzo', size=(20, 1), key=Keys.ADDINDIRIZZO),
             labelled_input('CAP', size=(7, 1), key=Keys.ADDCAP), labelled_input('Comune', key=Keys.ADDCOMUNE),
             labelled_input('Provincia', size=(10, 1), key=Keys.ADDPROV)]
        ])],

        [sg.Frame('Contatti', [
            [labelled_input('Telefono 1', key=Keys.ADDTELEFONO1), labelled_input('Telefono 2', key=Keys.ADDTELEFONO2),
             labelled_input('E-mail 1', size=(20, 1), key=Keys.ADDMAIL1),
             labelled_input('E-mail 2', size=(20, 1), key=Keys.ADDMAIL2)]
        ])],

        [sg.Frame('Persone Collegate', [
            [labelled_input('Persone Collegate', key=Keys.ADDCOLLEGATE),
             labelled_input('Rapporto', key=Keys.ADDRAPPORTO)]
        ])],

        [sg.Frame('Servizi & Prodotti', [
            [labelled_input('Servizio CAF', key=Keys.ADDCAF),
             labelled_input('Servizio Patronato', key=Keys.ADDPATRONATO),
             labelled_input('Prodotto Finanziario', key=Keys.ADDFINANZIARIO)]
        ])],

        [sg.Frame('Dati Tesseramento', [
            [labelled_input('Data Tesseramento', key=Keys.ADDDATATESSERA),
             labelled_input('Tipo Tessera', key=Keys.ADDTIPOTESSERA),
             labelled_input('Numero Ricevuta', key=Keys.ADDRICEVUTA)],
            [labelled_input('Contributo Volontario', key=Keys.ADDCONTRIBUTO),
             labelled_input('Uscita', key=Keys.ADDUSCITA)]
        ])],

        [sg.Column([
            [sg.Text("Note", justification="left")],
            [sg.Multiline(size=(40, 3), key=Keys.ADDNOTE)]
        ], scrollable=False, element_justification='left', justification='left'),
            sg.Column([
                [sg.Text("Dettagli Aggiuntivi", justification="left")],
                [sg.Multiline(size=(40, 3), key=Keys.ADDDETTAGLI)]
            ], scrollable=False, element_justification='left', justification='left')
        ],

        [sg.Button("Conferma inserimento nuovo soggetto", key=Keys.ADDSAVE)]
    ]

    window = sg.Window('Aggiungi nuovo soggetto', layout, location=(0, 0))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            window.close()
            del window
            break

        if event == Keys.ADDSAVE:
            form_contents = {}
            for k in Keys.ADD_FORM_TO_COLUMN.keys():
                form_contents[Keys.ADD_FORM_TO_COLUMN[k]] = window[k].get()

            new_cf = form_contents[Keys.COLCF]
            if codicefiscale.is_valid(new_cf):
                if not explorer.TABLE.codice_fiscale_already_exists(new_cf):
                    window.close()
                    del window
                    return form_contents
                else:
                    sg.popup_error("Codice fiscale inserito già presente nel database!")
            else:
                sg.popup_error("Codice fiscale inserito non valido!")


# Global ui utilities
def get_screen_dimensions() -> (int, int):
    temp_window = sg.Window("tmp", [[]], alpha_channel=0, finalize=True)
    w, h = temp_window.get_screen_dimensions()
    temp_window.close()
    del temp_window
    return w, h


width, height = get_screen_dimensions()
