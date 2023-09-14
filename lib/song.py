class Song:

    count = 0
    all = []
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count([self.genre])
        self.add_to_artist_count([self.artist])

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genres):
        for genre in genres:
            if genre in cls.genre_count:
                cls.genre_count[genre] += 1
            else:
                cls.genre_count[genre] = 1     

    @classmethod
    def add_to_artist_count(cls, artists):
        for artist in artists:
            if artist in cls.artist_count:
                cls.artist_count[artist] += 1

            else:
                cls.artist_count[artist] = 1
        



     
