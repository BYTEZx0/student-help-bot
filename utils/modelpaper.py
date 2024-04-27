from supabase import create_client, Client
from configuration.config import SUPABASE_KEY, SUPABASE_URL

def get_question_paper():
    print(f"{SUPABASE_URL=} + {SUPABASE_KEY=}")
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    res = supabase.table('user_info').select("*").execute()
    print(f"{res=}")

