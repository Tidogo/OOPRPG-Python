from Classes.Item import Item


class Armor(Item) :
    def __init__(self, defense, slot, dodgeMod) :
        super().__init__(self)
        self.Defense = defense
        self.Slot = slot
        self.DodgeMod = dodgeMod
