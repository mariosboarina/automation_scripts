import schedule
from pathlib import Path
from tkinter import Tk, simpledialog
import time
from datetime import datetime, timedelta

# PARAMETRI DI CONFIGURAZIONE

# percorso file creato, modificare secondo le proprie esigenze
JOURNAL_FILE = Path.home() / "giornale di bordo.txt"

TIME_FORMAT = "%Y/%m/%d_%H:%M"

# orario di inizio e fine della raccolta note
START_TIME = "8:30"
END_TIME = "19:00"

# intervallo tra una richiesta di nota e la successiva
TIME_INTERVAL_MINUTES = 30

# tempo limite per una nuova richiesta se la precedente non è stata immessa (es: utente non è al pc)
DELAY_MINUTES_TO_ACCEPT = 5


def generate_timestamps(start_time, end_time, time_interval):
    """
    Genera lista di orari a intervalli regolari
    :param start_time:
    :param end_time:
    :param time_interval:
    :return: timestamps
    """
    timestamps = []
    current_time = datetime.strptime(start_time, "%H:%M")

    while current_time <= datetime.strptime(end_time, "%H:%M"):
        timestamps.append(current_time.strftime("%H:%M"))
        current_time += timedelta(minutes=time_interval)

    return timestamps


def append_to_file(text, file_path):
    """
    Aggiunge la stringa in coda al file
    :param text:
    :param file_path:
    :return:
    """
    with open(file_path, "a") as my_file:
        my_file.write(text + "\n")


def prompt_journal(hour=None):
    """Apre un popup per la richiesta di nota e accoda al file di giornale. Gestisce i casi in cui non richiedere"""
    if hour:
        # se fornita l'ora verifica di non essere troppo in ritardo
        now = datetime.now()
        scheduled_date_base = datetime.strptime(hour, '%H:%M')
        scheduled_date = datetime.today().replace(hour=scheduled_date_base.hour,
                                                  minute=scheduled_date_base.minute,
                                                  second=0, microsecond=0)
        if now - scheduled_date > timedelta(minutes=DELAY_MINUTES_TO_ACCEPT):
            return
        # stringa ora da usare nel file di giornale
        timestamp = scheduled_date.strftime(TIME_FORMAT)
    else:
        # ora attuale (default se non è fornita a strftime)
        timestamp = time.strftime(TIME_FORMAT)

    root = Tk()  # Finestra principale (necessaria per usare la finestra di dialogo)
    root.withdraw()  # Nasconde la finestra principale
    entry = simpledialog.askstring(f"{timestamp} - Giornale di bordo", "Testo di oggi:\t\t\t\t\t\t\t\t")
    if entry:
        journal_entry = timestamp + " -> " + entry
        # aggiunge la riga al file
        append_to_file(journal_entry, JOURNAL_FILE)



if __name__ == '__main__':
    hours = generate_timestamps(START_TIME, END_TIME, TIME_INTERVAL_MINUTES)
    print(hours)
    for hour in hours:
        schedule.every().day.at(hour).do(prompt_journal, hour=hour)
    while True:
        schedule.run_pending()
        # verifica eventi in sospeso ogni 30 secondi
        time.sleep(30)
