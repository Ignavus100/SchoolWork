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
newp = Pokemon("Bulbasaur", "Grass", 100, 97, 67, 43)
newp.Damage(10)