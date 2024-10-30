# folder-reorder: uno script per riordinare le cartelle

Questo script sposta i file da una cartella a diverse cartelle di destinazione, a seconda dell'estensione o altri filtri sul nome file.

Ad esempio, è possibile spostare tutte le immagini nella sottocartella Immagini, tutti i file PDF e Word nella cartella Docs, ecc.

Se un file esiste già nella cartella di destinazione verrà rinominato aggiungendo un indice numerico incrementale al nome file, in modo da non sovrascrivere mai alcun dato.

**Consiglio di lanciare lo script con un collegamento, da mettere per esempio nel menu di sistema o sul desktop, per lanciarlo in pochi istanti**

#
## Configurazione

### Parametri Principali

Nel file di script è possibile modificare i seguenti parametri per adattare lo script alle proprie esigenze:
- **`PATH`**: percorso della cartella da riordinare, es `Path.home() / "Desktop"`
- **`RULES`**: è una lista di regole per spostare i file
  - Ogni regola è un dizionario con le keyword `"filters"` e `"dest_folder"`
    - `"filters"` contiene una lista si stringhe di filtro per i file da selezionare: es. `"filters": ["*.png", "*.gif", "*.jpg", "*.jpeg"]` per selezionare diversi formati di immagine.
- `"dest_folder"` è la cartella in cui spostare i file selezionati (usare `PATH / "nomecartella"` per spostare in una sottocartella). Se la cartella non esiste verrà creata.
- Un esempio di regole (puoi partire da questo e personalizzarlo):
``` python
RULES = (
{"filters": ["*.png", "*.gif", "*.jpg", "*.jpeg"], "dest_folder": PATH / "images"},
{"filters": ["*.pdf"], "dest_folder": PATH / "pdf"},
{"filters": ["*.zip", "*.rar"], "dest_folder": PATH / "archives"},
{"filters": ["*.pkg", "*.stp", "*.step", "*.dwg", "*.dxf"], "dest_folder": PATH / "cad"},
{"filters": ["*.wav", "*.mp3", "*.flac"], "dest_folder": PATH / "audio"},
{"filters": ["*.mpg", "*.mp4", "*.avi"], "dest_folder": PATH / "video"},
{"filters": ["*.txt", "*.md"], "dest_folder": PATH / "note"},
{"filters": ["*.msi", "*setup*.exe", "*install*.exe"], "dest_folder": PATH / "installers"}
)
```
## Requisiti

- Python 3.8 o superiore

## Come Utilizzarlo

1. 1. Clonare il repository o scaricare da github (consigliabile in una sottocartella della propria Home es. journaling):

2. Modificare i parametri di configurazione all'interno dello script Python, se necessario.

3. Posizionarsi nella cartella ed eseguire lo script:
   ```bash
   python folder-reorder.py
   ```
   NB: come sempre, suggerisco di creare un collegamento con questo comando per averlo a portata di click.
 
4. A ogni esecuzione lo script esegue gli spostamenti necessari seguendo le regole impostate.



## Contributi

I contributi a questo progetto sono benvenuti! Sentitevi liberi di aprire una issue o creare una pull request.

## Licenza

Questo progetto è rilasciato sotto la licenza MIT. Vedi il file [LICENSE](LICENSE) per i dettagli.
```