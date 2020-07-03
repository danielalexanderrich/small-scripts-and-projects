# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:54:16 2020

@author: dan
"""

party = []

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
    damage = 0
    select = input("attacks: {}, {} \n".format(pokemon.moveset[0], 
                   pokemon.moveset[1]))
    
    if select == "vinewhip" and pokemon.pType == "grass":
        print("selected vine whip")
        damage = pokemon.attack * 2
    
    elif select is "ember" and pokemon.pType == "fire":
        print("selected ember")
        damage = pokemon.attack * 2
    
    elif select is "water gun" and pokemon.pType == "water":
        print("selected water gun")
        damage = pokemon.attack * 2
    else:
        print("selected tackle")
        damage = pokemon.attack
        
    return damage, select

def Damage(pokemon, damage, select):
     typing = pokemon.pType
     
     if select == 'vine whip' and typing == 'grass':
         damage = damage * .75
     elif select == 'vine whip' and typing == 'water':
         damage = damage * 1.5
         
     elif select == 'water gun' and typing == 'water':
         damage = damage * .75
     elif select == 'water gun' and typing == 'fire':
         damage = damage * 1.5
         
     elif select == 'ember' and typing == 'fire':
         damage = damage * .75
     elif select == 'ember' and typing == 'grass':
         damage = damage * 1.5
         
     elif select == 'tackle':
         damage = damage
    
    return damage
    
#def Battle(pokemon, enemy):
    ### maybe calls another function Turn(pokemon), calls attack and damage
    ### if hp <= 0 at end of round, battle is over and winner is declared

#choice = input("Choose a pokemon: Bulbasaur, Charmander, or Squirtle:\n").lower()
#party.append(choice)

#print("You chose {}".format(party[0]))



