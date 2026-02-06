from dotenv import load_dotenv
import os
from app.services.folder_service import create_runtime_folders


def main():
    load_dotenv()
    print("My Python project started")
    """ print("ENV=", os.getenv("ENV"))
    print("MYCREATION=", os.getenv("APP_NAME")) """
    base_path = create_runtime_folders()
    print(f"Runtime folders created at: {base_path}")


if __name__ == "__main__":
    main()
