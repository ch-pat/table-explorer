import PySimpleGUI as sg
from application import ui
from application.strings import Strings
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
