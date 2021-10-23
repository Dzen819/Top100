from bs4 import BeautifulSoup


class Soup:
    def __init__(self, doc):
        self.doc = doc

    def get_soup(self):
        soup = BeautifulSoup(self.doc, "html.parser")

        songs_html = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

        songs = [song.getText() for song in songs_html]

        return songs
