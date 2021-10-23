from soup import Soup
import requests
from spoti import Spoti

date = input("Type the date in this format YYYY-MM-DD: ")

html_link = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(html_link)
doc = response.text

soup = Soup(doc)
songs = soup.get_soup()

spotify = Spoti(songs, date)

spotify.search_sp()
spotify.add_tracks()


