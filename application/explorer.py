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
        self.headings: list = self.get_headings()
        self.view_headings: list = self.get_view_headings()
        self._data: pd.DataFrame = pd.read_excel(filepath)
        self._view: list = self._data[self.view_headings].values.tolist()

    @property
    def view(self) -> list:
        return self._view

    @view.setter
    def view(self, new_view: pd.DataFrame):
        self._view = new_view[self.get_view_headings()].values.tolist()

    @property
    def data(self) -> pd.DataFrame:
        return self._data

    @data.setter
    def data(self, new_data: pd.DataFrame):
        self._view = new_data.values.tolist()

    def get_headings(self) -> list:
        # TODO maybe get from file rather than keeping hardcoded
        headings = [
            "Nome", "Cognome", "Codice Fiscale",
            "Indirizzo", "CAP", "Comune", "Provincia",
            "Telefono 1", "Telefono 2",
            "E-mail 1", "E-mail 2",
            "Persone collegate", "Rapporto",
            "Servizio CAF", "Servizio Patronato",
            "Prodotto Finanziario",
            "Note",
            "Dettagli Aggiuntivi",
            "Data Tesseramento",
            "Tipo Tessera",
            "Numero Ricevuta",
            "Contributo Volontario",
            "Uscita"
        ]
        return headings

    def get_view_headings(self):
        headings = [
            "Nome", "Cognome", "Codice Fiscale", "Telefono 1", "E-mail 1"
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
        assert len(row) == len(self.view_headings)
        idx = self.get_codice_fiscale_index()
        cf = row[idx]
        return cf.upper()

    def get_codice_fiscale_list(self):
        cf_heading = self.get_headings()[self.get_codice_fiscale_index()]
        return self.data[cf_heading].values.tolist()

    def filter_view(self, columns: list, queries: list):
        """
        Modifies the view according to the filters defined
        :param columns: columns on which the filtering must be performed
        :param queries: the strings to search within the column
        """
        dataframe_view = self.data.__deepcopy__()
        for (column, query) in zip(columns, queries):
            dataframe_view = dataframe_view[dataframe_view[column].str.contains(query, na=False, case=False)]
        self.view = dataframe_view

    def gives_results(self, columns: list, queries: list) -> bool:
        """ Returns True if the query contains any result """
        results = self.data.__deepcopy__()
        for (column, query) in zip(columns, queries):
            results = results[results[column].str.contains(query, na=False, case=False)]
        return len(results) > 0


# Global TABLE variable to be accessed by all modules that need to read or write to the excel file
TABLE: InteractiveData = None


def define_table():
    sg.user_settings_load()
    excel_file = sg.user_settings()["excel_file"]
    global TABLE
    TABLE = InteractiveData(excel_file)
