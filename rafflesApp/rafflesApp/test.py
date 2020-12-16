from pathlib import Path

BASE_DIR = Path(__file__).resolve()
absPath = BASE_DIR / 'home/db.sqlite3'

print(absPath)