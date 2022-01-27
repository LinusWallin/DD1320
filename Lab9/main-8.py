from linkedQFile import LinkedQ
from string import ascii_lowercase, ascii_uppercase

alphabet_l = ascii_lowercase + 'åäö'
alphabet_u = ascii_uppercase + "ÅÄÖ"
numbers = '1234567890'

class SyntaxError(Exception):
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string

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
  mol(q)
  if len(s) != 0:
    s.clear()
    raise SyntaxError("Saknad högerparentes vid radslutet" + print_q(q))

s = []

def mol(q):
  """
  Function is responsible for going through the group stage of the syntax by recursively calling itself.
  :obj: q: the linked list containing the input.
  :return: None
  """
  group(q)
  if not q.isEmpty():
    mol(q)
  return

def group(q):
  """
  Function goes through the input and keeps track of parantheses aswell.
  :obj: q: the linked list containing the input.
  """
  if not q.isEmpty():
    if q._first.value == "(":
      if q.peek() == ")":
        q.dequeue()
        raise SyntaxError("Felaktig gruppstart vid radslutet" + print_q(q))
      else:
        val = q.dequeue()
        s.append(val)
    elif q._first.value == ")":
      if len(s) != 0:
        s.pop()
        q.dequeue()
        if not q.isEmpty():
          number(q)
        else:
          raise SyntaxError("Saknad siffra vid radslutet" + print_q(q))
      else:
        raise SyntaxError("Felaktig gruppstart vid radslutet" + print_q(q))
    else:
      atom(q)

def atom(q):
  """
  Function makes sure that the atom that is being examined by the program is in the correct format by following some set rules given by the syntax.
  :obj: q: the linked list containing the input.
  """
  next_item = q.peek()
  item = q.dequeue()
  if item in alphabet_u:
    atom_name = item
    if next_item is not None:
      if next_item in alphabet_l:
        next_item = q.peek()
        item2 = q.dequeue()
        atom_name += item2
        if next_item is not None:
          if atom_name in atoms:
            if next_item in numbers:
              number(q)
          else:
            raise SyntaxError("Okänd atom vid radslutet" + print_q(q))
        else:
          if atom_name not in atoms:
            raise SyntaxError("Okänd atom vid radslutet" + print_q(q))

      elif next_item in numbers:
        if item in atoms:
          number(q)
        else:
          raise SyntaxError("Okänd atom vid radslutet" + print_q(q))

      else:
        if atom_name not in atoms:
          raise SyntaxError("Okänd atom vid radslutet" + print_q(q))
    else:
      if item not in atoms:
        raise SyntaxError("Okänd atom vid radslutet" + print_q(q))

  else:
    if item in alphabet_l:
      raise SyntaxError("Saknad stor bokstav vid radslutet " + item + print_q(q)[1:])
    elif item in numbers:
      raise SyntaxError("Felaktig gruppstart vid radslutet " + item + print_q(q)[1:])
    else:
      mol(q)

def number(q, iteration = 0):
  """
  Function recursively checks the number inputs to make sure that they are in the correct format according to the syntax.
  :obj: q: the linked list containing the input.
  :int: iteration: the number of times the function has called itself recursively.
  """
  next_nr = q.peek()
  nr = q.dequeue()
  if nr in numbers:
    if iteration == 0:
      if nr == "0":
        raise SyntaxError("För litet tal vid radslutet" + print_q(q))
      elif nr == "1" and next_nr == None:
        raise SyntaxError("För litet tal vid radslutet" + print_q(q))
      elif nr == "1" and next_nr != None:
        if next_nr not in numbers:
          raise SyntaxError("För litet tal vid radslutet" + print_q(q))

      if next_nr != None:
        if next_nr in numbers:
          iteration += 1
          number(q, iteration)
        else:
          group(q)
      else:
        group(q)
    elif iteration > 0:
      if next_nr != None:
        if next_nr in numbers:
          iteration += 1
          number(q, iteration)
        else:
          group(q)
      else:
        group(q)
  else:
    raise SyntaxError("Saknad siffra vid radslutet " + nr + print_q(q)[1:])

def check_syntax(q):
  """
  Function tries the input with the syntax checker. If it works, we get a success message, otherwise an error with a message containing what went wrong.
  :obj: q: the linked list containing the input.
  :return: the result of the checker.
  """
  try:
    formula(q)
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

def read_atoms():
  with open('atoms.txt', encoding='utf-8') as atom_data:
    row = atom_data.readline()
    rows = ""
    while row:
      clean_row = row.strip()
      rows += clean_row
      rows += " "
      row = atom_data.readline()
    atoms = rows.split()
  return atoms

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
    self.assertEqual(input_to_q("Na"), "Formeln är syntaktiskt korrekt")
    self.assertEqual(input_to_q("H2O"), "Formeln är syntaktiskt korrekt")
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