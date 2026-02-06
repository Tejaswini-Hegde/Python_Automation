import os
from dotenv import load_dotenv

load_dotenv()

BASE_AUTOMATION_PATH = os.getenv("BASE_AUTOMATION_PATH")
ENV = os.getenv("ENV")
