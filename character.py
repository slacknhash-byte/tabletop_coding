from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Character:
    """ The 'Character' class stores all the relevant data about the character:
    name, ability scores, etc. """
    name: str
    char_race: str = 'Unassigned'
    char_class: str = 'Unassigned'
    level: int = 1
    hit_points: int = 0
    ability_scores: dict = field(default_factory=lambda: {
        "Strength": "Unassigned", 
        "Intelligence": "Unassigned", 
        "Wisdom": "Unassigned", 
        "Dexterity": "Unassigned", 
        "Constitution": "Unassigned", 
        "Charisma": "Unassigned"
    })
    biography: dict = field(default_factory=lambda: {
        "Height": 0,
        "Weight": 0,
        "Age": 0,
        "Gender": "Unassigned",
        "Hair": "Unassigned",
        "Eyes": "Unassigned"
    })
