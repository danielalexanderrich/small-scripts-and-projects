# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:54:16 2020

@author: dan
"""

class Pokemon:
    def __init__(self,
                 name = '', 
                 pType = '', 
                 weakness = None,
                 effective = None,
                 hp = 20,
                 attack = 10,
                 moveset = None):
        self.name = name
        self.pType = pType
        
        if weakness is None:
            weakness = []
        self.weakness = weakness
        
        if effective is None:
            effective = []
        self.effective = effective
        
        self.hp = hp
        self.attack = attack
        
        if moveset is None:
            moveset = ['tackle']
        self.moveset = moveset
        
    
    def typing(self):
            if self.pType == "grass":
                self.weakness.append('fire')
                self.effective.append('water')
                self.moveset.append('vinewhip')
            elif self.pType == "water":
                self.weakness.append('grass')
                self.effective.append('fire')
                self.moveset.append('water gun')
            elif self.pType == "fire":
                self.weakness.append('water')
                self.effective.append('grass')
                self.moveset.append('ember')
            else:
                return    
        
bulbasaur = Pokemon(name = "bulbasaur")
bulbasaur.pType = 'grass'
bulbasaur.typing()

squirtle = Pokemon(name = 'squirtle')
squirtle.pType = 'water'
squirtle.typing()

charmander = Pokemon(name = 'charmander')
charmander.pType = 'fire'
charmander.typing()


def Attack(pokemon):
    ### shows moves, checks type bonus, calculates damage
    
def Damage(pokemon):
    ### checks if resists, calculates damage, returns/updates hp
    
def Battle(pokemon, enemy):
    ### maybe calls another function Turn(pokemon), calls attack and damage
    ### if hp <= 0 at end of round, battle is over and winner is declared





