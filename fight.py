import runes
import sys
from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def monster_attack(source, target):
    '''has source monster do an attack on target monster
    returns damage dealt'''
    damage_randomizer = randint(80, 120)/100
    magic_randomizer = randint(0,10)
    if(type(source)!=runes.Physical_Animal and type(source)!=runes.Spell_Animal):
        return "Source of Attack is not Animal object"
    if(type(target)!=runes.Physical_Animal and type(target)!=runes.Spell_Animal):
        return "Target of Attack is not Animal object"
    target_monster = target
    source_monster = source
    attack_type = ''
    if(source_monster.spell_power > source_monster.attack_power):
        #more spell power, attack with spell. spells have no damage randomizer
        if(magic_randomizer<=1):
            source_damage = 0
            attack_type="spell misses"
        elif(magic_randomizer>=9):
            source_damage = source_monster.spell_power/10*2
            attack_type = "spell crits"
        else:
            source_damage = source_monster.spell_power/10
            attack_type = "spell attacks"
    else:
        source_damage = source_monster.attack_power/10*damage_randomizer
        attack_type = "attacks"
    source_damage = int(source_damage)
    target_monster.life -= source_damage
    attack_string = bcolors.WARNING+source_monster.name + bcolors.ENDC+" " + attack_type + " " + bcolors.WARNING+target_monster.name+bcolors.ENDC + " for "+str(source_damage)+" damage."
    result_array = [attack_string, source_monster, target_monster, source_damage, attack_type]
    return(result_array)


text = ''
while(text != 'p' and text !='s'):
    text = input("Spawn your monster. Type p for Physical Animal, or s for Spell Animal: ")

player_monster = runes.spawnAnimal(text)
print("Your monster is: "+bcolors.WARNING+player_monster.name+bcolors.ENDC)
print("Type f to fight.")
command = input("Command: ")
while(command != "f"):
    print("Incorrect input. Type f to fight.")
    command = input("Command: ")

if(command == "f"):
    enemy_monster = runes.spawnAnimal()
    while(enemy_monster==player_monster):
        enemy_monster = runes.spawnAnimal()

print("You're fighting "+bcolors.WARNING+enemy_monster.name+bcolors.ENDC)

print("Fight starts!")
attack_turn = 1

while(player_monster.life>=0 and enemy_monster.life>=0):
    print(bcolors.OKGREEN+ player_monster.name +": "+bcolors.ENDC+ str(player_monster.life)+" Life.")
    print(bcolors.FAIL+enemy_monster.name +": "+bcolors.ENDC+ str(enemy_monster.life)+" Life.")
    command = input("Press any key for next turn")
    if attack_turn == 1:
        #player attacks
        print(bcolors.OKBLUE+"Your turn"+bcolors.ENDC)
        attack = monster_attack(player_monster, enemy_monster)
        attack_turn = 0
    elif attack_turn == 0:
        #enemy attacks
        print(bcolors.OKBLUE+"Enemy turn"+bcolors.ENDC)
        attack = monster_attack(enemy_monster, player_monster)
        attack_turn = 1
    print(attack[0])



if(player_monster.life<=0):
    print(player_monster.name+" died. You lose.")
else:
    print(enemy_monster.name+" died. You win.")
