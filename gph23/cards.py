import typing
from enum import Enum

class Food(Enum):
    BOARRY = 1
    FLOWER = 2
    EGG = 3
    BEE = 4
    CREAM = 5
    BUTTER = 6
    PIE = 7

class Cost(Enum):
    BOARRY = 1
    FLOWER = 2
    EGG = 3
    BEE = 4
    CREAM = 5
    BUTTER = 6
    DOT = 7
    MILK = 8

costDictionary = {
    Cost.BOARRY: [Food.BOARRY, Food.PIE],
    Cost.FLOWER: [Food.FLOWER, Food.PIE],
    Cost.EGG: [Food.EGG, Food.PIE],
    Cost.BEE: [Food.BEE, Food.PIE],
    Cost.CREAM: [Food.CREAM, Food.PIE],
    Cost.BUTTER: [Food.BUTTER, Food.PIE],
    Cost.DOT: [Food.BOARRY, Food.FLOWER, Food.EGG, Food.BEE, Food.CREAM, Food.BUTTER, Food.PIE],  # all of them
    Cost.MILK: [Food.BUTTER, Food.CREAM, Food.PIE]
}

def canPayForCost(food: Food, cost: Cost):
    return cost in costDictionary[food]

class Faction(Enum):
    BOARS = 1
    BEES = 2
    DINOSAURS = 3
    DRYADS = 4
    BUTTER = 5
    MILK = 6
    CREAM = 7

class Card:
    def __init__(self, name: str, power: int, health: int, cost: typing.List[Cost],
                 additional_desc: str, faction: Faction, legendary: bool = False):
        self.name: str = name
        self.power: int = power
        self.health: int = health
        self.cost: typing.List[Cost] = cost
        self.unimplemented: str = additional_desc
        self.faction: Faction = faction
        self.legendary: bool = legendary

cards = {
    "Beeowulf": Card("Beeowulf", 1, 1, [Cost.BEE], "Special attack moves enemy creatures", Faction.BEES),
    "Beethoven": Card("Beethoven", 2, 3, [Cost.DOT, Cost.BEE], "First time damaged takes one less", Faction.BEES),
    "Boarry Farmer": Card("Boarry Farmer", 3, 2, [Cost.DOT, Cost.BOARRY], "Can only attack in column", Faction.BOARS),
    "Chicken": Card("Chicken", 1, 1, [Cost.EGG], "Special: on start of next turn, gain pie", Faction.DINOSAURS),
    "Chocolate Calf": Card("Chocolate Calf", 1, 3, [Cost.DOT, Cost.BUTTER], "Flex with cream +1 temporary power", Faction.BUTTER),
    "Dargle, Dargle, Deargle": Card("Dargle, Dargle, Deargle", 2, 3, [Cost.EGG, Cost.EGG, Cost.EGG], "Legendary, effects cryptic", Faction.DINOSAURS, legendary=True),
    "Flora The Explora": Card("Flora The Explora", 0, 1, [Cost.FLOWER], "Special: draw a card", Faction.DRYADS),
    "Hamlet": Card("Hamlet", 1, 1, [Cost.BOARRY], "", Faction.BOARS),
    "Hog": Card("Hog", 2, 1, [Cost.BOARRY], "Can only attack in column", Faction.BOARS),
    "Log": Card("Log", 1, 2, [Cost.FLOWER], "", Faction.DRYADS),
    "Nepeta Legion": Card("Nepeta Legion", 2, 4, [Cost.FLOWER, Cost.FLOWER, Cost.FLOWER], "When summoned, draw a card", Faction.DRYADS),
    "New Boarn": Card("New Boarn", 3, 4, [Cost.BOARRY, Cost.BOARRY, Cost.BOARRY], "When summoned, moves randomly.", Faction.BOARS),
    "o": Card("o", 1, 1, [Cost.BUTTER], "When Summoned, Adjacent Friendly Milk and cream creatures gain +1 health", Faction.BUTTER),
    "Payne": Card("Payne", 1, 2, [Cost.MILK], "When attacked by cream or butter, takes +1 damage", Faction.MILK),
    "PBee & J": Card("PBee & J", 1, 1, [Cost.BEE], "When damaged, by a creature, that creature takes 1 damage", Faction.BEES),
    "Petroleum Jelly": Card("Petroleum Jelly", 1, 1, [Cost.EGG], "When damages by a creature in this column, takes -1 damage", Faction.DINOSAURS),
    "re": Card("re", 1, 1, [Cost.CREAM], "When summoned, adjacent friendly butter and milk creatures gain +1 power", Faction.CREAM),
    "Roe Doe Dendron": Card("Roe Doe Dendron", 1, 2, [Cost.DOT, Cost.FLOWER], "Special attack chains damage", Faction.DRYADS),
    "Tusk Enhancement": Card("Tusk Enhancement", 0, 2, [Cost.DOT, Cost.BOARRY, Cost.BOARRY], "When summoned, other creatures in its column gain +1 power", Faction.BOARS),
    "2 Bees or not 2 Bees?": Card("2 Bees or not 2 Bees?", 1, 2, [Cost.BEE, Cost.BEE, Cost.BEE], "Takes half damage, rounded down.", Faction.BEES),
    "Vanilla Calf": Card("Vanilla Calf", 1, 3, [Cost.DOT, Cost.CREAM], "Flex butter: removes 1 damage from creature", Faction.CREAM),
    "Yoshisaur Munchakoopas": Card("Yoshisaur Munchakoopas", 2, 4, [Cost.DOT, Cost.EGG], "", Faction.DINOSAURS),
}
