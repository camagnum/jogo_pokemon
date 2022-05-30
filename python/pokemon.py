import random
import time


options = ['a','b','c','d','e']
pokemons = {'a':('Pikachu',120,35,20),
            'b':('Charmander',115,40,15),
            'c':('Squirtle',130,25,20),
            'd':('Bulbasaur',125,30,30),
            'e':('Mewtwo',130,40,25)};

class Pkmn_select:
    def __init__(self,trainer_name,name,hp,attack,cure):
        self.trainer_name = trainer_name
        self.name = name;
        self.hp = hp;
        self.attack = attack;
        self.cure = cure;
        print("\n" + self.trainer_name + "'s selected " + self.name + "!");
        print('HP = ' + str(self.hp) +
        '\nAttack = ' + str(self.attack) +
        '\nCure = ' + str(self.cure));

    def damage(self,opp_attack):
        if opp_attack < self.hp:
            self.hp -= opp_attack;
        else:
            self.hp = 0;
        time.sleep(1)
        print("\n" + self.trainer_name + "'s " + self.name + "'s got " + str(opp_attack) + " damage!");
        time.sleep(1)
        print(self.trainer_name + "'s " + self.name + "'s HP now is " + str(self.hp) + ".");

    def heal(self):
        self.hp += self.cure;
        time.sleep(1)
        print("\n" + self.trainer_name + "'s " + self.name + "'s healed " + str(self.cure) + " of itself HP.");
        time.sleep(1)
        print(self.trainer_name + "'s " + self.name + "'s HP now is " + str(self.hp) + ".");

# Pokémon Battle
print("Hello! Let's start the Pokémon battle.");
usr_name = input("What's your name?\n");

# User's pokémon selection
usr_select = str(input("Please, select your Pokémon: \na) " + pokemons['a'][0] + 
    "\nb) " + pokemons['b'][0] + 
    "\nc) " + pokemons['c'][0] + 
    "\nd) " + pokemons['d'][0] + 
    "\ne) " + pokemons['e'][0] + 
    "\n"));
pokemon = pokemons[usr_select];

pkmn_usr = Pkmn_select(usr_name,pokemon[0],pokemon[1],pokemon[2],pokemon[3]);

# CPU's pokémon selection
cpu_select = options[random.randint(0,3)];
pokemon = pokemons[cpu_select];

pkmn_cpu = Pkmn_select("CPU",pokemon[0],pokemon[1],pokemon[2],pokemon[3]);

# Battle
while True:
    # Player's round
    while True:
        action = input("\nChoose your action: \na) Attack\nb) Heal\nc) Run!\n")
        if action == 'a':
            print("\n" + pkmn_usr.trainer_name + "'s " + pkmn_usr.name + " attacks!")
            pkmn_cpu.damage(pkmn_usr.attack);
            break
        elif action == 'b':
            print("\n" + pkmn_usr.trainer_name + "'s " + pkmn_usr.name + " heals itself!")
            pkmn_usr.heal();
            break
        elif action == 'c':
            print("\n" + pkmn_usr.trainer_name + "'s " + pkmn_usr.name + " ran away!")
            pkmn_usr.hp = 0;
            break
        else:
            print("Select a correct option.")

    # CPU's round
    if pkmn_cpu.hp > 0:
        cpu_action = options[random.randint(0,1)]
        if cpu_action == 'a':
            print("\n" + pkmn_cpu.trainer_name + "'s " + pkmn_cpu.name + " attacks!")
            pkmn_usr.damage(pkmn_cpu.attack);
        elif cpu_action == 'b':
            print("\n" + pkmn_cpu.trainer_name + "'s " + pkmn_cpu.name + " heals itself.")
            pkmn_cpu.heal();

# Finish conditions
    if pkmn_usr.hp <= 0:
        time.sleep(1)
        print("\n" + pkmn_cpu.trainer_name + " wins!")
        break
    
    if pkmn_cpu.hp <= 0:
        time.sleep(1)
        print("\n" + pkmn_usr.trainer_name + " wins!")
        break

print("Game Over")