class Entity :
    def __init__(self, Name, Level, Strength, Constitution, Dexterity, Health, Defense, Dodge, Crit, AttPower, CritDmgMultiplier) :
        self.Name = Name
        self.Level = Level
        self.Strength = Strength
        self.Constitution = Constitution
        self.Dexterity = Dexterity
        self.Health = Health
        self.Defense = Defense
        self.Dodge = Dodge
        self.Crit = Crit
        self.AttPower = AttPower
        self.CritDmgMultiplier = CritDmgMultiplier
    
    def CalcSubStats() :
        Defense = 1

