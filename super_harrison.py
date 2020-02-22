"""
The Marvel's hero

Author: Liang Chen
Email: biolchen@gmail.com

This game is for my 3-years old boy, Harrison, who always bother me while I am
working. I hope this game will keep him away from me for a while. 
I hope you are also enjoying it!

Cheers!
"""

import math
import os
import time
from random import choice, randint, sample


class Act:
    def __init__(self):
        pass

    def voice_over(self,*line_key):
        for i in line_key:
            print(Game_data().lines[i])
            print("." * 6)
            input()

    def menu_loop(self,menu):
        choice = None
        while choice != 'q':
            for key, value in menu.items():
                if isinstance(value, Act):
                    print('{}) {}'.format(key, value.__doc__))
                elif key == "Question":
                    print(RED + "%s" % value + RESET)
            print('q) Quit')
            choice = input('\nAction: ')
            if choice in menu:
                return menu[choice]
        if choice == 'q':
            print('Bye-bye!')
            exit(1)


class Superhero_Landing(Act):
    def play(self):
        if hero.name == "Frank Castle":
            self.voice_over(1, 2, 3)
        else:
            self.voice_over(7, 8, 9, 10, 11, 12)
        self.menu_loop(scenes_menu).play()


class Hells_kitchen(Act):
    '''Hells Kitchen'''
    def play(self):
        hero.talk(Game_data().lines[1], "Happy")
        Arena().play(0)
        self.menu_loop(scenes_menu).play()


class Atlantic_City(Act):
    '''The Atlantic City Casino'''
    def __init__(self):
        super().__init__()
        self.jackpot = 1000
        self.d = {"\U0001F352": 10, "\U0001F351": 9, "\U0001F350": 8, "\U0001F6CE": 7, "\U0001F346": 6, "\U0001F4B0": 5}
        self.items = "".join([key * value for key, value in self.d.items()])
        self.slot1 = None
        self.slot2 = None
        self.slot3 = None
        self.win = 0

    def play(self):
        playQuestion = self.ask()
        while self.jackpot != 0 and playQuestion and hero.gold >= 0:
            self.slot1 = self.items[randint(0, len(self.items) - 1)]
            self.slot2 = self.items[randint(0, len(self.items) - 1)]
            self.slot3 = self.items[randint(0, len(self.items) - 1)]
            self.wheel_turn()
            self.outputResult()
            playQuestion = self.ask()

        if self.jackpot == 0:
            print ("Reset jackpot")
            self.jackpot = 1000
        elif hero.gold <= 0:
            print("You are bankrupted")
            input("Leave the casino")
        self.menu_loop(scenes_menu).play()

    def wheel_turn(self):
        l = list("".join([key * value * 80 for key, value in self.d.items()]))
        CURSOR_UP = '\033[F'; ERASE_LINE = '\033[K'; t = 79
        while t >= 0:
            if t == len(self.items) - 1:
                print(ERASE_LINE + '{}\t{}\t{}'.format(sample(l, 80)[t], sample(l, 80)[t], sample(l, 80)[t]))
            else:
                print(CURSOR_UP + ERASE_LINE + '{}\t{}\t{}'.format(sample(l, 80)[t], sample(l, 80)[t],
                                                                   sample(l, 80)[t]))
            time.sleep(0.04)
            t -= 1

    def ask(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            if (self.jackpot <= 1):
                print("jackpot reset.")
                self.jackpot = 1000

            print("The Jackpot is currently: ${:0.0f}".format(self.jackpot))
            print("You have: ${:0.0f}".format(hero.gold))
            answer = input("Would you like to play? (y/n)").lower()
            if answer == "yes" or answer == "y":
                return True
            elif answer == "no" or answer == "n":
                print("You ended the game with ${:0.0f}.".format(hero.gold))
                input("Continue...")
                self.menu_loop(scenes_menu).play()
            else:
                print("Come again? yes or no? ")

    def outputResult(self):
        '''prints the current result'''
        if self.slot1 == "\U0001F352" and self.slot2 != "\U0001F352":
            self.win = 20
        elif self.slot1 == "\U0001F352" and self.slot2 == "\U0001F352" and self.slot3 != "\U0001F352":
            self.win = 50
        elif self.slot1 == "\U0001F352" and self.slot2 == "\U0001F352" and self.slot3 == "\U0001F352":
            self.win = 70
        elif self.slot1 == "\U0001F351" and self.slot2 == "\U0001F351" and (
                self.slot3 == "\U0001F351" or self.slot3 == "\U0001F346"):
            self.win = 100
        elif self.slot1 == "\U0001F350" and self.slot2 == "\U0001F350" and (
                self.slot3 == "\U0001F350" or self.slot3 == "\U0001F346"):
            self.win = 140
        elif self.slot1 == "\U0001F6CE" and self.slot2 == "\U0001F6CE" and (
                self.slot3 == "\U0001F6CE" or self.slot3 == "\U0001F346"):
            self.win = 200
        elif self.slot1 == "\U0001F346" and self.slot2 == "\U0001F346" and self.slot3 == "\U0001F346":
            self.win = 2500
        elif self.slot1 == "\U0001F4B0" and self.slot2 == "\U0001F4B0" and self.slot3 == "\U0001F4B0":
            self.win = self.jackpot
        else:
            self.win = -10

        hero.gold += self.win
        self.jackpot -= self.win

        if self.win == self.jackpot:
            print("You won the JACKPOT!!")
        if (self.win > 0):
            print('{}\t{}\t{} -- You win ${:0.0f}'.format(self.slot1, self.slot2, self.slot3, self.win))
            input("Continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print('{}\t{}\t{} -- You lost ${:0.0f}'.format(self.slot1, self.slot2, self.slot3, abs(self.win)))
            input("Continue...")
            os.system('cls' if os.name == 'nt' else 'clear')


class Status(Act):
    '''Check you status'''
    def play(self):
        hero.show_status()
        input("Return to menu")
        self.menu_loop(scenes_menu).play()


class Hotel(Act):
    '''Day's Inn (To recover hp)'''
    def play(self):
        print("One night stay costs $100")
        if hero.gold < 100:
            print ('insufficient funds!')
            input("press a key to return to the street")
            self.menu_loop(scenes_menu).play()
        else:
            print("Bienvenue! Monsieur!")
            input("press a key to continue")
        hero.gold = hero.gold - 100
        print ("You are siting down with a beer....")
        print("Nothing can not be healed by a hot shower and a good sleep....")
        input("press a key to continue")
        hero.heal_up()
        print("You have been healed up")
        input("Go out and kick more asses...")
        self.menu_loop(scenes_menu).play()


class Finale(Act):
    '''The Boss fight'''
    def play(self):
        Arena().play(1)
        print ("After defeating Fisk, you can finally have a good sleep.\nGood job!")
        time.sleep(1)
        exit(1)

class Death(Act):
    '''You don't want to come here'''
    def play(self):
        print("Game Over"); exit(1)

class Arena(Act):
    """Turn Based Battle Simulator"""
    def __init__(self):
        super().__init__()
        self.mob_count = {'Outlaw':0, 'Ninja':0, "Kingpin":0}
        self.boss = Kingpin()

        self.mob_list=[]
        self.action_menu = {}
        self.sucker=""

    def play(self, boss=0):
        self.spawn(boss)
        input("Press a key to start the battle...")
        self.fight()
        self.menu_loop(scenes_menu).play()

    def spawn(self, boss = 0):
        n = 0
        while n < choice([1, 2, 3]):
            if boss == 1:
                self.mob_count["Kingpin"] = 1
            else:
                self.mob_count["Kingpin"] = 0
            a = choice([Ninja().prof, Outlaw().prof])
            self.mob_count[a] += 1
            n += 1

        self.mob_list = [list([k,(k+str(i))]) for k,v in self.mob_count.items() for i in range(1,v+1)]
        ninja_name_list=[]
        outlaw_name_list=[]
        for i in self.mob_list:
            if i[0]=="Outlaw":
                name = choice(Game_data().Outlaw_name_list)
                if name not in outlaw_name_list:
                    self.action_menu[name] = Outlaw(name)
                else:
                    self.action_menu[name+" Jr."] = Outlaw(name+" Jr.")
                outlaw_name_list.append(name)
            elif i[0]=="Ninja":
                name = choice(Game_data().Ninja_name_list)
                if name not in ninja_name_list:
                    self.action_menu[name] = Ninja(name)
                else:
                    self.action_menu[name+" II"] = Ninja(name+" II")
            elif i[0]=="Kingpin":
                    self.action_menu[Kingpin().name] = Kingpin()
        mobs = []
        print("{}\n     VS".format(hero.show_hp()))
        for k, v in self.action_menu.items():
            mobs.append(k)
            print(v.show_hp())


    def choose_a_sucker(self):
        return choice(list(self.action_menu))

    def fight(self):
        input("Press a key to start the battle...")
        round = 1
        while hero.hp > 0 and sum([v.hp for k, v in self.action_menu.items()]) > 0:
            print("===== ROUND {} =====".format(round))
            mob_name = self.choose_a_sucker()
            mob_in_action = self.action_menu[mob_name]
            while mob_in_action.hp > 0 and hero.hp > 0:
                damage = randint(0, hero.attack)
                time.sleep(0.25)
                if damage == 0:
                    print ("You missed")
                    time.sleep(0.25)
                else:
                    print("On target")
                print("You deal {} damage to {}".format(damage, mob_name))
                mob_in_action.hp = mob_in_action.hp - damage
                print("{}".format(hero.show_hp()))
                print("\U0001F5E1  " * damage)
                for k, v in self.action_menu.items():
                    if k == mob_name:
                        v.show_hp(1, damage)
                    else:
                        v.show_hp()
                input("Take cover... incoming fire")
                damage = randint(0, mob_in_action.attack)
                if damage == 0:
                    print ("Missed")
                else:
                    print("You took {} damage from {}".format(damage, mob_name))
                hero.hp -= damage
                mob_in_action.show_hp()
                print("\U0001F5E1  " * damage)
                print("{}".format(hero.show_hp(1, damage)))
                input("Continue...")
                round += 1

        if sum([v.hp for k, v in self.action_menu.items()]) <= 0:
            hero.gold = hero.gold + 10*len(self.action_menu)
            print('You earned: \U0001F4B0:{:0.0f}'.format(10*len(self.action_menu)))
            hero.upgrade()
        elif hero.hp <= 0:
            print("Oh no! {} is dead\nGAME OVER".format(hero.name))
            time.sleep(1)
            exit(1)

class Characters:

    def __init__(self, name, prof, level, player, hp, maxHP, attack, accuracy, gold):
        self.name=name; self.prof=prof; self.level=level; self.player = player
        self.hp=hp; self.maxHP=int(maxHP*math.log10(10+level)); self.attack = int(attack*math.log10(10+level))
        self.accuracy = accuracy; self.gold=gold

    def show_status(self):
        if self.player:
            print(GREEN + "%s" % self.name + RESET, end="")
        else:
            print(RED + "%s" % self.name + RESET, end="")
        print("\U0001F494:{:0.0f}/{:0.0f} \U0001f44a:{:0.0f} \U0001F3B2:{:0.0f} \U0001F4B0:{:0.0f} \U0001F396 :{:0.0f}"\
              .format(self.hp, self.maxHP,self.attack,self.accuracy,self.gold,self.level))

    def show_hp(self, target = 0, damage = ''):
        if self.player:
            print(GREEN + "%s " % self.name + RESET, end = "")
        else:
            print(BLUE + "%s " % self.name + RESET, end = "")

        if self.hp <= 0:
            print("\U0001F480")
        else:
            if target == 1:
                print("\U0001F494"*self.hp +" -{}".format(damage))
            elif target == 0:
                print("\U0001F494" * self.hp + "{}".format(damage))
        return ""

    def punch(self):
        return randint(1, self.attack)

    def upgrade(self):
        print("\U0001F396 level UP!"); time.sleep(0.5); self.show_status(); time.sleep(0.5); print(">>>",end="")
        self.level += 1
        self.maxHP = int(round(self.maxHP*math.log10(10 + self.level)))
        time.sleep(0.5); self.show_status()

    def heal_up(self):
        CURSOR_UP = '\033[F'; ERASE_LINE = '\033[K'
        while self.hp <= self.maxHP:
            print (CURSOR_UP + ERASE_LINE + self.name+": "+ "\U0001F494"*self.hp)
            time.sleep(0.1)
            self.hp += 1
        self.hp = self.maxHP

    def talk(self, word, mood = "Angry"):
        print ("{}: {}".format(self.name,word),end = "")
        if mood == "Angry":
            print ("\U0001f604")
        else:
            print ("\U0001F616")


class Punisher(Characters):
    def __init__(self):
        super().__init__(name = "Frank Castle", prof = "Marine", level = 1, player = True, hp = 10, maxHP = 20, attack = 8, accuracy = 6, gold = 300)


class Daredevil(Characters):
    def __init__(self):
        super().__init__(name = "Matthew Murdock", prof = "Ninja", level = 1, player = True, hp = 16, maxHP = 16, attack = 5, accuracy = 8, gold = 300)


class Outlaw(Characters):
    def __init__(self, name = "unknown"):
        super().__init__(name = name, level = 1, prof = "Outlaw", player = False, hp = 10, maxHP = 10, attack = 3, accuracy = 1, gold = 25)


class Ninja(Characters):
    def __init__(self, name = "unknown"):
        super().__init__(name = name, level = 1, prof = "Ninja", player = False, hp = 10, maxHP = 10, attack = 1, accuracy = 8, gold = 10)


class Kingpin(Characters):
    def __init__(self):
        super().__init__(name = "Wilson fisk \U0001F60E", level = 10, prof = "Boss", player = False, hp = 20, maxHP = 20, attack = 2, accuracy = 1, gold = 0)


class Main:
    def run(self):
        global hero
        open_scene = Superhero_Landing()
        heroes = {'1': Punisher, '2': Daredevil}
        print("\n *** Welcome to Marvel's Hero! *** \n\n Do you want to kick some asses? \n")
        time.sleep(0.5)
        print(RED+"Now choose your character?\n"+RESET)
        for letter in heroes.keys():
            print("- Press {} for {}".format(letter, heroes[letter].__name__))
        while True:
            try:
                selection = input("> ")
                hero=heroes[selection]()
                open_scene.play()
            except KeyError:
                print("No such character! Try again...")
                continue


class Game_data:
    def __init__(self):
        self.action_menu = {}
        self.Outlaw_name_list = ["Joe Arron", "Wayne Barkeley", "Jesse James", "Jose Hernández"]
        self.Ninja_name_list = ["Haru Tanaka", "Kiwa Shinohara", "Akiko Takahashi", "Yang Ju"]

        self.lines={
            0:"."*6,
            99:"The quiet, secretive Hells' Kitchen is the darkest neighborhood of New York city.",
            1: "The quiet, secretive Hells' Kitchen is the darkest neighborhood of New York city, Let's see who is the sucker to show up",
            2:"After retired from the Marine Corp, you have a perfect life together with your kind wife, Ruth Godfrey.",
            3:"Until one day, Ruth was killed in home and you become the primary suspect.",
            4:"You have been set up..... but .... by whom",
            5:"Is this a revenge for the black ops in Ballarat?",
            6:"You have many questions..., first you have to find Burt Kenyon, your former partner on the job",
            7:"You are a blind lawyer who lives in New York City's Hell's Kitchen neighborhood. \n You runs a firm with best friend Franklin Nelson. \n You acquired you special ability in the age of 7, when you were blinded by a toxic waste spill. \n No one knows your xMen ability. \n After your father died in the hand of mobs, you promised to stop all criminal kinpins that controlled Hell's Kitchen.",
            8:"You are the Batman of Hell's Kitchen...",
            9:"You obtained a precious list of the criminals in the neighborhood",
            10:"The blacklist",
            11:"The next name on that list is...Burt Kenyon - a formal Marine",
            12: "It is time to knock his door",
            13: "It is a nice weekend, you are hanging out in the bar " + "\U0001f37a" * 3,
            17:"Good choice! Now go out and kick his ass",
            18:"Come on! Show what you have got!",
            19:"Please. Don't kill me...",
            20:"Run as far as you can, never show you face in my city",
            23:"Take cover...he is fighting back",
            100:"WTF? Let's try again",
        }

if __name__ == '__main__':
    # Define some global variables
    RED = "\x1b[31m"; GREEN = "\x1B[94m"; BLUE = "\x1b[34m"; RESET = "\x1B[0m"

    scenes_menu = {
        "Question": "Where do you want to go?\n",
        "1": Hells_kitchen(),
        "2": Atlantic_City(),
        "3": Hotel(),
        "4": Finale(),
        "5": Status()
    }

    hero = Punisher()
    Main().run()
