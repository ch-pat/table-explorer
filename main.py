import PySimpleGUI as sg
import pandas as pd
import threading

from application import ui, explorer, callbacks
from application.strings import Strings, Keys

sg.set_options(auto_size_buttons=True)
sg.theme("DefaultNoMoreNagging")

# Preliminary steps
callbacks.load_settings()

window_title = f"Database in uso: {sg.user_settings()['excel_file']}"
window = sg.Window(window_title, layout=ui.main_layout(), grab_anywhere=False, size=(1280, 600), resizable=True)
tb: sg.Table = window[Keys.MAINTABLE]

while True:  # Main update loop
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        # TODO: add close warning (if not saved?)
        break

    print(event)

    if event == Keys.SEARCHINPUT:
        # TODO: rework filtering into a class function and make use of view
        filter_word = window[Keys.SEARCHINPUT].get()
        filtered_data = explorer.TABLE.data[explorer.TABLE.data['nome'].str.contains(filter_word, na=False)]
        tb.update(filtered_data.values.tolist())

    if event == Keys.OPENFOLDER and tb.SelectedRows:  # Only run if a row is actually selected
        # IMPORTANT indexes refer to the current view, NOT THE ACTUAL DATA
        # shouldn't matter here because no change is made to the data, but keep in mind
        selected_row = tb.SelectedRows[0]
        selected_row_content = tb.get()[selected_row]
        callbacks.open_subject_folder(selected_row, selected_row_content)

    if event == Keys.MENUCREATEFOLDERS:
        callbacks.menu_create_folders()

window.close()
