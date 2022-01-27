# Arvid Gussarsson & Linus Wallin. CMETE2. LAB2

#Import classes

from array import array
from arrayQFile import ArrayQ
from linkedQFile import Node, LinkedQ
import unittest

# 1

# Create a new array and asign some values to it. Test some methods.

newArr = array("i", [1, 2, 3, 4])

print(newArr)
print(newArr.pop(-1))
newArr.append(5)
newArr.insert(0, 9)
newArr.remove(2)

print(newArr)


# 2

# Testing the array queue by enqueueing and dequeueing integers

q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = int(q.dequeue())
y = int(q.dequeue())
print(x, y)
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")


# 3


def magic(inp):
  """
  Performs a magic trick.
  :list: inp: a list of characters for the program to perform the magic trick on.
  :return: the modified string.
  """
  temp_str = ""
  for i in range(0, len(inp)):
    inp.append(inp[i])
    inp.pop(i)
    temp_str += inp[i] + " "
  return temp_str[:-1]

# Ask the user for numbers that the program will perform a magic trick on. Print the results.
user_inp = input()
inp_list = user_inp.split()
print(magic(inp_list))

# 3 Alternative

def magic_arr(user_inp):
  """
  Performs a magic trick. Using an array to queue and dequeue the characters.
  The dequeued characters are then stored in an string.
  :list: user_inp: a list of characters for the program to perform the magic trick on.
  :return: the modified string.
  
  """

  for i in range(len(user_inp)):
    if user_inp[i] == "Kn" or user_inp[i] == "KN":
      user_inp[i] = "x"
  
  card_arr = ArrayQ(user_inp)
  card_list = []
  card_string = ""
  while not card_arr.isEmpty():
    card_arr.enqueue(card_arr.dequeue())
    card_list.append(card_arr.dequeue())
  for elmt in card_list:
    if elmt == "x":
      elmt = "Kn"
    card_string += elmt + " "
  return card_string[:-1]

user_inp = input()
inp_list = user_inp.split()
print(magic_arr(inp_list))

# 4 TOP OF DOC

# 5

class TestQueue(unittest.TestCase):
  
    def test_isEmpty(self):
        #isEmpty shall return True if the queue is empty, otherwise False
        q = LinkedQ()
        self.assertTrue(q.isEmpty(), "isEmpty på tom kö")
        q.enqueue(17)
        self.assertFalse(q.isEmpty(), "isEmpty på icke-tom kö")

    def test_order(self):
        #Checks that the queue order is correct
        q = LinkedQ()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)

# 7

def magic_arr_linq(inp_list):
  """
  Performs the same magic trick as previous functions, but uses linked lists instead of regular lists.
  :list: inp: a list of characters for the program to perform the magic trick on.
  :return: the modified string.
  """
  card_arr = LinkedQ()
  card_string = ""
  for num in inp_list:
    card_arr.enqueue(num)
  card_list = []
  while not card_arr.isEmpty():
    card_arr.enqueue(card_arr.dequeue())
    card_list.append(card_arr.dequeue())
  for i in range(len(card_list)):
    card_string += card_list[i] + " "
  return (card_string[:-1])

# Ask the user for numbers that the program will perform a magic trick on. Make sure that the input entered is of type <int>. Print the results.
user_inp = input()
inp_list = user_inp.split()
print(magic_arr_linq(inp_list))

if __name__ == "__main__":
    unittest.main()
