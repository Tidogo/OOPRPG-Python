#The entity class is a superclass used by Player and Monster subclasses. Contains the attributes shared by both as core elements used in multiple sectors.
class Entity :
    def __init__(self, name, lvl, str, const, dex, hlth, defense, dodge, crit, attPwr, critDmgMult) :
        self.Name = name
        self.Level = lvl
        self.Strength = str
        self.Constitution = const
        self.Dexterity = dex
        self.Health = hlth
        self.Defense = defense
        self.Dodge = dodge
        self.Crit = crit
        self.AttPower = attPwr
        self.CritDmgMultiplier = critDmgMult
    
    #This method is used to calculate the "substats" dodge, attpower, crit, and critdmgmultiplier. All of these are used in the battle mechanic.
    def CalcSubStats(self) :
        Defense = 1
        tempDex = self.Dexterity
        for i in range(tempDex) :
            self.Dodge += 0.05
            self.Crit += 0.025
        self.CritDmgMultiplier = 2
        self.AttPower = self.Strength * 2


