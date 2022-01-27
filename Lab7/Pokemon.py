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

  
  def __str__(self):
    """
    Prints all information about the Pokemon.
    :return: A string consisting of all the attributes of the Pokemon.
    """
    return "Name: " + self.name + "\n" + "Type: " + self.type1 + "\n" + "and " + self.type2 + "\n" + "Total: " + self.total + "\n" + "HP: " + self.hp + "\n" + "Attack: " + self.attack + "\n" + "Defense: " + self.defense + "\n" + "Special Attack: " + self.sp_atk + "\n" + "Special Defense: " + self.sp_def + "\n" + "Speed: " + self.speed + "\n" + "Generation: " + self.generation + "\n" + "Legendary: " + self.legendary + "\n"