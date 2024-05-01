import requests

files = {"document":open("./bitcoin.pdf", 'rb')}

response = requests.post('https://api.telegram.org/bot7084726284:AAEQPkxGuJy8CclMOf79xHOzYWgiD_8uLy0/sendDocument?chat_id=-1002117509264', files=files)

#reponse_json = json.loads(response)
print("reponse", list(response))
