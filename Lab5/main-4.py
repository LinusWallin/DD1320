#LAB 5, Linus Wallin & Arvid Gussarsson.

def utskrift(lista):
    if len(lista) > 0:
      utskrift(lista[1:])
      print(lista[0])

utskrift([1,2,3,4,5])


# Import some classes

from string import ascii_lowercase
from linkedQFile import LinkedQ, Node, ParentNode
from bintreeFile import Bintree

class SolutionFound(Exception):
  """
  Class that is called if an end word is found from a path.
  """
  pass

# Create a lowercase alphabet string, adding "åäö" to convert it to the Swedish alphabet.

alphabet = ascii_lowercase + 'åäö'


def makechildren(node, q):
  """
  Function searches for children to the start word by iterating through the word and the alphabet. Every new char iteration is checked to make sure that the new created word exists in the "swedish" bintree obj. Then, it is added to a new bintree object "old" which makes sure there are no doules. The children are then assigned as parent nodes to the queue 'q'.
  :obj: node: the current node in the linked list.
  :obj: q: the linked queue object.
  """
  amt_children = 0
  node_list = list(node.word)
  for i in range(0, len(node_list)):
    new_word = node_list.copy()
    for char in alphabet:
      if char != node_list[i]:
        new_word[i] = char
        str1 = ""
        new_word_str = str1.join(new_word)
        if new_word_str in swedish:
          if new_word_str not in old:
            amt_children += 1
            old.put(new_word_str)
            q.enqueue(ParentNode(new_word_str, node))


def writechain(end_node):
  """
  Function prints the path result if a the end word was found.
  :obj: end_node: the current node of the linked list that the function iterates through.
  """
  if end_node != None:
    writechain(end_node.parent)
    print(end_node.word)

# Create a new Bintree object.
swedish = Bintree()
old = Bintree()
# Open a file and put all the words from the file into a list of words.
with open("word3.txt", "r", encoding = "utf-8") as swe_file:
  # Loop through the list of words and print the words that occur multiple times.
    for row in swe_file:
        word = row.strip()
        if word in swedish:
            print(word, end = " ") 
        else:
            swedish.put(word)             # insert into the search tree
print("\n")

# Ask the user for some input: a start word and an end word which to perform the search on.

start_word = input("Enter startword: ")

old = Bintree()

end_word = input("Enter endword: ")

def find_word(start_word, end_word):
  """
  Function finds a possible path from the start_word to the end_word by using the makechildren function. In this function the linked queue is utilized aswell, by queueing each node and then dequeueing it to iterate through different nodes in order to get the end word (if there is one).
  :str: start_word: the word to start the search for.
  :str: end_word: the word to search for.
  :return: a statement telling the user whether or not the word could be transformed or not.
  """
  q = LinkedQ()
  q.enqueue(ParentNode(start_word))
  while not q.isEmpty():
    node = q.dequeue()
    if node.word == end_word:
      writechain(node)
      raise SolutionFound
    else:
      makechildren(node, q)
  else:
    return "End word: not found. \n"

# Print the results from the find_word function.

print(find_word(start_word, end_word))