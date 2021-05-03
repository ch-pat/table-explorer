import PySimpleGUI as sg
import pandas as pd
import threading

from application import ui, explorer, callbacks
from application.strings import Strings, Keys

sg.set_options(auto_size_buttons=True)
sg.theme("Default")

# Preliminary steps
callbacks.load_settings()

window_title = f"Database in uso: {sg.user_settings()['excel_file']}"
window = sg.Window(window_title, layout=ui.main_layout(), grab_anywhere=False)

while True:  # Main update loop
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        # TODO: add close warning (if not saved?)
        break

    tb: sg.Table = window[Keys.MAINTABLE]

    if event == Keys.SEARCH:
        # TODO: rework filtering into a class function and make use of view
        filter_word = window[Keys.SEARCHINPUT].get()
        filtered_data = explorer.TABLE.data[explorer.TABLE.data['nome'].str.contains(filter_word, na=False)]
        tb.update(filtered_data.values.tolist())

    print(event)
    print(tb.SelectedRows)

window.close()
