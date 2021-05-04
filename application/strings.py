class Strings:
    SEARCH = "Cerca"
    CHOOSE_FOLDER_SUBJECTS = "Scegli cartella soggetti"
    CHOOSE_EXCEL_FILE = "Scegli file Excel"
    CONFIRM = "Conferma"
    CONFIGURATION = "Configurazione"
    FILL_CONFIG = "Selezionare sia la cartella dei soggetti che il file Excel da usare come database per procedere."
    FILL_TEXT = "Compilare il campo per proseguire"
    CONFIG_NOT_EXISTS = "Il file o la cartella selezionati non esistono.\nRieffettuare la selezione."
    CONFIG_ERROR = "Rilevato un errore nella configurazione esistente.\nPuò essere dovuto allo spostamento del file" \
                   " usato come database o della cartella soggetti.\nRitorno alla configurazione iniziale."
    OPEN_FOLDER = "Apri cartella soggetto"
    YES = "Si"
    NO = "No"
    CANCEL = "Annulla"
    WRITE_ERROR = "Si è verificato un errore. Probabilmente non si dispone dei permessi necessari per la scrittura."
    MENU_CREATE_FOLDERS = "Questa è un'utilità da usare al primo avvio dell'applicazione per impostare correttamente " \
                          "la cartella Soggetti.\n\n" \
                          "La cartella Soggetti deve contenere esclusivamente cartelle nel formato:\n\n" \
                          "'RSSMRA80A01H501U'\n\n" \
                          "Ovvero il codice fiscale della persona a cui corrisponde la cartella.\n\n" \
                          "Cliccando 'Conferma' saranno create, all'interno della cartella Soggetti, cartelle " \
                          "codice fiscale per ogni soggetto presente nel database che non ne abbia già una."


class Keys:
    SEARCHINPUT = "-SEARCHINPUT-"
    SEARCH = "-SEARCH-"
    SUBJECTSFOLDER = "-SUBJECTSFOLDER-"
    EXCELFILE = "-EXCELFILE-"
    CONFIRM = "-CONFIRM-"
    FILLCONFIGTEXT = "-FILLCONFIGTEXT-"
    MAINTABLE = "-MAINTABLE-"
    OPENFOLDER = "-OPENFOLDER-"

    MENUCREATEFOLDERS = "Crea cartelle soggetti::MENUCREATEFOLDERS"
    MENUCHANGESUBJECTSFOLDER = "Cambia cartella soggetti::CHANGESUBJECTSFOLDER"
    MENUCHANGEEXCELFILE = "Cambia file Excel::MENUCHANGEEXCELFILE"
