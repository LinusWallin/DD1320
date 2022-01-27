#LAB 3 Linus Wallin & Arvid Gussarsson. CMETE2.

# Import class Bintree from another file.
from bintreeFile import Bintree

def makeTree():
  """
  Function creates a Bintree object and expects user input to be added to the binary search tree.
  :return: the created binary tree.
  """
  tree = Bintree()
  data = input().strip()
  while data != "#":
      tree.put(data)
      data = input().strip()
  return tree

def searches(tree):
  """
  Function controls that the binary search tree created from makeTree has been created properly and that the search method "in" works for the binary search tree. Prints the results.
  :obj: tree: the binary search tree to be searched.
  """
  findme = input().strip()
  while findme != "#":
      if findme in tree:
          print(findme, "found")
      else:
          print(findme, "not found")
      findme = input().strip()

def main():
  """
  Main function runs other functions in the program.
  """
  tree = makeTree()
  searches(tree)

main()

# Create a new Bintree object.
swedish = Bintree()
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

# Create a new Bintree object.
english = Bintree()
# Open a file and put all the words from the file into a list of words.
with open("engelska.txt", "r", encoding = "utf-8") as eng_file:
    for row in eng_file:
        word_list = row.strip().split()
        # Loop through the list of words and print the words that exist both in the list of swedish words and the list of english words.
        for word in word_list:
          if word not in english:
            english.put(word)
            if word in swedish:
              print(word, end = " ")        # insert into the search tree
print("\n")
