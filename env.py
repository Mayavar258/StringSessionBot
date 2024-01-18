import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "23134975").strip()
API_HASH = os.getenv("API_HASH", "5c0a4b4bafb0418032faf4ec845a4df4").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6548114637:AAH9BQaGfv-Ml9-0oFItXP8Vj7HrxCmxbWI").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://ragav:ragav@cluster0.mv2hczu.mongodb.net/?retryWrites=true&w=majority").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "https://t.me/good_nation")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
