#LAB 4, Linus Wallin & Arvid Gussarsson.

# Import some classes

from string import ascii_lowercase
from linkedQFile import LinkedQ, Node
from bintreeFile import Bintree

# Create a lowercase alphabet string, adding "åäö" to convert it to the Swedish alphabet.

alphabet = ascii_lowercase + 'åäö'

def makechildren_1(start_word):
  """
  Function searches for children to the start word by iterating through the word and the alphabet. Every new char iteration is checked to make sure that the new created word exists in the "swedish" bintree obj. Then, it is added to a new bintree object "old" which makes sure there are no doules. The result (words that are children, ie can be created from the start word) is then printed.
  :str: start_word: the word to begin searching from
  """
  amt_children = 0
  start_word = list(start_word)
  for i in range(0, len(start_word)):
    new_word = start_word.copy()
    for char in alphabet:
      if char != start_word[i]:
        new_word[i] = char
        str1 = ""
        new_word_str = str1.join(new_word)
        if new_word_str in swedish:
          if new_word_str not in old:
            amt_children += 1
            old.put(new_word_str)
            print(str(amt_children), new_word_str)


def makechildren(node, q):
  """
  Function searches for children to the start word by iterating through the word and the alphabet. Every new char iteration is checked to make sure that the new created word exists in the "swedish" bintree obj. Then, it is added to a new bintree object "old" which makes sure there are no doules. The children are then assigned to the 
  queue 'q'.
  :str: node: the value of the current node that is iterated in the linked list.
  :obj: q: the linked queue object.
  """
  amt_children = 0
  node = list(node)
  for i in range(0, len(node)):
    new_word = node.copy()
    for char in alphabet:
      if char != node[i]:
        new_word[i] = char
        str1 = ""
        new_word_str = str1.join(new_word)
        if new_word_str in swedish:
          if new_word_str not in old:
            amt_children += 1
            old.put(new_word_str)
            q.enqueue(new_word_str)

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

makechildren_1(start_word)

old = Bintree()

end_word = input("Enter endword: ")

def find_word(start_word, end_word):
  """
  Function finds a possible path from the start_word to the end_word by using the makechildren function. In this function the linked queue is utilized aswell, by queueing each word and then dequeueing it to iterate through different words in order to get the end word (if there is one).
  :str: start_word: the word to start the search for.
  :str: end_word: the word to search for.
  :return: a statement telling the user whether or not the word could be transformed or not.
  """
  q = LinkedQ()
  q.enqueue(start_word)
  while not q.isEmpty():
    node = q.dequeue()
    print(node)
    if node == end_word:
      return "End word: " + end_word + " found. \n"
    else:
      makechildren(node, q)
  else:
    return "End word: not found. \n"

# Print the results from the find_word function.

print(find_word(start_word, end_word))