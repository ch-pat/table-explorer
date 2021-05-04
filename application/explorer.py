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
    def __init__(self, filepath: str = sg.user_settings()["excel_file"]):
        self._data: pd.DataFrame = pd.read_excel(filepath)
        self._view: list = self._data.values.tolist()
        self.headings: list = self.get_headings()

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

    def get_headings(self) -> list:
        # TODO maybe get from file rather than keeping hardcoded
        headings = [
            "nome",
            "cognome",
            "Codice Fiscale",
            "indirizzo",
            "cap",
            "comune",
            "prov",
            "telefono 1",
            "telefono 2",
            "mail 1",
            "mail 2",
            "persone collegate",
            "rapporto",
            "servizio CAF",
            "servizio Patronato",
            "prodotto Finanziario",
            "Note"
        ]
        return headings

    def get_codice_fiscale_index(self) -> int:
        """
        Returns the index corresponding to the 'Codice Fiscale' field in the headings
        """
        return self.headings.index('Codice Fiscale')

    def extract_codice_fiscale_from_row(self, row) -> str:
        """
        Takes a list in the shape of a row of the dataset (must have same length)
        Returns the value of the codice fiscale column
        """
        assert len(row) == len(self.headings)
        idx = self.get_codice_fiscale_index()
        cf = row[idx]
        return cf.upper()

    def get_codice_fiscale_list(self):
        cf_heading = self.get_headings()[self.get_codice_fiscale_index()]
        return self.data[cf_heading].values.tolist()


# Global TABLE variable to be accessed by all modules that need to read or write to the excel file
TABLE = InteractiveData()
