from pathlib import Path
import shutil

# regole spostamenti
# path = Path.home() / "Downloads"
PATH = Path.home() / "Desktop"

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


def get_filtered_list(path, filters=["*"]):
    file_list = []
    for file_filter in filters:
        for file_name in path.glob(file_filter):
            if not file_name.is_dir():
                file_list.append(file_name)
    return file_list


def move_files_to_folder(move_list, dest_folder):
    for file_path in move_list:
        file_name = file_path.name
        print(f"Moving file {file_name} from folder {file_path.parent} to folder {dest_folder}")
        destination_path = dest_folder / file_name
        index = 1
        while destination_path.exists():
            # se il file esiste già, aggiunge un suffisso incrementale finché non trova un nome libero
            destination_path = dest_folder / f"{file_path.stem} ({index:02d}){file_path.suffix}"
            index += 1
        try:
            shutil.move(file_path, destination_path)
        except Exception as e:
            print(e)


# per ogni regola esegue lo spostamento
for rule in RULES:
    move_list = get_filtered_list(path=PATH, filters=rule["filters"])
    if move_list and not rule["dest_folder"].exists():
        print(f"Making folder {rule['dest_folder']}")
        rule["dest_folder"].mkdir()
    move_files_to_folder(move_list, rule["dest_folder"])
