from linkedQFile import LinkedQ
from string import ascii_lowercase, ascii_uppercase
from molgrafik import *
from hashtest import *

alphabet_l = ascii_lowercase + 'åäö'
alphabet_u = ascii_uppercase + "ÅÄÖ"
numbers = '1234567890'

class SyntaxError(Exception):
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string

atom_list = lagraHashtabell(skapaAtomlista())

def molecular_weight(tree):
  """
  Iterates through the tree and adds all values of the different atoms.
  :obj: tree: a tree, of type general tree, containing information of the formula
  """
  i = True
  weight = 0
  while i:
    if tree.down != None:
      weight += (molecular_weight(tree.down) * float(tree.num))
    if tree.atom != "()":
      weight += (atom_list.search(tree.atom) * float(tree.num))
    if tree.next == None:
      i = False
    else:
      tree = tree.next
  return weight


def print_q(q):
  """
  Funciton returns the remainder of what exists in the linked queue.
  :obj: q: the linked queue to be printed.
  :return: the string of the remainding user input.
  """
  string = " "
  while not q.isEmpty():
    string += str(q.dequeue())
  if string.isspace():
    return ""
  else:
    return string

def formula(q):
  """
  The root in the syntax tree. Where the syntax checking starts checking the formula (input).
  :obj: q: the linked list containing the input.
  """
  s.clear()
  tree = mol(q)
  if len(s) != 0:
    s.clear()
    raise SyntaxError("Saknad högerparentes vid radslutet" + print_q(q))
  return tree

s = []

def mol(q):
    """
    Function is responsible for going through the group stage of the syntax by recursively calling itself.
    :obj: q: the linked list containing the input.
    :return: the square linking to other squares in the general tree.
    """
    sq = group(q)
    if sq.atom == "()":
        if sq.num == 1:
          if q._first != None:
            p_val = 1
            next_val = q._first.next
            while next_val != None:
              if next_val.value == "(":
                p_val += 1
              elif next_val.value == ")":
                p_val -= 1
                if p_val == 0:
                  sq.num = next_val.next.value

                  break
              next_val = next_val.next
            sq.down = mol(q)
        else:
            return
    if not q.isEmpty():
        sq.next = mol(q)
    return sq

def group(q):
    """
    Function goes through the input (linked list) and keeps track of parantheses aswell.
    We make sure here that each group is of the correct syntax.
    :obj: q: the linked list containing the input.
    :return: sq: the square containing the information about the group.
    """
    sq = Ruta()
    if q._first.value == "(":
        if q.peek() == ")":
            q.dequeue()
            raise SyntaxError("Felaktig gruppstart vid radslutet" + print_q(q))
        else:
            val = q.dequeue()
            s.append(val)
            return sq
    elif q._first.value == ")":
        if len(s) != 0:
            s.pop()
            q.dequeue()
            if not q.isEmpty():
              sq.num = number(q)
              return sq
            else:
              raise SyntaxError("Saknad siffra vid radslutet" + print_q(q))
        else:
            raise SyntaxError("Felaktig gruppstart vid radslutet" + print_q(q))
    else:
        sq.atom = atom(q)
        if not q.isEmpty():
            if q._first.value in numbers:
                sq.num = number(q)
    return sq

def atom(q):
  """
  Function makes sure that the atom that is being examined by the program is in the correct format by following some set rules given by the syntax.
  :obj: q: the linked list containing the input.
  :return: either an uppercase char (a single char atom) or a double char atom.
  """
  next_item = q.peek()
  prev_item = letter_u(q)
  if next_item is not None:
    if next_item in alphabet_l:
      return letter_l(q, prev_item)
  if prev_item in atoms:
    return prev_item
  # Check if the atom is valid and if it is <LETTER> or <LETTER><letter>


def letter_u(q):
  """
  Function checks if the dequeued char is uppercase. If so, it returns the char. Otherwise it raises an error.
  :obj: q: the linked list.
  :return: the char if it is uppercase
  """
  item = q.dequeue()
  if item in alphabet_u:
    return item
  else:
    if item in numbers:
      raise SyntaxError("Felaktig gruppstart vid radslutet " + item + print_q(q)[1:])
    raise SyntaxError("Saknad stor bokstav vid radslutet " + item + print_q(q)[1:])


def letter_l(q, prev_item):
  """
  Function checks if the dequeued char is lowercase. If so, it returns the char. Otherwise it raises an error. Here it needs to combine the prev_item and check if it exists in atoms since a single atom cant be lowercase.
  :obj: q: the linked list.
  :str: prev_item: the previous character (should be uppercase).
  :return: the char if it is lowercase
  """
  item = q.dequeue()
  if (prev_item + item) in atoms:
    return (prev_item + item)
  else:
    raise SyntaxError("Okänd atom vid radslutet" + print_q(q))


def number(q, iteration=0):
  """
  Function checks if the dequeued character is a number. It also needs to make sure that the whole number is dequeued, so we have to peek the next number before we return the completed number (cnr).
  :obj: q: the linked list containing the input.
  """
  cnr = ""
  iteration = 0
  next_item = q.peek()
  item = q.dequeue()
  while item in numbers:
    cnr += item
    if iteration == 0:
      if item == "0":
        raise SyntaxError("För litet tal vid radslutet" + print_q(q))
      elif item == "1":
        if next_item is not None:
          if next_item not in numbers:
            raise SyntaxError("För litet tal vid radslutet" + print_q(q))

    if next_item is not None:
      if next_item in numbers:
        next_item = q.peek()
        item = q.dequeue()
        iteration += 1
      else:
        break
    else:
      break

  else:
    raise SyntaxError("Saknad siffra vid radslutet " + item + print_q(q)[1:])
  return cnr

def check_syntax(q):
  """
  Function tries the input with the syntax checker. If it works, we get a success message, otherwise an error with a message containing what went wrong.
  :obj: q: the linked list containing the input.
  :return: the result of the checker.
  """
  try:
    tree = formula(q)
    print(molecular_weight(tree))
    mg = Molgrafik()
    mg.show(tree)
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

atoms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']

def main():
  """
  Asks the user for input until an '#' is given and starts the test of its syntax.
  """
  inp = input()
  while inp != "#":
    if not inp.isspace() and inp != "":
      print(input_to_q(inp))
      inp = input()
    else:
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

if __name__ == "__main__":
  main()



import unittest


class SyntaxTest(unittest.TestCase):

  def test_correct_syntax(self):
    self.assertEqual(input_to_q("O"), "Formeln är syntaktiskt korrekt")
    self.assertEqual(input_to_q("CO2"), "Formeln är syntaktiskt korrekt")
    self.assertEqual(input_to_q("(CH3)2(CH2)4"), "Formeln är syntaktiskt korrekt")
    self.assertEqual(input_to_q("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")
    self.assertEqual(input_to_q("Na332"), "Formeln är syntaktiskt korrekt")
    self.assertEqual(input_to_q("Na(Cl)2"), "Formeln är syntaktiskt korrekt")
    self.assertEqual(input_to_q("Si(H2O)3"), "Formeln är syntaktiskt korrekt")



  def test_wrong_syntax(self):
    self.assertEqual(input_to_q("C(Xx4)5"), "Okänd atom vid radslutet 4)5")
    self.assertEqual(input_to_q("C(OH4)C"), "Saknad siffra vid radslutet C")
    self.assertEqual(input_to_q("C(OH4C"), "Saknad högerparentes vid radslutet")
    self.assertEqual(input_to_q("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe")
    self.assertEqual(input_to_q("H0"), "För litet tal vid radslutet")
    self.assertEqual(input_to_q("H1C"), "För litet tal vid radslutet C")
    self.assertEqual(input_to_q("H02C"), "För litet tal vid radslutet 2C")
    self.assertEqual(input_to_q("Nacl"), "Saknad stor bokstav vid radslutet cl")
    self.assertEqual(input_to_q("a"), "Saknad stor bokstav vid radslutet a")
    self.assertEqual(input_to_q("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3")
    self.assertEqual(input_to_q(")"), "Felaktig gruppstart vid radslutet )")
    self.assertEqual(input_to_q("2"), "Felaktig gruppstart vid radslutet 2")

if __name__ == '__main__':
  unittest.main()