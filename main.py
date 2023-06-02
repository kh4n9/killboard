import requests as re

link = "https://gameinfo.albiononline.com/api/gameinfo/events?limit=51&offset=0"

rp = re.get(link)

list = rp.text.split(',')

print(list[0])