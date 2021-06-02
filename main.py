import PySimpleGUI as sg

from application import ui, explorer, callbacks
from application.strings import Strings, Keys

sg.set_options(auto_size_buttons=True)
sg.theme("DefaultNoMoreNagging")

# Preliminary steps
callbacks.load_settings()
explorer.define_table()
callbacks.first_run()

window_title = f"Database in uso: {sg.user_settings()['excel_file']}"
window = sg.Window(window_title, layout=ui.main_layout(), grab_anywhere=False, size=(ui.width, ui.height), resizable=True,
                   location=(0, 0), finalize=True)
window.maximize()
tb: sg.Table = window[Keys.MAINTABLE]

while True:  # Main update loop
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        # TODO: add close warning (if not saved?)
        break

    print(event)

    if event in Keys.SEARCHES:  # List of all search input fields (they trigger events on change)
        callbacks.filter_table_from_elements(window)

    if event == Keys.OPENFOLDER:
        callbacks.open_subject_folder(window)

    if event == Keys.MENUCREATEFOLDERS:
        callbacks.menu_create_folders()

    if event == Keys.MENUCHANGESUBJECTSFOLDER:
        callbacks.menu_change_subjects_folder()

    if event == Keys.MENUCHANGEEXCELFILE:
        window = callbacks.menu_change_excel_file(window)

    if event == Keys.EDITVAI:
        callbacks.filter_persone_collegate(window)

window.close()
