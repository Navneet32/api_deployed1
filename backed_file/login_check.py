import time
import os
from dotenv import load_dotenv
from supabase import create_client

def supabase_setup(contacts: list):
    load_dotenv()
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("Supabase credentials are missing in the .env file.")
        return
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    try:
        response = supabase.table("grow_next1").insert(contacts).execute()
        time.sleep(0.5)
        print("Inserted contacts to Supabase:", response)
    except Exception as e:
        print("Supabase insert error:", e)