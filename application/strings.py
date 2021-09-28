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
    OPEN_FOLDER = "📁 Apri cartella soggetto"
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
    SAVE_CHANGES = "Salva Modifiche"
    DELETE_ROW = "Elimina Riga"
    ADD_NEW = "➕ Aggiungi nuovo soggetto"
    RELOAD = "↻ Aggiorna"
    SELECT_ROW = "Seleziona una riga della tabella prima di apportare modifiche!"
    SERVICES = "💼 Servizi"
    RELATED = "👥 Persone Collegate"


class Keys:
    # "Nome", "Cognome", "Codice Fiscale",
    # "Indirizzo", "CAP", "Comune", "Provincia",
    # "Telefono 1", "Telefono 2",
    # "E-mail 1", "E-mail 2",
    # "Persone collegate", "Rapporto",
    # "Servizio CAF", "Servizio Patronato",
    # "Prodotto Finanziario",
    # "Note",
    # "Dettagli Aggiuntivi",
    # "Data Tesseramento",
    # "Tipo Tessera",
    # "Numero Ricevuta",
    # "Contributo Volontario",
    # "Uscita"

    COLNOME = "Nome"
    COLCOGNOME = "Cognome"
    COLCF = "Codice Fiscale"
    COLINDIRIZZO = "Indirizzo"
    COLCAP = "CAP"
    COLCOMUNE = "Comune"
    COLPROV = "Provincia"
    COLTELEFONO1 = "Telefono 1"
    COLTELEFONO2 = "Telefono 2"
    COLMAIL1 = "E-mail 1"
    COLMAIL2 = "E-mail 2"
    COLCOLLEGATE = "Persone Collegate"
    COLRAPPORT0 = "Rapporto"
    COLSERVIZIOCAF = "Servizio CAF"
    COLSERVIZIOPATRONATO = "Servizio Patronato"
    COLFINANZIARIO = "Prodotto Finanziario"
    COLNOTE = "Note"
    COLDETTAGLI = "Dettagli Aggiuntivi"
    COLDATATESSERA = "Data Tesseramento"
    COLTIPOTESSERA = "Tipo Tessera"
    COLRICEVUTA = "Numero Ricevuta"
    COLCONTRIBUTO = "Contributo Volontario"
    COLUSCITA = "Uscita"

    SEARCHINPUTNOME = "-SEARCHINPUTNOME-"
    SEARCHINPUTCOGNOME = "-SEARCHINPUTCOGNOME-"
    SEARCHINPUTCF = "-SEARCHINPUTCF-"
    SEARCH = "-SEARCH-"

    # The two lists must correspond -- not elegant, should find a different way
    SEARCHES = [SEARCHINPUTNOME, SEARCHINPUTCOGNOME, SEARCHINPUTCF]
    SEARCHES_COLUMNS = [  # Contains column names as specified in InteractiveData.get_headings()
        'Nome', 'Cognome', 'Codice Fiscale'
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
    EDITDETTAGLI =      "-EDITDETTAGLI-",
    EDITDATATESSERA =   "-EDITDATATESSERA-",
    EDITTIPOTESSERA =   "-EDITTIPOTESSERA-",
    EDITRICEVUTA =      "-EDITRICEVUTA-",
    EDITCONTRIBUTO =    "-EDITCONTRIBUTO-",
    EDITUSCITA =        "-EDITUSCITA-"

    COLUMN_TO_FORM = {
        COLNOME: EDITNOME,
        COLCOGNOME: EDITCOGNOME,
        COLCF: EDITCODICEFISCALE,
        COLINDIRIZZO: EDITINDIRIZZO,
        COLCAP: EDITCAP,
        COLPROV: EDITPROV,
        COLCOMUNE: EDITCOMUNE,
        COLTELEFONO1: EDITTELEFONO1,
        COLTELEFONO2: EDITTELEFONO2,
        COLMAIL1: EDITMAIL1,
        COLMAIL2: EDITMAIL2,
        COLCOLLEGATE: EDITCOLLEGATE,
        COLRAPPORT0: EDITRAPPORTO,
        COLSERVIZIOCAF: EDITCAF,
        COLSERVIZIOPATRONATO: EDITPATRONATO,
        COLFINANZIARIO: EDITFINANZIARIO,
        COLNOTE: EDITNOTE,
        COLDETTAGLI: EDITDETTAGLI,
        COLDATATESSERA: EDITDATATESSERA,
        COLTIPOTESSERA: EDITTIPOTESSERA,
        COLRICEVUTA: EDITRICEVUTA,
        COLCONTRIBUTO: EDITCONTRIBUTO,
        COLUSCITA: EDITUSCITA
    }

    FORM_TO_COLUMN = {v: k for k, v in COLUMN_TO_FORM.items()}

    ADDNOME = "-ADDNOME-"
    ADDCOGNOME = "-ADDCOGNOME-"
    ADDCODICEFISCALE = "-ADDCODICEFISCALE-"
    ADDINDIRIZZO = "-ADDINDIRIZZO-"
    ADDCAP = "-ADDCAP-"
    ADDCOMUNE = "-ADDCOMUNE-"
    ADDPROV = "-ADDPROV-"
    ADDTELEFONO1 = "-ADDTELEFONO1-"
    ADDTELEFONO2 = "-ADDTELEFONO2-"
    ADDMAIL1 = "-ADDMAIL1-"
    ADDMAIL2 = "-ADDMAIL2-"
    ADDCOLLEGATE = "-ADDCOLLEGATE-"
    ADDRAPPORTO = "-ADDRAPPORTO-"
    ADDCAF = "-ADDCAF-"
    ADDPATRONATO = "-ADDPATRONATO-"
    ADDFINANZIARIO = "-ADDFINANZIARIO-"
    ADDNOTE = "-ADDNOTE-"
    ADDDETTAGLI = "-ADDDETTAGLI-",
    ADDDATATESSERA = "-ADDDATATESSERA-",
    ADDTIPOTESSERA = "-ADDTIPOTESSERA-",
    ADDRICEVUTA = "-ADDRICEVUTA-",
    ADDCONTRIBUTO = "-ADDCONTRIBUTO-",
    ADDUSCITA = "-ADDUSCITA-"
    ADDSAVE = "-ADDSAVE-"

    COLUMN_TO_ADD_FORM = {
        COLNOME: ADDNOME,
        COLCOGNOME: ADDCOGNOME,
        COLCF: ADDCODICEFISCALE,
        COLINDIRIZZO: ADDINDIRIZZO,
        COLCAP: ADDCAP,
        COLPROV: ADDPROV,
        COLCOMUNE: ADDCOMUNE,
        COLTELEFONO1: ADDTELEFONO1,
        COLTELEFONO2: ADDTELEFONO2,
        COLMAIL1: ADDMAIL1,
        COLMAIL2: ADDMAIL2,
        COLCOLLEGATE: ADDCOLLEGATE,
        COLRAPPORT0: ADDRAPPORTO,
        COLSERVIZIOCAF: ADDCAF,
        COLSERVIZIOPATRONATO: ADDPATRONATO,
        COLFINANZIARIO: ADDFINANZIARIO,
        COLNOTE: ADDNOTE,
        COLDETTAGLI: ADDDETTAGLI,
        COLDATATESSERA: ADDDATATESSERA,
        COLTIPOTESSERA: ADDTIPOTESSERA,
        COLRICEVUTA: ADDRICEVUTA,
        COLCONTRIBUTO: ADDCONTRIBUTO,
        COLUSCITA: ADDUSCITA
    }

    ADD_FORM_TO_COLUMN = {v: k for k, v in COLUMN_TO_ADD_FORM.items()}

    SUBJECTSFOLDER = "-SUBJECTSFOLDER-"
    EXCELFILE = "-EXCELFILE-"
    CONFIRM = "-CONFIRM-"
    FILLCONFIGTEXT = "-FILLCONFIGTEXT-"
    MAINTABLE = "-MAINTABLE-"
    OPENFOLDER = "-OPENFOLDER-"
    OPENSERVICES = "-OPENSERVICES-"
    OPENRELATED = "-OPENRELATED-"
    SAVE = "-SAVE-"
    DELETE = "-DELETE-"
    ADD = "-ADD-"
    FEEDBACK = "-FEEDBACK-"
    RELOAD = "-RELOAD-"

    MENUCREATEFOLDERS = "Crea cartelle soggetti::MENUCREATEFOLDERS"
    MENUCHANGESUBJECTSFOLDER = "Cambia cartella soggetti::CHANGESUBJECTSFOLDER"
    MENUCHANGEEXCELFILE = "Cambia file Excel::MENUCHANGEEXCELFILE"
