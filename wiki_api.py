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