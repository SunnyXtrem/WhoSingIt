import requests
import re
import random

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
    print("Keine Tabelle gefunden")
    exit()

table_html = table_match.group(0)
rows = re.findall(r'<tr>(.*?)</tr>', table_html, re.DOTALL)

songs = []

for row in rows[1:16]:
    cells = re.findall(r'<t[dh].*?>(.*?)</t[dh]>', row, re.DOTALL)

    if len(cells) >= 3:
        artist = re.sub(r'<.*?>', '', cells[0]).strip()
        title = re.sub(r'<.*?>', '', cells[1]).strip()
        release_year = re.sub(r'<.*?>', '', cells[2]).strip()

        song = {
            "title": title,
            "artist": artist,
            "release_year": release_year
        }

        songs.append(song)

player_notes = [
    {"artist": "Bing Crosby",
     "hint1": "war von 1926 bis 1977 führend bei Plattenverkäufen, Einschaltquoten im Radio und Kinofilmen",
     "hint2": "Ein Charakter aus einem animierten Fantasy-Abenteuer, der oft mit Sarkasmus und einer Vorliebe für Chaos auffällt"},
    {"artist": "Elton John",
     "hint1": "Dieser Künstler ist bekannt für seine extravaganten Bühnenoutfits und brilliert seit Jahrzehnten als Sänger, Pianist und Songwriter",
     "hint2": "Dieser Musiker trägt oft eine Sonnenbrille und ist bekannt für seinen unverwechselbaren Stil, sowohl musikalisch als auch modisch. Außerdem wurde er in den Adelsstand erhoben."},
    {"artist": "Tino Rossi",
     "hint1": "Dieser Sänger war bekannt für seine weiche Stimme und gilt als einer der erfolgreichsten Chanson-Interpreten Frankreichs.",
     "hint2": "Er war ein französischer Sänger, dessen warme, gefühlvolle Stimme oft mit Weihnachten und besinnlichen Momenten verbunden wird. Außerdem trat er auch als Schauspieler in zahlreichen Filmen auf."},
    {"artist": "Bill Haley & His Comets",
     "hint1": "Diese Band wird oft als Pionier des Rock ’n’ Roll bezeichnet und war besonders in den 1950er-Jahren einflussreich.",
     "hint2": "Der Frontmann dieser Band trug eine markante Tolle, und ihre Musik brachte die Jugend weltweit zum Tanzen. Ihr Einfluss auf die Rock-Ära ist kaum zu überschätzen."},
    {"artist": "Whitney Houston",
     "hint1": "Diese Sängerin war nicht nur für ihre kraftvolle Stimme bekannt, sondern auch für ihre Erfolge als Schauspielerin und Model.",
     "hint2": "Sie gilt als eine der erfolgreichsten Pop- und R&B-Sängerinnen aller Zeiten und war bekannt für ihre außergewöhnliche stimmliche Reichweite. Sie sang auch die amerikanische Nationalhymne auf unvergleichliche Weise bei einem legendären Sportereignis."},
    {"artist": "Elvis Presley",
     "hint1": "Dieser Künstler war nicht nur ein Sänger, sondern auch ein Schauspieler und wurde zu einer kulturellen Ikone der 1950er-Jahre.",
     "hint2": "Er wird oft als ‚King of Rock ’n’ Roll‘ bezeichnet und ist bekannt für seine Hüftbewegungen, seine charakteristische Tolle und seinen Einfluss auf die moderne Musik."},
    {"artist": "The Ink Spots",
     "hint1": "Diese Gruppe prägte die Musikgeschichte mit ihrem einzigartigen Stil, der frühe Popmusik mit Elementen aus Jazz und Rhythm and Blues verband.",
     "hint2": "Sie waren eine einflussreiche Vokalgruppe der 1930er- und 1940er-Jahre, bekannt für ihren sanften Gesangsstil, oft begleitet von einem gesprochenen Bariton-Monolog in ihren Songs."},
    {"artist": "USA for Africa",
     "hint1": "Dieses Projekt vereinte einige der größten Musiker der 1980er-Jahre, um für einen guten Zweck zusammenzuarbeiten.",
     "hint2": "Die Gruppe bestand aus Stars wie Michael Jackson, Lionel Richie und anderen, die sich zusammengeschlossen haben, um gegen Hunger und Armut in Afrika zu kämpfen."},
    {"artist": "Celine Dion",
     "hint1": "Diese Künstlerin aus Kanada ist bekannt für ihre kraftvolle Stimme und hat eine Vielzahl von Musikgenres von Pop bis Klassik erfolgreich gesungen",
     "hint2": "Ihr weltberühmter Hit aus einem Film über das berühmte Schiffsunglück wurde zu einem ihrer größten Erfolge und machte sie international bekannt"},
    {"artist": "Mariah Carey",
     "hint1": "Diese Sängerin hat eine außergewöhnliche Stimmspanne und ist bekannt für ihre Fähigkeit, hohe Töne und beeindruckende Melismen zu singen.",
     "hint2": "Sie gilt als eine der erfolgreichsten Pop- und R&B-Künstlerinnen und ist bekannt für ihre extravaganten Bühnenauftritte sowie ihre Jahreszeit-übergreifende Popularität."},
    {"artist": "Baccara",
     "hint1": "Diese Duo wurde in den 1970er-Jahren berühmt und verband Popmusik mit Disco-Elementen, was ihre Musik zu einem internationalen Hit machte",
     "hint2": "Das Duo aus Spanien erzielte großen Erfolg mit einem weltbekannten Song, der oft als einer der größten Disco-Hits aller Zeiten angesehen wird."},
    {"artist": "Bryan Adams",
     "hint1": "Dieser Musiker ist bekannt für seinen Rock- und Pop-Stil und hat in den 1980er-Jahren einen großen Durchbruch als Sänger und Songwriter gefeiert",
     "hint2": "Er ist kanadischer Herkunft und seine Musik wurde durch zahlreiche Filme bekannt, besonders durch einen berühmten Soundtrack für einen großen Hollywood-Film."},
    {"artist": "John Travolta",
     "hint1": "Dieser Schauspieler ist bekannt für seine vielseitigen Rollen in verschiedenen Filmgenres, von Comedy bis Thriller, und wurde besonders in den 1970er-Jahren berühmt.",
     "hint2": "Er wurde zu einer Ikone der Disco-Ära und ist bekannt für seine Tanzbewegungen in einem weltbekannten Film, in dem er in einem weißen Anzug glänzte."},
    {"artist": "Olivia Newton-John",
     "hint1": "Diese Sängerin und Schauspielerin hatte Erfolg in verschiedenen Musikgenres, darunter Country, Pop und Soft Rock, und wurde für ihre Vielseitigkeit gefeiert.",
     "hint2": "Sie wurde besonders durch ihre Rolle in einem beliebten Film aus den 1970er-Jahren berühmt, in dem sie an der Seite von berühmten Schauspieler tanzte und sang."},
]

def get_random_song():
    song = random.choice(songs)
    artist = song["artist"]
    hint_data = next((entry for entry in player_notes if entry["artist"] == artist), None)
    if hint_data:
        song["hints"] = [hint_data["hint1"], hint_data["hint2"]]
    else:
        song["hints"] = ["Keine Hinweise verfügbar", "Keine Hinweise verfügbar"]
    return song
