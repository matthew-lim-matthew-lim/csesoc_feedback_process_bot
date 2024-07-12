import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

sheet_id = os.getenv('GOOGLE_SHEET_ID')

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

print(df)

print(df["Port"])