import requests
import os
import time

access_token=os.environ["BOT_TOKEN"]
l = [
    [access_token, "910540882829271100"]
]

while True:
    for i in l:
        res = requests.post("https://discord.com/api/v8/channels/" + i[1] + "/messages", json={"content": "!d bump"}, headers={
                "Authorization": i[0] })
        print(res)

    time.sleep(7210)
