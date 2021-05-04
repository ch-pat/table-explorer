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

    table_and_search = [
        [sg.Menu(menu_layout())],
        [sg.Text(Strings.SEARCH), sg.Input(key=Keys.SEARCHINPUT, change_submits=True), sg.T("(Per ora cerca solo nella colonna nome)")],
        [sg.Column([
            [sg.Table(values=explorer.TABLE.view,
                      headings=explorer.TABLE.headings,
                      # Allows for only one item to be selected at a time and causes an event on single click
                      select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                      display_row_numbers=False,
                      auto_size_columns=True,
                      vertical_scroll_only=True,
                      justification="left",
                      alternating_row_color='light gray',
                      num_rows=min(35, len(explorer.TABLE.view)),
                      enable_events=True,
                      key=Keys.MAINTABLE)]
            ], scrollable=True, size=(800, 600), element_justification="left", expand_x=True, expand_y=True)]
    ]

    fields_and_buttons = [
        [sg.Button(Strings.OPEN_FOLDER, key=Keys.OPENFOLDER)],
        [sg.T("Spazio vuoto riservato per l'interfaccia di modifica e inserimento dati")]
    ]

    layout = [
        [sg.Column(table_and_search), sg.Column(fields_and_buttons)]
    ]
    return layout


def menu_layout() -> list:
    menu = [
        ["Configurazione",
            ["Cambia file Excel::MENUCHANGEEXCELFILE", "Cambia cartella soggetti::CHANGESUBJECTSFOLDER", "Crea cartelle soggetti::MENUCREATEFOLDERS"]]
    ]
    return menu

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
        event, values = window.read()

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
