import PySimpleGUI as sg
from application import ui
from application.strings import Strings
from application import explorer
import os


def load_settings():
    """
    Settings are a key: value dictionary
    The following are the currently used keys and the meaning for their values

    "subjects_folder":  the folder containing all the 'codice fiscale' folders
    "excel_file":       the excel file used as database
    """
    # Used to load the settings file and for first configuration
    settings = sg.UserSettings()
    if not settings.exists():
        # If this is the first time running the program
        subj_folder, excel_file = ui.edit_settings_window()
        settings["subjects_folder"] = subj_folder
        settings["excel_file"] = excel_file
        settings.save()
    else:
        # Settings exist, check if they contain acceptable values
        subj_folder = settings["subjects_folder"]
        excel_file = settings["excel_file"]
        if not(os.path.isdir(subj_folder) and os.path.isfile(excel_file)):
            sg.popup(Strings.CONFIG_ERROR)
            subj_folder, excel_file = ui.edit_settings_window()
            settings["subjects_folder"] = subj_folder
            settings["excel_file"] = excel_file
            settings.save()


def first_run():
    """
    Only runs on first run
    Asks user to generate the codice fiscale folders
    other important configuration could be added later on
    """
    if "first_run" not in sg.user_settings().keys():
        menu_create_folders()
        print(sg.user_settings())
        sg.user_settings_set_entry("first_run", False)
        sg.user_settings_save()


def open_subject_folder(row_index, row_content):
    # IMPORTANT indexes refer to the current view, NOT THE ACTUAL DATA
    # shouldn't matter here because no change is made to the data, but keep in mind
    cf = explorer.TABLE.extract_codice_fiscale_from_row(row_content)
    subj_folder = sg.user_settings()["subjects_folder"]
    full_path = os.path.join(subj_folder, cf)
    if open_dir(full_path):
        return
    else:
        text = f"Non è stata trovata la cartella {cf} sotto la cartella Soggetti.\n" \
               f"Si desidera crearla in questo momento?"
        if ui.yes_no_window(text):
            try:
                os.mkdir(full_path)
                open_dir(full_path)
            except Exception:  # TODO: narrow the error down if encountered
                sg.popup_error(Strings.WRITE_ERROR)


def menu_create_folders():
    if ui.yes_no_window(Strings.MENU_CREATE_FOLDERS):
        cf_list = explorer.TABLE.get_codice_fiscale_list()
        subj_folder = sg.user_settings()["subjects_folder"]
        count = 0
        if not os.path.isdir(subj_folder):
            sg.popup_error(f"Il percorso selezionato per la cartella soggetti ({subj_folder}) non è una cartella.")
        else:
            for cf in cf_list:
                full_path = os.path.join(subj_folder, cf)
                if not os.path.isdir(full_path):  # Only if folder doesn't already exist
                    try:
                        os.mkdir(full_path)
                        count += 1
                    except Exception:  # TODO: narrow the error down if encountered
                        sg.popup_error(Strings.WRITE_ERROR)
            if count > 0:
                sg.popup(f"Creazione cartelle codice fiscale completata! Create {count} cartelle.")
            else:
                sg.popup(f"Non è stato necessario creare nuove cartelle.")


# ---- HELPER FUNCTIONS ---- #
"""
These functions are meant to be called from the above functions only and are meant to help keep the logic clean
"""


def open_dir(full_path_to_dir) -> bool:
    """
    Opens the specified directory using file explorer
    Note: only works on windows
    Returns False if directory doesn't exist, True if successful
    """
    if os.path.isdir(full_path_to_dir):
        os.startfile(full_path_to_dir)
        return True
    return False
