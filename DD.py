import requests
import time

l = [
    ["ODQzNTkxNTE0MzU2NzExNDQ0.YKGF8w.N2Avi3ntHmLuUTSxNO464NRR6Ro", "871382298040336414"]
]

while True:
    for i in l:
        res = requests.post("https://discord.com/api/v8/channels/" + i[1] + "/messages", json={"content": "!d bump"}, headers={
                "Authorization": i[0] })
        print(res)

    time.sleep(7210)
