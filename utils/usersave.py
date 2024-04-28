from supabase import create_client
from configuration.config import SUPABASE_KEY, SUPABASE_URL

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def post_usersave(*args, **kwargs):
    '''Saves user info to databse ''' 
    user_name = kwargs["user_name"]
    uyt_reg = kwargs["uyt_reg"]
    data, count = supabase.table("user_info").insert({"username":user_name, "utyreg": uyt_reg}).execute()

