#LAB 8 Linus Walling & Arvid Gussarsson

from linkedQFile import LinkedQ
from string import ascii_lowercase, ascii_uppercase
import unittest

# Create a lowercase and uppercase alphabet string, adding "åäö" to convert it to the Swedish alphabet.
# Create a string with numbers 0-9.

alphabet_l = ascii_lowercase + 'åäö'
alphabet_u = ascii_uppercase + "ÅÄÖ"
numbers = '1234567890'


"""
<molekyl> ::= <atom> | <atom><num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ...
"""

class SyntaxError(Exception):
  """
  SyntaxError class that is called when an error occurs.
  Exception: the parent class.
  """
  def __init__(self, string):
    """
    :str: string: A string containing the error message.
    """
    self.string = string

  def __str__(self):
    return self.string

def print_q(q):
  """
  Funciton returns the remainder of what exists in the linked queue.
  :obj: q: the linked queue to be printed.
  :return: the string of the remainding user input.
  """
  string = ""
  while not q.isEmpty():
    string += str(q.dequeue())
  return string

def molecular(q):
  """
  Function is for the first step of the syntax hierarchy (make sure that we get an atom and then a number if the queue isn't empty).
  :obj: q: the linked queue containing the user input.
  """
  atom(q)
  if q.isEmpty() != True:
    number(q)
  
def atom(q):
  """
  Function checks that the atom entered by the user is of correct syntax <Upper> | <Upper> <Lower>
  :obj: q: the linked queue containing the user input.
  """
  next_item = q.peek()
  if next_item != None:
    if next_item not in numbers:
      letter_u(q)
      letter_l(q)
    else:
      letter_u(q)
  else:
    letter_u(q)

def letter_u(q):
  """
  Function checks if the dequeued character is uppercase by checking if it exists in the uppercase string. Otherwise raise an error.
  :obj: q: the linked queue containing the user input.
  :return: None, just return to the parent function.
  """
  item = q.dequeue()
  if item in alphabet_u:
    return
  else:
    raise SyntaxError("Saknad stor bokstav vid radslutet " + str(item) + print_q(q))

def letter_l(q):
  """
  Function checks if the dequeued character is lowercase by checking if it exists in the lowercase string. Otherwise raise an error.
  :obj: q: the linked queue containing the user input.
  :return: None, just return to the parent function.
  """
  item = q.dequeue()
  if item in alphabet_l:
    return
  else:
    raise SyntaxError("Saknad liten bokstav vid radslutet " + str(item) + print_q(q))

def number(q, iteration = 0):
  """
  Function checks if the dequeued character is a number by checking if it exists in the number string. Otherwise raise an error.
  :obj: q: the linked queue containing the user input.
  :int: iteration: the amount of times we have iterated through this function recursively in order to make sure that 0's and 1's are not accepted on certain spots in the input.
  :return: None, just return to the parent function.
  """
  next_nr = q.peek()
  nr = q.dequeue()
  if nr in numbers:
    if iteration == 0:
      if nr == "0":
        raise SyntaxError("För litet tal vid radslutet " + print_q(q))
      elif nr == "1" and next_nr == None:
        raise SyntaxError("För litet tal vid radslutet " + print_q(q))
  else:
    raise SyntaxError("För litet tal vid radslutet " + print_q(q))
  if next_nr != None:
    iteration += 1
    number(q, iteration)
  else:
    return

def check_syntax(q):
  """
  Checks if the syntax of the input entered by the user is correct.
  :obj: q: the linked queue containing the user input.
  :return: returns a string that tells the user if the syntax was correct or not, and if not it also contains the error.
  """
  try:
    molecular(q)
    return "Formeln är syntaktiskt korrekt"
  except SyntaxError as error:
    return str(error)

def fill_q(inp, linked_q):
  """
  Queues up all characters from the input.
  :str: inp: the user input
  :obj: linked_q: a linked queue that is used to store and read the user input
  :return: returns the linked queue
  """
  for i in range(len(inp)):
    if i < len(inp) - 1:
      linked_q.enqueue(inp[i], inp[i + 1])
    else:
      linked_q.enqueue(inp[i])
  return linked_q
  
def main():
  """
  Asks the user for input until an '#' is given and starts the test of its syntax.
  """
  inp = input()
  while inp != "#":
    print(input_to_q(inp))
    inp = input()

def input_to_q(inp):
  """
  Queues up the input and checks its SyntaxError
  :str: inp: the input in the form of a string
  :return: returns a string that tells the user if the syntax was correct or not, and if not it also contains the error.
  """
  linked_q = LinkedQ()
  q = fill_q(inp, linked_q)
  return (check_syntax(q))

main()


class SyntaxTest(unittest.TestCase):
  """
  Class is a unittest syntaxtest of two set inputs. These have set corresponding outputs which the system also should output.
  """
  def test_correct_syntax(self):
      self.assertEqual(input_to_q("Ab12"), "Formeln är syntaktiskt korrekt")

  def test_wrong_syntax(self):
      self.assertEqual(input_to_q("AB12"), "Saknad liten bokstav vid radslutet B12")

if __name__ == '__main__':
  unittest.main()