from Classes.Entity import Entity


class Monster(Entity) :
    def __init__(self) -> None:
        super().__init__()
        super().CalcSubStats(self)
        self.LootSeedValue = 0
        self.ExperienceValue = 0
        self.RndCashLoot = 0
        self.Difficulty = 0
        self.Initiative = 0.0
    


