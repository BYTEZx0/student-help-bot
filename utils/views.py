from supabase import create_client, Client
from configuration.config import SUPABASE_KEY, SUPABASE_URL

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

#this will be replaced by a logic to take question paper from local storage
def get_question_paper():
    '''to fetch question paper from supabase bucket'''
    print(f"{SUPABASE_URL=} + {SUPABASE_KEY=}")
    res = supabase.table('user_info').select("*").execute()
    print(f"{res=}")

def post_usersave(*args, **kwargs):
    '''Saves user info to database ''' 
    user_name = kwargs["user_name"]
    uyt_reg = kwargs["uyt_reg"]
    chat_id = kwargs["chat_id"]
    data, count = supabase.table("user_info").insert({"username":user_name, "utyreg": uyt_reg, "chatid": chat_id}).execute()

def post_aadhar_update(*args, **kwargs):
    aadhar_no = kwargs["aadhar_no"]
    chat_id = kwargs["chat_id"]
    data, count = supabase.table("user_info").update({"aadhar_no": aadhar_no}).eq("chatid", chat_id).execute()

def post_dob_update(*args, **kwargs):
    dob = kwargs["dob"]
    chat_id = kwargs["chat_id"]
    data, count = supabase.table("user_info").update({"dob": dob}).eq("chatid", chat_id).execute()