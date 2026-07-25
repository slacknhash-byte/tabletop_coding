from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Character:
    """ 
    Created 12/07/2026
    Last modified 25/07/2026
    The 'Character' class stores all the relevant data about the character:
    name, ability scores, etc. 
    All character attribute names are stored in lower case: any formatting will occur
    when the character sheet is output.
    """
    name: str
    char_race: str = 'Unassigned'
    char_class: str = 'Unassigned'
    level: int = 1
    hit_points: int = 0
    ability_scores: dict = field(default_factory=lambda: {
        "strength": "Unassigned", 
        "intelligence": "Unassigned", 
        "wisdom": "Unassigned", 
        "dexterity": "Unassigned", 
        "constitution": "Unassigned", 
        "charisma": "Unassigned"
    })
    biography: dict = field(default_factory=lambda: {
        "height": 0,
        "weight": 0,
        "age": 0,
        "gender": "Unassigned",
        "hair": "Unassigned",
        "eyes": "Unassigned"
    })
