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
window = sg.Window(window_title, layout=ui.main_layout(), grab_anywhere=False, size=(1280, 600), resizable=True,
                   location=(0, 0))
tb: sg.Table = window[Keys.MAINTABLE]

while True:  # Main update loop
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        # TODO: add close warning (if not saved?)
        break

    print(event)

    if event == Keys.SEARCHINPUT:
        callbacks.filter_table(window)

    if event == Keys.OPENFOLDER:
        callbacks.open_subject_folder(window)

    if event == Keys.MENUCREATEFOLDERS:
        callbacks.menu_create_folders()

    if event == Keys.MENUCHANGESUBJECTSFOLDER:
        callbacks.menu_change_subjects_folder()

    if event == Keys.MENUCHANGEEXCELFILE:
        window = callbacks.menu_change_excel_file(window)

window.close()
