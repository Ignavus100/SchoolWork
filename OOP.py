import random
class Pokemon():
    def __init__(self, name, ptype, hp, spd, att, df):
        self.name = name
        self.ptype = ptype
        self.hp = hp
        self.spd = spd
        self.att = att
        self.df = df
    def Damage(self, damage):
        self.hp -= damage
    def Talk(self):
        print(self.name)
    def Attack(self, other, val):
        print(self.name + " Attacks " + other.name)
        val -= other.df/10
        other.hp -= val
        print(other.name + " is on " + str(other.hp) + "hp")
    def Fade(self):
        if self.hp <= 0:
            print(self.name + " has faded")
    def Eat(self, food):
        self.hp += 10

#OC Creating pokemon
Bulbasaur = Pokemon("Bulbasaur", "Grass", 45, 45, 49, 49)
Ivysaur = Pokemon("Ivysaur", "Grass", 60, 60, 62, 63)
Venusaur = Pokemon("Venusaur", "Grass", 80, 80, 82, 83)
MVenusaur = Pokemon("MVenusaur", "Grass", 80, 80, 100, 123)
pokemon = [Bulbasaur, Ivysaur, Venusaur, MVenusaur]

def main():
    Lost = False
    for i in range(len(pokemon)):
        print(str(i + 1) + " " + str(pokemon[i].name))
    ch = int(input("Enter the number of your pokemon of choice: "))
    print("you have chosen " + str(pokemon[ch -1].name))
    choice = pokemon[ch - 1]
    other = random.choice(pokemon)
    GameOver = False
    while not GameOver:
        temp = True
        print('''
1. Eat Food
2. Attack
3. Run
''')
        action = int(input(">"))
        if action == 1:
            choice.Eat(1)
        elif action == 2:
            choice.Attack(other, 10)
        elif action == 3:
            Lost = True
            temp = False
            GameOver = True
        else:
            temp = False
            print("invalid input")
        if temp:
            other.Attack(choice, 10)
main()