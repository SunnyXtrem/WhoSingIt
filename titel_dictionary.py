import requests
import re

WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"

params = {
    "action": "parse",
    "page": "List of best-selling singles",
    "format": "json",
    "prop": "text"
}

response = requests.get(WIKIPEDIA_API_URL, params=params)
data = response.json()

html_content = data['parse']['text']['*']

table_match = re.search(r'<table class="wikitable.*?</table>', html_content, re.DOTALL)
if not table_match:
    print("No table found")
    exit()

table_html = table_match.group(0)

rows = re.findall(r'<tr>(.*?)</tr>', table_html, re.DOTALL)

songs = []

for row in rows[1:16]:
    cells = re.findall(r'<t[dh].*?>(.*?)</t[dh]>', row, re.DOTALL)
    if len(cells) >= 5:
        artist = re.sub(r'<.*?>', '', cells[0]).strip()
        title = re.sub(r'<.*?>', '', cells[1]).strip()
        release_year = re.sub(r'<.*?>', '', cells[2]).strip()


        # Create a dictionary for the song
        song = {
            "titel": title,
            "released": release_year,
            "Musiker": artist
        }
        songs.append(song)

# Output the dictionary
for song in songs:
    print(song)
