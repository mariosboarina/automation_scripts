# Giornale di Bordo Automatizzato

Questo progetto Python è uno script per raccogliere note regolari durante la giornata, basato su orari predefiniti. Ogni nota viene registrata in un file di testo, il "giornale di bordo", per tenere traccia delle attività quotidiane in modo semplice ed efficiente.

## Funzionalità

- Raccoglie automaticamente le note a intervalli regolari durante l'orario lavorativo.
- Le note vengono inserite tramite una finestra popup generata con `Tkinter`.
- Le risposte vengono salvate in un file di testo, con timestamp (giorno e ora) per ogni voce.
- Se non si risponde entro un certo limite di tempo, la richiesta di nota viene saltata.
- Configurazione flessibile degli orari di inizio, fine e dell'intervallo tra le richieste.

## Configurazione

### Parametri Principali

Nel file di script è possibile modificare i seguenti parametri per adattare lo script alle proprie esigenze:

- **`JOURNAL_FILE`**: il percorso del file di testo dove verranno salvate le note. Di default, è il file `giornale di bordo.txt` nella directory principale dell'utente.
- **`START_TIME`**: l'orario di inizio della raccolta note. Esempio: `8:30`.
- **`END_TIME`**: l'orario di fine della raccolta note. Esempio: `19:00`.
- **`TIME_INTERVAL_MINUTES`**: intervallo in minuti tra una richiesta di nota e la successiva. Esempio: `30` minuti.
- **`DELAY_MINUTES_TO_ACCEPT`**: tempo limite per accettare una nota prima di saltarla. Esempio: `5` minuti.

## Requisiti

- Python 3.8 o superiore
- Le seguenti librerie Python:
  - `schedule`
  - `tkinter` (generalmente già incluso in Python)
  - `pathlib`

Per installare la libreria `schedule`, eseguire il seguente comando:
```bash
pip install schedule
```
## Come Utilizzare

1. Clonare il repository:
   ```bash
   git clone https://github.com/tuo-username/giornale-di-bordo.git
   cd giornale-di-bordo
   ```

2. Modificare i parametri di configurazione all'interno dello script Python, se necessario.

3. Eseguire lo script:
   ```bash
   python script.py
   ```

4. Lo script inizierà a raccogliere le note agli orari configurati, generando finestre popup per richiedere l'inserimento del testo. Le note verranno salvate automaticamente nel file di giornale di bordo.
5. È anche possibile creare un collegamento per l'avvio dello script (con il comando al punto 3) e inserislo nella cartella di avvio automatico del sistema (nel caso Windows) 

## Struttura del File di Giornale

Le note raccolte verranno salvate nel seguente formato:

```
YYYY/MM/DD_HH:MM -> Testo inserito dall'utente
```

Ad esempio:
```
2024/10/08_08:30 -> Inizio attività giornaliera
2024/10/08_09:00 -> Riunione con il team
```

## Personalizzazione

È possibile personalizzare ulteriormente il comportamento dello script modificando:
- L'intervallo di tempo tra le note (`TIME_INTERVAL_MINUTES`).
- Gli orari di inizio e fine raccolta (`START_TIME` e `END_TIME`).

## Contributi

I contributi a questo progetto sono benvenuti! Sentitevi liberi di aprire una issue o creare una pull request.

## Licenza

Questo progetto è rilasciato sotto la licenza MIT. Vedi il file [LICENSE](LICENSE) per i dettagli.
```