import requests
import os

page_id = os.environ.get("PAGE_ID")

access_token = os.environ.get("ACCESS_TOKEN")

response=requests.get("https://zenquotes.io/api/random")
data=response.json()[0]
quote=data["q"]
author=data["a"]

message = f"{quote}.\n\n--{author}"

if response.status_code== 200:
    print("success")
else:
    response.text



url = f"https://graph.facebook.com/v19.0/{page_id}/feed"

payload = {
    "message": message,
    "access_token": access_token
}

res = requests.post(url, data=payload)


if res.status_code==200:
    print("This has been posted")
else:
    print(res.text)
