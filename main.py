# https://www.youtube.com/watch?v=I87CoNJsOxo
import requests
from bs4 import BeautifulSoup


from datetime import datetime, timedelta
unix_ts = 1627763400000 / 1000.00


dt = (datetime.fromtimestamp(unix_ts) - timedelta(hours=2)).strftime('%Y-%m-%d %H:%M:%S')
print(dt)
url = 'https://www.youtube.com/watch?v=I87CoNJsOxo'
# webbrowser.open(url, new=0, autoraise=True)


URL = "https://overwatchleague.com/en-us/schedule?stage=regular_season&week=16"
page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")

print(page)