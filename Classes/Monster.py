from Classes.Entity import Entity


#This monster class is a subclass of entity with new attributes essential for the battle mechanic.
class Monster(Entity) :
    def __init__(self, diff, init) :
        super().__init__(self)
        super().CalcSubStats(self)
        self.LootSeedValue = self.Level * 10
        self.ExperienceValue = self.Level * 10
        self.Difficulty = diff
        self.RndCashLoot = self.level * (10 * self.Difficulty)
        self.Initiative = init
    


