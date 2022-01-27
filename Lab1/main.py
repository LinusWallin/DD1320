#Linus Wallin & Arvid Gussarsson. CMETE2. LAB 1

#Create the list that will hold all the pokemons from the file.
pokemon = []

class Pokemon:
  def __init__(self, name, type1, type2, total, hp, attack, defense , sp_atk, sp_def, speed, generation, legendary):
    """
    Assigns values to all attributes.
    :str: name: the name of the Pokemon
    :str: type1: the first type of the Pokemon
    :str: type2: the second type of the Pokemon
    :str: total: the total amount of points for the Pokemon
    :str: hp: the amount of hitpoints for the Pokemon
    :str: attack: the amount of attack points for the Pokemon
    :str: defense: the amount of defense points for the Pokemon
    :str: sp_atk: the amount of special attack points for the Pokemon
    :str: sp_def: the amount of special defense points for the Pokemon
    :str: speed: the swiftness of the Pokemon
    :str: generation: which generation the Pokemon is from
    :str: legendary: whether or not the Pokemon is of legendary status
    """
    self.name = name
    self.type1 = type1
    self.type2 = type2
    self.total = total
    self.hp = hp
    self.attack = attack
    self.defense = defense
    self.sp_atk = sp_atk
    self.sp_def = sp_def
    self.speed = speed
    self.generation = generation
    self.legendary = legendary
  

  def __lt__(self, p2):
    """
    Compares the hp between two Pokemon. Checks if the second sent Pokemon has less HP
    than the first sent Pokemon in the comparison statement.
    :obj: p2: An object of type Pokemon
    :return: A string stating whether or not the comparison was true or not.
    """
    pok1 = self.hp
    pok2 = p2.hp
    if pok2 < pok1:
      return p2.name + " has less hp than " + self.name + ".\n"
    else:
      return p2.name + " does not have less hp than " + self.name + ".\n"
    
  def __gt__(self, p2):
    """
    Compares the hp between two Pokemon. Checks if the second sent Pokemon has more HP
    than the first sent Pokemon in the comparison statement.
    :obj: p2: An object of type Pokemon
    :return: A string stating whether or not the comparison was true or not.
    """
    pok1 = self.hp
    pok2 = p2.hp
    if pok2 > pok1:
      return p2.name + " has more hp than " + self.name + ".\n"
    else:
      return p2.name + " does not have more hp than " + self.name + ".\n"

  def __eq__(self, p2):
    """
    Compares the hp between two Pokemon. Checks if the second sent Pokemon has an equal amount of HP as the first sent Pokemon in the comparison statement.
    :obj: p2: An object of type Pokemon
    :return: A string stating whether or not the comparison was true or not.
    """
    pok1 = self.hp
    pok2 = p2.hp
    if pok1 == pok2:
      return p2.name + " has the same amount of hp as " + self.name + ".\n"
    else:
      return p2.name + " does not have the same amount of hp as " + self.name + ".\n"

  def __str__(self):
    """
    Prints all information about the Pokemon.
    :return: A string consisting of all the attributes of the Pokemon.
    """
    return "Name: " + self.name + "\n" + "Type: " + self.type1 + "\n" + "and " + self.type2 + "\n" + "Total: " + self.total + "\n" + "HP: " + self.hp + "\n" + "Attack: " + self.attack + "\n" + "Defense: " + self.defense + "\n" + "Special Attack: " + self.sp_atk + "\n" + "Special Defense: " + self.sp_def + "\n" + "Speed: " + self.speed + "\n" + "Generation: " + self.generation + "\n" + "Legendary: " + self.legendary + "\n"

  def add_hp(self, hp):
    """
    Adds HP to a Pokemon.
    :int: hp: The amount of HP to be added to the existing HP of the Pokemon.
    :return: A string stating that the HP adjustment was successful, with the new HP for the Pokemon.
    """
    prev_hp = int(self.hp)
    self.hp = str(hp + prev_hp)
    return "HP adjusted. New hp for " + self.name + ": " + self.hp
    


def read_poklist():
  """
  Reads the Pokemon data into the program.
  :return: A list with all the data from the file stored as objects of type Pokemon.
  """
  with open('pokemon.csv', encoding='utf-8') as pokedata:
    row = pokedata.readline()
    row = pokedata.readline()
    pokemon = []
    while row:
      clean_row = row.strip()
      mod_row = clean_row.split(',')
      pokemon.append(Pokemon(mod_row[1], mod_row[2], mod_row[3], mod_row[4], mod_row[5], mod_row[6], mod_row[7], mod_row[8], mod_row[9], mod_row[10], mod_row[11], mod_row[12]))
      row = pokedata.readline()
    return pokemon
  
# Call the function that reads the data.
pokemon = read_poklist()


def test_pokemon():
  """
  Test that the class works by creating an object.
  """
  pokemon.append(Pokemon("Mew", "Ghost", "Psychic", "1000", "100", "100", "100", "100", "100", "100", "100", "True"))

# Call the testing function.
test_pokemon()

# Print the results from the testing function.
print(pokemon[-1])

# Test the less than, greater than and equals methods in the Pokemon class. Print the results.
print(pokemon[0] < pokemon[1])
print(pokemon[0] > pokemon[1])
print(pokemon[0] == pokemon[1])


def find_pok():
  """
  Asks the user for a Pokemon name and checks if that Pokemon exists in the Pokemon list.
  :return: The pokemon object and the index in the list where it was found or exit the program if the user enters 'exit'.
  """
  input_pok = "0"
  while True:
    input_pok = input("Please enter a pokemon name or 'exit' to exit the program: ")
    if input_pok != "exit":
      i = 0
      for obj in pokemon:
        if i != len(pokemon) - 1:
            if obj.name == input_pok:
              print(pokemon[i])
              return (obj, i)
        else:
          print("Pokemon not found.")
        i += 1
    else:
      exit()

# Call the find_pok function to search for a pokemon.
searched_pok, index = find_pok()


def change_hp():
  """
  Asks the user to either change the HP of the searched Pokemon or to exit the program. If the user chooses to change HP the user can input an amount of HP that should be added to the Pokemon. The function checks if the input entered by the user is an int > 0. The new HP of the Pokemon is the printed.
  """
  print("Would you like to add hp to the pokemon you searched for?")
  while True:
    new_hp = input("Please enter the HP to be added for the searched pokemon or enter 'exit' to exit the program:")
    if new_hp != "exit":
      try:
        new_hp = int(new_hp)
        if new_hp > 0:
          searched_pok.add_hp(new_hp)
          print("The new hp for " + searched_pok.name + " is: " + searched_pok.hp + ".\n")
          break
        else:
          print("Please enter an integer > 0.")
      except:
        print("Entered input was not of type <int>. Please try again.")
    else:
      exit()

# Call the change_hp function to ask the user if they would like to change the HP of a Pokemon.
change_hp()
