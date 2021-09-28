import pandas as pd
import PySimpleGUI as sg
import os


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
        self._data: pd.DataFrame = pd.read_excel(filepath, dtype=str).fillna("")
        self._view: list = self._data[self.view_headings].values.tolist()
        self.filepath: str = filepath

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
        self._data = new_data.fillna("")

    def get_headings(self) -> list:
        # TODO maybe get from file rather than keeping hardcoded
        headings = [
            "Nome", "Cognome", "Codice Fiscale",
            "Indirizzo", "CAP", "Comune", "Provincia",
            "Telefono 1", "Telefono 2",
            "E-mail 1", "E-mail 2",
            "Persone Collegate", "Rapporto",
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

    def get_data_row(self, cf: str) -> dict:
        """
        :param cf: the Codice Fiscale of the desired row
        :return dict: the dictionary containing the requested data
        """
        row = self.data[self.data['Codice Fiscale'].str.lower() == cf.lower()]
        idx = row.index.values.astype(int)[0]
        row = row.to_dict()
        result = {k: v[idx] for k, v in row.items()}
        return result

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

    def update_row(self, cf: str, data: dict):
        """
        Updates row identified by cf with the data provided and saves to file
        :param cf:
        :param data:
        :return:
        """
        # Reload file before applying changes in case someone else modified it
        self.reload_data()
        # Apply changes if needed
        cf_column = self.data["Codice Fiscale"].str.lower()
        if cf.lower() in cf_column.values.tolist():
            new_row = [data[k] for k in self.get_headings()]
            idx = self.data[self.data["Codice Fiscale"].str.lower() == cf.lower()].index
            self.data.at[idx, :] = new_row
            self.data = self.data
            # Save file and update view
            self.save_data_to_file()
            self.view = self.data
            if cf != data["Codice Fiscale"]:
                update_subject_folder_name(cf, data["Codice Fiscale"])
        else:
            sg.popup_ok("Il soggetto selezionato per la modifica non è stato trovato. È possibile che un altro utente"
                        " abbia cancellato il soggetto o ne abbia modificato il codice fiscale.")

    def delete_row(self, cf: str):
        # Reload file before applying changes in case someone else modified it
        self.reload_data()
        # Apply changes if needed
        cf_column = self.data["Codice Fiscale"].str.lower()
        if cf.lower() in cf_column.values.tolist():
            idx = self.data[cf_column == cf.lower()].index
            self.data.drop(index=idx, inplace=True)
            # Save file and update view (again) only if changes have been made
            # otherwise, view has already been updated in reload_data()
            self.save_data_to_file()
            self.view = self.data

    def add_row(self, data):
        # Reload file before applying changes in case someone else modified it
        self.reload_data()
        # Apply changes if needed
        cf_column = self.data["Codice Fiscale"].str.lower()
        if data["Codice Fiscale"].lower() not in cf_column.values.tolist():
            new_row = [str(data[k]) for k in self.get_headings()]
            new_row = pd.DataFrame([new_row], columns=self.get_headings())
            self.data = self.data.append(new_row, ignore_index=True)
            # Save file and update view
            self.save_data_to_file()
            self.view = self.data

    def reload_data(self):
        self.data = pd.read_excel(self.filepath).fillna("")
        self.view = self.data

    def save_data_to_file(self):
        self.data.to_excel(self.filepath, index=False, float_format="%.0f")

    def codice_fiscale_already_exists(self, cf: str):
        if cf in self.get_codice_fiscale_list():
            return True
        return False


# Global TABLE variable to be accessed by all modules that need to read or write to the excel file
TABLE: InteractiveData = None


def define_table():
    sg.user_settings_load()
    excel_file = sg.user_settings()["excel_file"]
    global TABLE
    TABLE = InteractiveData(excel_file)


def update_subject_folder_name(old_cf: str, new_cf: str):
    subj_folder = sg.user_settings()["subjects_folder"]
    full_path_old = os.path.join(subj_folder, old_cf.upper())
    full_path_new = os.path.join(subj_folder, new_cf.upper())
    try:
        os.rename(full_path_old, full_path_new)
    except PermissionError:
        os.mkdir(full_path_new)
        sg.popup_ok("Non è stato possibile aggiornare la cartella del soggetto! Un altro processo sta "
                    "utilizzando un file presente nella cartella.\nÈ stata creata la nuova cartella ma "
                    "occorre spostare manualmente i file del soggetto modificato.")
