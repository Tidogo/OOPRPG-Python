from Classes.Item import Item

#This class is for armor items. Uses xml data to instantiate new armor objects.
class Armor(Item) :
    def __init__(self, defense, slot, dodgeMod) :
        super().__init__(self)
        self.Defense = defense
        self.Slot = slot
        self.DodgeMod = dodgeMod
