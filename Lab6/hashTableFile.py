
class HashTable:
    """
    Class is for creating hash tables.
    """
    def __init__(self, data):
        """

        :param data: a list of objects
        """
        self.hash_dict = {}
        self.data = data
        # self.max = 1000000
        for j in range(len(self.data)):
            self.put(self.data[j].artist, j)

    def get(self, key):
        """

        :param key: a string
        :return: returns the dictionary on an index of a hash value of a key
        """
        return self.hash_dict[hash(key)]

    def put(self, key, data):
        """
        Method adds new key-value-pairs to the hash table dictionary using hashed keys
        :param key: a string
        :param data: a list of objects
        :return: null
        """
        self.hash_dict[hash(key)] = data

    def __contains__(self, key):
        """
        Magical method checks if a key exists in the hash table dictionary
        :param key: a string
        :return: a boolean
        """
        if self.get(key) != None:
            return True
        else:
            return False