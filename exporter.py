import os
import json
import pandas as pd

def export_to_csv(data: list[dict], filename: str = "output.csv"):
    os.makedirs("output", exist_ok=True)
    path = f"output/{filename}"
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)
    print(f"Saved to {path}")
    return path

def export_to_json(data: list[dict], filename: str = "output.json"):
    os.makedirs("output", exist_ok=True)
    path = f"output/{filename}"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved to {path}")
    return path
