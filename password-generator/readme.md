# Generatore di password negli appunti

Questo script genera una password sicura e la copia negli appunti, pronta per essere incollata.

**Consiglio di lanciare lo script con un collegamento, cui si può associare una scorciatoia da tastiera in modo da avere sempre la password a portata di Ctr-V.**

## Funzionalità

- Personalizzabile per lunghezza password e tipi di caratteri contenuti

## Configurazione

### Parametri Principali

Nel file di script è possibile modificare i seguenti parametri per adattare lo script alle proprie esigenze:
- **`LENGTH`**: numero di caratteri della password
- **`INCLUDE_DIGITS`**: se True include cifre numeriche
- **`INCLUDE_SPECIAL_CHARS`**: se True include caratteri speciali
- **`INCLUDE_UPPERCASE`**: se True include le maiuscole

## Requisiti

- Python 3.8 o superiore
- Le seguenti librerie Python:
  - `pyperclip`


Per installare la libreria `pyperclip`, eseguire il seguente comando:
```bash
pip install pyperclip
```
## Come Utilizzare

1. 1. Clonare il repository o scaricare da github (consigliabile in una sottocartella della propria Home es. journaling):

2. Modificare i parametri di configurazione all'interno dello script Python, se necessario.

3. Posizionarsi nella cartella ed eseguire lo script:
   ```bash
   python password-generator.py
   ```
   NB: è molto utile creare un collegamento a questo comando in modo da generare la password in modo veloce; 
   ancora meglio, si può associare una scorciatoia da tastiera (es. Ctrl-alt-P) per avere la password pronta da incollare in un istante, senza dover uscire dall'applicazione in cui si vuole incollare e senza usare il mouse.
 
4. A ogni esecuzione lo script incolla negli appunti una nuova password, pronta per essere incollata dove serve.



## Contributi

I contributi a questo progetto sono benvenuti! Sentitevi liberi di aprire una issue o creare una pull request.

## Licenza

Questo progetto è rilasciato sotto la licenza MIT. Vedi il file [LICENSE](LICENSE) per i dettagli.
```