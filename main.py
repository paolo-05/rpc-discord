import json
from pypresence import Presence
import time

data = json.load(open("config.json"))


def main():
    rpc = Presence(data["CLIENT_ID"])
    rpc.connect()
    rpc.update(state="A very cool discord bot", details="(A lot of commands)", large_image="logo", buttons=[
               {"label": "Website", "url": "https://xgnbot.xyz"},
               {"label": "invite", "url": "https://discord.com/oauth2/authorize?client_id=840300480382894080&permissions=8&scope=bot%20applications.commands"}]
               )


print("loop created")
while True:
    time.sleep(15)
    main()
