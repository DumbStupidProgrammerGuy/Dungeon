enemyTypes=[
    # "Dungeon Lizard",
    "Enemy",
    "slime"
    ]

slimeSprites = [
    "(\u0c77 \u0D2E \u0c84)", 
    "(\u0c77  \u0c84)", 
    "(\u0c77 \U00010119 \u0c84)", 
    "(\u0c77 \U00011119 \u0c84)", 
    "(\u0c77 \U00010101 \u0c84)",
    "(\U00010F57 \U00011119 \U00010F57)", 
    "(\U00010F57 \U00010119 \U00010F57)", 
    "(\U00010F57 \U00010101 \U00010F57)", 
    "( \U00010F58 )"
    ]

slimeColors  = [
    "\033[32m", # Green
    "\033[34m", # Blue
    "\033[35m" # Purple
]

lizardColors  = [
    "\033[32m", # Green
    "\033[32m", # Green
    "\033[32m", # Green
    "\033[32m", # Green
    "\033[32m", # Green
    "\033[33m", # Orange
    "\033[33m", # Orange
    "\033[33m", # Orange
    "\033[34m", # Blue
    "\033[34m", # Blue
    "\033[35m" # Purple
]

enemySprites = [
    "\U00013020",
    "\U0001301A",
    "\U0001301B",
    "\U0001301C",
    "\U0001301D",
    "\U0001301E",
    "\U0001301F",
    "\U00013041"
]

actions={
    "Attack":"target.takeDamage(self.damageMod)",
    "Defend":"self.defense += self.defenseMod",
    "Warrior's Strike":"target.takeDamage(self.damageMod+1)",
    "Warrior's Defense":"self.defense += self.defenseMod+1",
    "Shield Bash" : "target.takeDamage(self.damageMod//2)",
    "Sword Slash":"for enemy in enemies: enemy.takeDamage(self.damageMod//2 +1)",
    "Cunning Strike": "target.takeDamage(self.damageMod+1, True)",
    "Desperate Dodge": "self.dodges += 3",
    "Enhanced Relexes": "self.dodgeChance += 25",
    "Counterstrike": "self.counterstriking = True",
    "Dodge": "self.dodges += 1",
    "Split":'self.splitting = True',
    "Ooze": "target.takeDamage(target.defense + self.health//5, True)"
    }

cardsWithTargets=[
    "Attack",
    "Warrior's Strike",
    "Shield Bash",
    "Cunning Strike"]

items = [
    "Warrior's Sword",
    "Warrior's Shield",
    "Slink's Daggers",
    "Slink's Hood",
    "Mage's Spellbook",
    "Mage's Staff",
    "Weathered Sword",
    "Weathered Sheild",
    "Weathered Daggers",
    "Tattered Hood",
    "Tattered Spellbook",
    "Battered Staff",
    "Broken Sword",
    "Broken Shield",
    "Broken Daggers",
    "Torn Hood",
    "Torn Spellbook",
    "Broken Staff"
]

weapons = [
    "Warrior's Sword",
    "Slink's Daggers",
    "Mage's Staff",
    "Weathered Sword",
    "Weathered Daggers",
    "Battered Staff",
    "Broken Sword",
    "Broken Daggers",
    "Broken Staff"
]

nonWeaponItems = [
    "Warrior's Shield",
    "Slink's Hood",
    "Mage's Spellbook",
    "Weathered Sheild",
    "Tattered Hood",
    "Tattered Spellbook",
    "Broken Shield",
    "Torn Hood",
    "Torn Spellbook"
]

itemAbilities = {
    "Warrior's Sword" : "if self.damageMod < 5: self.damageMod = 5",
    "Warrior's Shield" : "if self.defenseMod < 5: self.defenseMod = 5",
    "Slink's Daggers" : "if self.damageMod < 4: self.damageMod = 4",
    "Slink's Hood" : "self.handSize = random.randrange(4, 6)",
    "Mage's Spellbook" : "",
    "Mage's Staff" : "if self.damageMod < 2: self.damageMod = self.defenseMod = 2",
    "Weathered Sword" : "if self.damageMod < 5: self.damageMod = 5",
    "Weathered Sheild" : "if self.defenseMod < 5: self.defenseMod = 5",
    "Weathered Daggers" : "if self.damageMod < 4: self.damgeMod = 4",
    "Tattered Hood" : "self.handSize = random.randrange(3, 5)",
    "Tattered Spellbook" : "",
    "Battered Staff" : "if self.damageMod < 2: self.damageMod = self.defenseMod = 2",
    "Broken Sword" : "if self.damageMod < 4: self.damgeMod = 4",
    "Broken Shield" : "",
    "Broken Daggers" : "if self.damageMod < 3: self.damageMod = 3",
    "Torn Hood" : "self.handSize = random.randrange(3, 4)",
    "Torn Spellbook" : "",
    "Broken Staff" : "if self.damageMod < 2: self.damageMod = self.defenseMod = 2"
}

itemDescriptions ={
    "Warrior's Sword" : "Increases attack damage to 5",
    "Warrior's Shield" : "Increases block amount to 5",
    "Slink's Daggers" : "Increases attack damage to 4",
    "Slink's Hood" : "Increases hand size to a random value between 4 and 6",
    "Mage's Spellbook" : "This item's ability hasn't been implemented yet, sorry", # Not implemented!
    "Mage's Staff" : "Increases attack damage and block amount to 2",
    "Weathered Sword" : "Increases your attack damage to 5",
    "Weathered Sheild" : "Increases block amount to 5",
    "Weathered Daggers" : "Increases attack damage to 4",
    "Tattered Hood" : "Sets hand size to a random value between 3 and 5",
    "Tattered Spellbook" : "This item's ability hasn't been implemented yet, sorry", # Not implemented!
    "Battered Staff" : "Increases attack damage and block amount to 2",
    "Broken Sword" : "Increases attack damage to 4",
    "Broken Shield" : "This item's ability hasn't been implemented yet, sorry", # Not implemented!
    "Broken Daggers" : "Increases attack damage to 3",
    "Torn Hood" : "Has a 50\u0025 of increasing hand size to 4",
    "Torn Spellbook" : "This item's ability hasn't been implemented yet, sorry", # Not implemented!
    "Broken Staff" : "Increases attack damage and block amount to 2"
}

agedItem = {
    "Warrior's Sword" : "Weathered Sword",
    "Warrior's Shield" : "Weathered Sheild",
    "Slink's Daggers" : "Weathered Daggers",
    "Slink's Hood" : "Tattered Hood",
    "Mage's Spellbook" : "Tattered Spellbook",
    "Mage's Staff" : "Battered Staff",
    "Weathered Sword" : "Broken Sword",
    "Weathered Sheild" : "Broken Shield",
    "Weathered Daggers" : "Broken Daggers",
    "Tattered Hood" : "Torn Hood",
    "Tattered Spellbook" : "Torn Spellbook",
    "Battered Staff" : "Broken Staff",
    "Broken Sword" : None,
    "Broken Shield" : None,
    "Broken Daggers" : None,
    "Torn Hood" : None,
    "Torn Spellbook" : None,
    "Broken Staff" : None
}
