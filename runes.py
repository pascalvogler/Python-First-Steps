from random import randint

#BASIC ANIMAL CLASS
class Basic_Form:
    
    #class variables
    life_multiplicator = 15
    attack_power_multiplicator = 10
    spell_power_multiplicator = 20
    animal_population = 0
    
    total_attack_power = 0
    total_spell_power = 0
    
    #class function (init). Defines actions for each instance
    def __init__(self, name, type, subtype, lore, food):
        self.name = name
        self.type = type
        self.subtype = subtype
        self.lore = lore
        self.food = food
             
        #counts total instances
        Basic_Form.animal_population += 1
          
    def basic_info(self):
        return '{} / {} / {}'.format(self.name, self.type, self.subtype)

    def __repr__(self):
        return "Basic_Form('{}', '{}', '{}', '{}', '{}')".format(self.name, self.type, self.subtype, self.lore, self.food)

    def __str__(self):
        return '{} - {}'.format(self.name, self.lore)

#PHYSICAL BASED ANIMAL CLASS        
class Physical_Animal(Basic_Form):
    
    physical_population = 0
    
    def __init__(self, name, type, subtype, lore, food, size, dexterity, strength, stamina, enemy=None):
        super().__init__(name, type, subtype, lore, food)
        self.size = size
        self.dexterity = dexterity
        self.strength = strength
        self.stamina = stamina
        self.life = self.life_multiplicator * self.stamina
        self.attack_power = self.attack_power_multiplicator * self.strength + self.attack_power_multiplicator * self.dexterity
        self.spell_power = 0
        if enemy is None:
            self.enemy = []
        else:
            self.enemy = enemy
        
        Physical_Animal.physical_population += 1
    
    def enemy_name(self):
        for i in self.enemy:
            return(i.name)
     
    #FIRST CHECKS IF THERE IS ONLY ONE OPPONENT. THEN IT COMPARES THE POWER AND THEREFORE RETURNS FIGHT ESTIMATE. 
    def enemy_estimate(self):
        if len(self.enemy) > 1:
            return "Dude, more than one enemy is too much... or are you King Kong?!"
        elif len(self.enemy) == 0:
            return "There is no enemy."
        else:
            for i in self.enemy:
                if (i.spell_power() + i.attack_power()) < (self.attack_power() + self.spell_power()):
                    return self.name + " probably wins against " + i.name
                else:
                    return self.name + " probably loses against " + i.name

#SPELL BASED ANIMAL CLASS
class Spell_Animal(Basic_Form):
    
    spell_population = 0
    
    def __init__(self, name, type, subtype, lore, food, intelligence, stamina, enemy=None):
        super().__init__(name, type, subtype, lore, food)
        self.intelligence = intelligence
        self.stamina = stamina
        self.life = self.life_multiplicator * self.stamina
        self.attack_power = 0
        self.spell_power = self.spell_power_multiplicator * self.intelligence
        if enemy is None:
            self.enemy = []
        else:
            self.enemy = enemy
        
        Spell_Animal.spell_population += 1
        
    
    def enemy_name(self):
        for i in self.enemy:
            return(i.name)
    
    #FIRST CHECKS IF THERE IS ONLY ONE OPPONENT. THEN IT COMPARES THE POWER AND THEREFORE RETURNS FIGHT ESTIMATE.        
    def enemy_estimate(self):
        if len(self.enemy) > 1:
            return "Dude, more than one enemy is too much... or are you King Kong?!"
        elif len(self.enemy) == 0:
            return "There is no enemy."
        else:
            for i in self.enemy:
                if (i.attack_power() + i.spell_power()) < (self.spell_power() + self.attack_power()):
                    return self.name + " probably wins against " + i.name
                else:
                    return self.name + " probably loses against " + i.name


    
#INSTANCES LEVEL 1 BASIC FORM       
animal_1 = Basic_Form("Vittorio","Dinosaur", "Jungle", "Tapfere Octagon Kämpfer!","Meat")
animal_2 = Basic_Form("Samuel","Mamal (Non human)", "Mountain", "Wiit gfürchtets Flexitariermonster", "Meat")
animal_3 = Basic_Form("Claudio","Mamal (Non human)", "Jungle", "Mächtige Pflanzefresser", "Plants")
animal_4 = Basic_Form("Jazz","Human", "Forest", "Overlord Veganerin isch sie!", "Plants")
animal_5 = Basic_Form("Selina", "Dragon", "Mountain", "Sie seit immer, Momos sind mächtiger als Buuchschmerze.", "Meat")

#INSTANCES LEVEL 2 PHYSICAL ANIMALS
physical_1 = Physical_Animal("Veloceraptor","Dinosaur", "Jungle", "This is a very fast and dangerous beast that uses its highly evolved brain to track down its pray and kill it with its sharp claws.","Meat", 20, 85, 20, 30, [])
physical_2 = Physical_Animal("Sabretooth","Mamal (Non human)", "Mountain", "Swift Hunter, which can survive in extreme environments", "Meat", 15, 90, 10,30, [])
physical_3 = Physical_Animal("Silverback","Mamal (Non human)", "Jungle", "Ancient Monkey-Species that can get extremely tall and powerfull.", "Plants", 90, 25, 90, 95, [])
physical_4 = Physical_Animal("Shaman","Human", "Forest", "Spiritual Guide of a whole people. Can control the spirits around him.", "Plants", 18, 5, 5, 20, [])
physical_5 = Physical_Animal("Skyblade", "Dragon", "Mountain", "Small Dragon species, inhabiting the hightest Mountains. The Name Skyblade comes from its sharp and thin body structure.", "Meat", 45, 45, 60, 50, [])
physical_animals = [physical_1, physical_2, physical_3, physical_4, physical_5]

#INSTANCES LEVEL 2 SPELL ANIMALS
spell_1 = Spell_Animal("Spell-Raptor","Dinosaur", "Jungle", "This is a very fast and dangerous beast that uses its highly evolved brain to track down its pray and kill it with its sharp claws.","Meat",60,30, [])
spell_2 = Spell_Animal("Magical Sabretooth","Mamal (Non human)", "Mountain", "Swift Hunter, which can survive in extreme environments", "Meat", 55,30, [])
spell_3 = Spell_Animal("Silverback","Mamal (Non human)", "Jungle", "Ancient Monkey-Species that can get extremely tall and powerfull.", "Plants", 45,95, [])
spell_4 = Spell_Animal("Shaman","Human", "Forest", "Spiritual Guide of a whole people. Can control the spirits around him.", "Plants", 100, 20, [])
spell_5 = Spell_Animal("Skyblade", "Dragon", "Mountain", "Small Dragon species, inhabiting the hightest Mountains. The Name Skyblade comes from its sharp and thin body structure.", "Meat", 70, 50, [])
spell_animals = [spell_1, spell_2, spell_3, spell_4, spell_5]

all_animals = physical_animals+spell_animals

def spawnAnimal(type='r'):
  ''' takes type as string 'p' or 's'
  returns a random animal from the respective type, or random from all types
  if no type is given'''
  if type == 'r':
    return all_animals[randint(0,len(all_animals)-1)]
  if type == 'p':
    return physical_animals[randint(0,len(physical_animals)-1)]
  if type == 's':
    return spell_animals[randint(0,len(spell_animals)-1)]


#Fightcode

#spell_2.enemy.append(physical_1)
#print(spell_2.enemy_estimate())
