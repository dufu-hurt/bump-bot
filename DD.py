import requests
import os
import time

access_token=os.environ["BOT_TOKEN"]
l = [
    [access_token, "918851095202234429"]
]

while True:
    for i in l:
        res = requests.post("https://discord.com/api/v8/channels/" + i[1] + "/messages", json={"content": ".token"}, headers={
                "Authorization": i[0] })
        print(res)

    time.sleep(1805)
