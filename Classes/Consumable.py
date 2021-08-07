from Classes.Item import Item

#This class is for consumable items. Inherits from Item superclass. Used in battle mechanic.
class Consumable(Item) :
    def __init__(self, Name, StackLimit, TempBoost, Equippable, Value, HealthBoost, TempCritBoost, TempAttackBoost, TempDodgeBoost, TempDefenseBoost, TempInitBoost, NumOfBattles) :
        super().__init__(Name, StackLimit, TempBoost, Equippable, Value)
        self.TempCritBoost = TempCritBoost
        self.TempAttackBoost = TempAttackBoost
        self.TempDefenseBoost = TempDefenseBoost
        self.TempInitBoost = TempInitBoost
        self.NumOfBattles = NumOfBattles
        self.HealthBoost = HealthBoost
