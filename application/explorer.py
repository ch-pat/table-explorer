import pandas as pd
import PySimpleGUI as sg


class InteractiveData:
    """
    Contains the data from the loaded spreadsheet in a pandas dataframe.
    the `data` attribute contains the entire table and is accessed by all functions that need to create views.
    the `view` attribute holds the current view to be shown by the gui, without altering the original data.
    data should only be modified by specific functions called when the user wants to save changes.
    """
    # TODO: implement all methods dealing with the table here
    # TODO: the same InteractiveData object should be used as reference globally for modifying data.
    def __init__(self, filepath: str):
        self._data: pd.DataFrame = pd.read_excel(filepath)  # TODO: replace with getting data from file set in config
        self._view: list = self._data.values.tolist()

    @property
    def view(self) -> list:
        return self._view

    @view.setter
    def view(self, new_view: pd.DataFrame):
        self._view = new_view.values.tolist()

    @property
    def data(self) -> pd.DataFrame:
        return self._data

    @data.setter
    def data(self, new_data: pd.DataFrame):
        self._view = new_data.values.tolist()


# Global TABLE variable to be accessed by all modules that need to read or write to the excel file
excel_file = sg.user_settings()["excel_file"]
TABLE = InteractiveData(excel_file)
