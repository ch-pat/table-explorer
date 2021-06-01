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
    # "nome", "cognome", "Codice Fiscale",
    # "indirizzo", "cap", "comune", "prov",
    # "telefono 1", "telefono 2",
    # "mail 1", "mail 2",
    # "persone collegate", "rapporto",
    # "servizio CAF", "servizio Patronato",
    # "prodotto Finanziario",
    # "Note"
    COLNOME = "nome"
    COLCOGNOME = "cognome"
    COLCF = "Codice Fiscale"
    COLINDIRIZZO = "indirizzo"
    COLCAP = "cap"
    COLCOMUNE = "comune"
    COLPROV = "prov"
    COLTELEFONO1 = "telefono 1"
    COLTELEFONO2 = "telefono 2"
    COLMAIL1 = "mail 1"
    COLMAIL2 = "mail 2"
    COLCOLLEGATE = "persone collegate"
    COLRAPPORT0 = "rapporto"
    COLSERVIZIOCAF = "servizio CAF"
    COLSERVIZIOPATRONATO = "servizio Patronato"
    COLFINANZIARIO = "prodotto Finanziario"
    COLNOTE = "Note"

    SEARCHINPUTNOME = "-SEARCHINPUTNOME-"
    SEARCHINPUTCAP = "-SEARCHINPUTCAP-"
    SEARCHINPUTCF = "-SEARCHINPUTCF-"
    SEARCH = "-SEARCH-"

    # The two lists must correspond -- not elegant, should find a different way
    SEARCHES = [SEARCHINPUTNOME, SEARCHINPUTCAP, SEARCHINPUTCF]
    SEARCHES_COLUMNS = [  # Contains column names as specified in InteractiveData.get_headings()
        'nome', 'cap', 'Codice Fiscale'
    ]

    # ---- EDIT FIELDS ---- #

    EDITNOME =          "-EDITNOME-"
    EDITCOGNOME =       "-EDITCOGNOME-"
    EDITCODICEFISCALE = "-EDITCODICEFISCALE-"
    EDITINDIRIZZO =     "-EDITINDIRIZZO-"
    EDITCAP =           "-EDITCAP-"
    EDITCOMUNE =        "-EDITCOMUNE-"
    EDITPROV =          "-EDITPROV-"
    EDITTELEFONO1 =     "-EDITTELEFONO1-"
    EDITTELEFONO2 =     "-EDITTELEFONO2-"
    EDITMAIL1 =         "-EDITMAIL1-"
    EDITMAIL2 =         "-EDITMAIL2-"
    EDITCOLLEGATE =     "-EDITCOLLEGATE-"
    EDITRAPPORTO =      "-EDITRAPPORTO-"
    EDITVAI =           "-EDITVAI-"
    EDITCAF =           "-EDITCAF-"
    EDITPATRONATO =     "-EDITPATRONATO-"
    EDITFINANZIARIO =   "-EDITFINANZIARIO-"
    EDITNOTE =          "-EDITNOTE-"


    SUBJECTSFOLDER = "-SUBJECTSFOLDER-"
    EXCELFILE = "-EXCELFILE-"
    CONFIRM = "-CONFIRM-"
    FILLCONFIGTEXT = "-FILLCONFIGTEXT-"
    MAINTABLE = "-MAINTABLE-"
    OPENFOLDER = "-OPENFOLDER-"

    MENUCREATEFOLDERS = "Crea cartelle soggetti::MENUCREATEFOLDERS"
    MENUCHANGESUBJECTSFOLDER = "Cambia cartella soggetti::CHANGESUBJECTSFOLDER"
    MENUCHANGEEXCELFILE = "Cambia file Excel::MENUCHANGEEXCELFILE"
