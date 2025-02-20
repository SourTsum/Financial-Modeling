import json
from pathlib import Path


def write_json(response, file):
    try:
        file_path = Path(file)
        file_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure parent directories exist

        with file_path.open("w", encoding="utf-8") as open_file:
            json.dump(response, open_file, ensure_ascii=False, indent=4)
    except Exception as e:
        log_error(e)
        print(f"[API Controller]: {file} file doesn't exist OR can't write to file...")


def write_text(response, file):
    try:
        file_path = Path(file)
        file_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure parent directories exist

        with file_path.open("w", encoding="utf-8") as open_file:
            open_file.write(response)
    except Exception as e:
        log_error(e)
        print(f"[API Controller]: {file} file doesn't exist OR can't write to file...")


def get_json(file):
    try:
        file_path = Path(file)

        with file_path.open("r", encoding="utf-8") as open_file:
            return json.load(open_file)
    except Exception as e:
        log_error(e)
        return None


def log_error(e):
    log_file = Path("./output/logs.txt")
    log_file.parent.mkdir(parents=True, exist_ok=True)

    with log_file.open("a", encoding="utf-8") as logging:
        logging.write(str(e) + "\n")
