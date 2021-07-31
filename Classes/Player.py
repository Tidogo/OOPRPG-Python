from Classes.Entity import Entity


class Player(Entity) :
    def __init__(self, inven, equipped, cash, experience) : 
        super().__init__(self)
        self.Experience = experience
        self.Cash = 9999
        self.Equipped = equipped
        inven = [] 
        self.Inventory = inven
        equippedGear = []
        self.EquippedGear = equippedGear
        super().CalcSubStats(self)
        self.GearDefenseTotal = 0
        self.GearDodgeTotal = 0
        self.GearStrengthMod = 0
        self.GearConstitutionMod = 0
        self.GearDexterityMod = 0
        self.GearDefenseMod = 0
        self.GearDodgeMod = 0
        self.GearCritMod = 0
        self.GearAttPowerMod = 0
        self.GearInitiativeMod = 0
        self.GearCritDmgMod = 0
        self.BattleCounter = 0


