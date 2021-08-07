#The item class is a superclass which is inherited by Armor, Weapon, and Consumable.
class Item :
    def __init__(self, name, stackLmt, tempBoost, equippable, value) :
        self.Name = name
        self.StackLimit = stackLmt
        self.TempBoost = tempBoost
        self.Equippable = equippable
        self.Value = value
