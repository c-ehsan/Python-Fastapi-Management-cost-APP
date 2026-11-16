import json
from pathlib import Path
from uuid import uuid4
import random


class DataLoader:
    BASE_DIR=Path(__file__).resolve().parent
    DATA_PATH=BASE_DIR / "Costs.json"



    def load_data(self):
        with open (f"{self.DATA_PATH}","r+") as f:
            content=json.load(f)
            return content
    
    def save_data(self,data):
        with open(self.DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
