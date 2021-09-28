import PySimpleGUI as sg
from codicefiscale import codicefiscale
from application import ui
from application.strings import Strings, Keys
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


def open_subject_folder(window: sg.Window):
    cf = window[Keys.EDITCODICEFISCALE].get()
    if not cf:
        return

    subj_folder = sg.user_settings()["subjects_folder"]
    full_path = os.path.join(subj_folder, cf.upper())
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
                full_path = os.path.join(subj_folder, cf.upper())
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


def menu_change_subjects_folder():
    new_folder = ui.edit_subjects_folder_window()
    if new_folder:
        sg.user_settings_set_entry("subjects_folder", new_folder)


def menu_change_excel_file(window: sg.Window) -> sg.Window:
    """
    Changes the excel file used for the displayed table
    needs to update the table element and returns it to give back control to main
    """
    new_excel_file = ui.edit_excel_file_window()
    if new_excel_file:
        sg.user_settings_set_entry("excel_file", new_excel_file)
        # Update window elements
        explorer.TABLE = explorer.InteractiveData(new_excel_file)
        new_window_title = f"Database in uso: {sg.user_settings()['excel_file']}"
        new_window = sg.Window(new_window_title, layout=ui.main_layout(), grab_anywhere=False, size=(1280, 600),
                               location=(0, 0), resizable=True)
        window.close()
        del window
        return new_window
    return window


def filter_table_from_elements(window: sg.Window):
    """ Applies a filter to the table view and update the Table element to reflect the changes
        Uses keywords filled in the ui search forms
    """
    filter_words = [window[i].get() for i in Keys.SEARCHES]
    columns = Keys.SEARCHES_COLUMNS
    filter_table(window, columns, filter_words)


def filter_table(window: sg.Window, columns: list, filter_words: list):
    tb: sg.Table = window[Keys.MAINTABLE]  # Grab table element from window

    explorer.TABLE.filter_view(columns, filter_words)  # Apply filter(s)
    tb.update(explorer.TABLE.view)  # Update ui table


def filter_persone_collegate(window: sg.Window):
    persone_collegate = window[Keys.EDITCOLLEGATE].get()
    columns1 = [Keys.COLNOME, Keys.COLCOGNOME]
    columns2 = columns1[::-1]
    if len(persone_collegate.split()) == 0:
        # Empty field, early return to prevent crashing
        return
    query = [persone_collegate.split()[0], persone_collegate.split()[-1]]

    # No guarantee in how this is written, try assuming it's [name, surname] or viceversa
    # Hopefully it's just two names most times
    if explorer.TABLE.gives_results(columns1, query):
        filter_table(window, columns1, query)
    elif explorer.TABLE.gives_results(columns2, query):
        filter_table(window, columns2, query)
    else:
        filter_table(window, [], [])


def load_input_forms(window: sg.Window):
    tb: sg.Table = window[Keys.MAINTABLE]
    if not tb.SelectedRows:  # Only run if a row is actually selected
        return

    row_index = tb.SelectedRows[0]
    row_content = tb.get()[row_index]
    cf = explorer.TABLE.extract_codice_fiscale_from_row(row_content)
    data = explorer.TABLE.get_data_row(cf)
    load_data_to_forms(window, data)


def save_changes(window: sg.Window):
    tb: sg.Table = window[Keys.MAINTABLE]
    if not tb.SelectedRows:  # Only run if a row is actually selected
        sg.popup_ok("Selezionare una riga da modificare dalla tabella")
        return

    # Get current CF in case it gets changed
    row_index = tb.SelectedRows[0]
    row_content = tb.get()[row_index]
    cf = explorer.TABLE.extract_codice_fiscale_from_row(row_content)

    # grab data from window
    data = {}
    for k in Keys.FORM_TO_COLUMN.keys():
        if k in window.key_dict:
            data[Keys.FORM_TO_COLUMN[k]] = window[k].get()
        else:
            data[Keys.FORM_TO_COLUMN[k]] = None

    new_cf = data[Keys.COLCF]
    if codicefiscale.is_valid(new_cf):
        if new_cf.lower() != cf.lower():  # If you are changing the cf, make sure new one is not duplicate
            if not explorer.TABLE.codice_fiscale_already_exists(new_cf):
                # TODO: change subject folder name here
                explorer.TABLE.update_row(cf, data)
                tb.update(explorer.TABLE.view)
            else:
                sg.popup_error("Codice fiscale inserito già presente nel database!")
        else:
            explorer.TABLE.update_row(cf, data)
            tb.update(explorer.TABLE.view)
    else:
        sg.popup_error("Codice fiscale inserito non valido!")


def delete_row(window: sg.Window):
    tb: sg.Table = window[Keys.MAINTABLE]
    if not tb.SelectedRows:  # Only run if a row is actually selected
        return

    text = "ATTENZIONE!!!\n\nSi sta cercando di cancellare la riga attualmente selezionata! Confermare solo se si" \
           " vuole veramente cancellare la riga selezionata."

    if not ui.yes_no_window(text):
        return

    # Get current CF in case it gets changed
    row_index = tb.SelectedRows[0]
    row_content = tb.get()[row_index]
    cf = explorer.TABLE.extract_codice_fiscale_from_row(row_content)
    explorer.TABLE.delete_row(cf)
    tb.update(explorer.TABLE.view)


def add_new_row(window: sg.Window):
    data = ui.add_new_row_window()
    if data:
        explorer.TABLE.add_row(data)
        tb: sg.Table = window[Keys.MAINTABLE]
        tb.update(explorer.TABLE.view)


def reload_data(window: sg.Window):
    tb: sg.Table = window[Keys.MAINTABLE]
    explorer.TABLE.reload_data()
    tb.update(explorer.TABLE.view)


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


def load_data_to_forms(window: sg.Window, data: dict):
    """
    Loads data of a row to the input forms of the ui window
    :param window: the ui window object
    :param data: dict containing all the data
    :return:
    """
    for k in data.keys():
        form_key = Keys.COLUMN_TO_FORM[k]
        if form_key in window.key_dict:
            window[form_key].update(data[k])
