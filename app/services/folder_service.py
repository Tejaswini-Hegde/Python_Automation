import os
from datetime import datetime
from app.config.settings import BASE_AUTOMATION_PATH


def create_runtime_folders():
    if not BASE_AUTOMATION_PATH:
        raise ValueError(
            "BASE_AUTOMATION_PATH is not set in the env variables")
    """ if not os.path.exists(BASE_AUTOMATION_PATH):
        os.makedirs(BASE_AUTOMATION_PATH) """

    # Create a timestamped folder for the current runtime
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H-%M-%S")

    base_date_path = os.path.join(BASE_AUTOMATION_PATH, current_date)
    if not os.path.exists(base_date_path):
        print(base_date_path, "does not exist. Creating it.")
        os.makedirs(base_date_path)

    folders = ["Input", "Output", "Log", "Reference"]
    for folder in folders:
        path = os.path.join(base_date_path, folder)
        os.makedirs(path, exist_ok=True)
    return base_date_path
