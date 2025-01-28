import wikipedia  # Bibliothek für Wikipedia-Suche und Summary

# Sprache für Wikipedia-Suche setzen
wikipedia.set_lang("de")

# Komplette Songliste mit Titel, Interpret und Veröffentlichungsjahr selbst erstellt
song_liste = [
    {"title": "Sweet Child o’ Mine", "artist": "Guns N’ Roses", "release_year": "1987"},
    {"title": "Imagine", "artist": "John Lennon", "release_year": "1971"},
    {"title": "Bohemian Rhapsody", "artist": "Queen", "release_year": "1975"},
    {"title": "Hotel California", "artist": "Eagles", "release_year": "1976"},
    {"title": "Like a Rolling Stone", "artist": "Bob Dylan", "release_year": "1965"},
    {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "release_year": "1991"},
    {"title": "Billie Jean", "artist": "Michael Jackson", "release_year": "1982"},
    {"title": "Hey Jude", "artist": "The Beatles", "release_year": "1968"},
    {"title": "Uptown Funk", "artist": "Mark Ronson feat. Bruno Mars", "release_year": "2014"},
    {"title": "Rolling in the Deep", "artist": "Adele", "release_year": "2010"},
    {"title": "Wonderwall", "artist": "Oasis", "release_year": "1995"},
    {"title": "Lose Yourself", "artist": "Eminem", "release_year": "2002"},
    {"title": "I Will Always Love You", "artist": "Whitney Houston", "release_year": "1992"},
    {"title": "Take On Me", "artist": "a-ha", "release_year": "1985"},
    {"title": "Shape of You", "artist": "Ed Sheeran", "release_year": "2017"},
    {"title": "Thriller", "artist": "Michael Jackson", "release_year": "1982"},
    {"title": "Rolling in the Deep", "artist": "Adele", "release_year": "2010"},
    {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "release_year": "1971"},
    {"title": "Hotel California", "artist": "Eagles", "release_year": "1976"}
]

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

# Funktion: Lade Wikipedia-Daten für einen Song
def lade_songdaten(song):
    print(f"\n🔍 Lade Wikipedia-Daten für: {song['title']}")

    # Suche nach der Wikipedia-Seite
    try:
        # Versuch, die Seite mit "(Lied)" zu finden
        seite = wikipedia.page(f"{song['title']} (Lied)", auto_suggest=False)
    except wikipedia.PageError:
        try:
            # Falls das nicht klappt, suche nur mit dem Titel
            seite = wikipedia.page(song["title"], auto_suggest=False)
        except wikipedia.PageError:
            song["wikipedia_link"] = "Nicht gefunden"
            song["hinweis"] = "Kein Hinweis verfügbar."
            return song

    # Füge den Link und den ersten Absatz hinzu
    song["wikipedia_link"] = seite.url
    try:
        # Abruf des ersten Absatzes und der ersten 2 Zeilen
        song["hinweis"] = wikipedia.summary(seite.title, sentences=2)
    except wikipedia.exceptions.PageError:
        song["hinweis"] = "Kein Hinweis verfügbar."
    except wikipedia.exceptions.DisambiguationError:
        song["hinweis"] = "Mehrdeutige Ergebnisse gefunden."

    return song

# Lade Wikipedia-Daten für alle Songs und erstelle eine neue Liste
erweiterte_song_liste = [lade_songdaten(song) for song in song_liste]

# Ausgabe der neuen Songliste mit Hinweisen
print("\n--- Songliste mit Hinweisen ---\n")
for song in erweiterte_song_liste:
    print(f"Titel: {song['title']}")
    print(f"Interpret: {song['artist']}")
    print(f"Veröffentlichung: {song['release_year']}")
    print(f"Wikipedia-Link: {song['wikipedia_link']}")
    print(f"Hinweis: {song['hinweis']}")
    print("-" * 50)