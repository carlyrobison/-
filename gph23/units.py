import typing
import cards

# Units can be generated from Cards, or they are just enemies.

class Unit:
    def __init__(self, name: str, friendly: bool, health: int, ready: bool):
        self.name: str = name
        self.friendly: bool = friendly
        self.health: int = health
        self.damage: int = 0
        self.ready: bool = ready

    def becomes_destroyed(self, damage: int) -> bool:
        return damage >= self.current_health()

    def deal_damage(self, damage: int) -> None:
        self.damage += damage
    
    def gain_health(self, health: int) -> None:
        self.health += health
        self.damage -= health
    
    def current_health(self) -> int:
        return self.health - self.damage

class Base(Unit):
    def __init__(self):
        super().__init__(self)

class Creature(Unit):
    def __init__(self, card: cards.Card):
        super().__init__(self)
        # TODO: convert card into Creature

# TODO: entire Food section