from Classes.Item import Item


class Weapon(Item) :
    def __init__(self, attpwr, twohanded, intve, critchance, critdmgmod) :
        super().__init__(self)
        self.AttackPower = attpwr
        self.TwoHanded = twohanded
        self.Initiative = intve
        self.CritChance = critchance
        self.CritDmgMmod = critdmgmod

