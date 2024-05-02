import requests

files = {"document":open("../pdf/bitcoin.pdf", 'rb')}

response = requests.post('https://api.telegram.org/bot7084726284:AAEQPkxGuJy8CclMOf79xHOzYWgiD_8uLy0/sendDocument?chat_id=-1002117509264', files=files)

print(type(response))

json_reponse = response.json()
print(f"{json_reponse} : {type(json_reponse)}")
#reponse_json = json.loads(response)
print("reponse", list(response))


# {
#     "subject_code1":
#     {
#         "file_id1":"filename", 
#         "fileid2":"filename", 
#         "file_id3":"filename"
#     },
#
#         
# }
