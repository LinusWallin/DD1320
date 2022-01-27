
class Song:
    """
    Class is to save each song as an object
    """
    def __init__(self, trackid, time, artist, title):
        """

        :param trackid: a string
        :param time: a string
        :param artist: a string
        :param title: a string
        """
        self.trackid = trackid
        self.time = time
        self.artist = artist
        self.title = title

    def __lt__(self, other):
        """
        Magical method lt checks if an element is less than another object based on the artist attribute
        :param other: another object
        :return: a boolean
        """
        if self.artist < other.artist:
            return True
        else:
            return False