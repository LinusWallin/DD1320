def find_prime(n):
    """
    Function finds the nearest (larger than the sent number) primenumber and sends it back to make sure we avoid endless loops in our quad probing.
    :int: n: the size of the table sent.
    :return: n: the number now converted to a prime number to avoid endless looping.
    """
    size = n
    prime = False
    while not prime:
        prime = True
        for i in reversed(range(2, n // 2 + 1)):
            if n % i == 0:
                prime = False
                break
        if prime:
            print("Prime found: ", n, ", original size: ", size)
            return n
        else:
            n += 1


class HashNode:
    """
    A class for the nodes in the hash table.
    """

    def __init__(self, key="", data=None):
        """
        Define some standard attributes (kvp) for the node.
        :str: key: a string with the key to the node.
        :obj: data: an object containing the information about the stored value.
        """
        self.key = key
        self.data = data


class HashTable:
    """
    A class for creating a hash table of nodes.
    """

    def __init__(self, size):
        """
        Creates an empty list of size self.size
        :int: size: the size of the list of objects
        """
        self.size = size * 2
        self.size = find_prime(self.size)
        self.node_list = [None] * self.size

    def get(self, key):
        """
        Method checks if a key exists in the hash table by calling find_hash method with the given key. Checks and returns whether the key existed in the hash table or not.
        :str: key: a string with the key value to be searched in the hash table.
        :return: either the value (data) in the pair found to the key or raise a KeyError if no key was found.
        """
        if self.node_list[self.find_hash(key)] != None:
            return self.node_list[self.find_hash(key)].data
        else:
            raise KeyError

    def store(self, key, value=None):
        """
        Stores the node in the list on a hashed index.
        :str: key: a string with the key to the node
        :obj: value: the data to be stored with the key in the node
        """
        self.node_list[self.find_hash(key)] = HashNode(key, value)
        if self.size < len(self.node_list):
            self.size = len(self.node_list)

    def __contains__(self, key):
        """
        Magical method checks if a key exists in the hash table similarly to the "get" method. Only difference is that here False is returned if no key was found.
        :str: key: a string with the key value to be searched in the hash table.
        """
        if self.node_list[self.find_hash(key)] != None:
            return True
        else:
            return False

    def search(self, key):
        """
        Checks if the key exists in the hash HashTable.
        :str: key: a string with the key to the node
        :return: returns the data of the key if it exists, otherwise raises KeyError
        """
        get_key = self.get(key)
        if self.node_list[self.find_hash(key)].key == key:
            return get_key
        else:
            raise KeyError

    def find_hash(self, key):
        """
        Method hashes a key value. Here we expect the key to be a string, which we turn into a index hash value to store in the hash table. If the hash value that we created already exists in the hash table (the index is busy), we create a new hash value by using quad probing in "quad_probing_search" method.
        :str: key: a string with the key value to be searched in the hash table.
        :return: the index created to store the value (data) on.
        """
        index = 0
        for char in key:
            index = (index * 32 + ord(char))
        index = index % self.size

        if self.node_list[index] != None:
            if self.node_list[index].key != key:
                index = self.quad_probing_search(index, key)
        else:
            index = self.quad_probing_search(index, key)

        return index

    def quad_probing_search(self, index, key):
        """
        Method creates a new index for a key in the case of that the keys created hash value in method "find_hash" was already occupied. This is done by creating a quadtratical displacement from the original created index. This process is repeated until we find an empty index. If the index happens to be out of bounds, we use modulo to map in back around.
        :int: index: the current index.
        :str: key: a string with the key to the node.
        :return: the new hash value (new index value).
        """
        new_hash = index
        displacement = 1
        while self.node_list[new_hash] != None:
            if self.node_list[new_hash].key != key:
                new_hash = (new_hash + (displacement ** 2)) % self.size
                displacement += 1
                if displacement == self.size:
                    return False
            else:
                break
        return new_hash
