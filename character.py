from dataclasses import dataclass, field
from typing import Dict

@dataclass
class CharacterClass:
    """
    Created 31/07/2026

    The 'CharacterClass' class stores data about the character's classes.
    Confused yet? This is what happens when there's so much overlap between
    programming jargon and AD&D jargon. A character class is a character's
    profession - fighter, cleric, magic-user, etc. A character may have one or
    more classes at a time.
    In 1st and 2nd Edition AD&D, humans have one class, but if they have high
    stats they can 'dual class' - switch into different classes later in their
    careers.
    Meanwhile, other races -- dwarves, elves, etc -- can 'multiclass'. Their
    experience is divided between multiple classes, and they advance them
    simultaneously, but at a slower rate because their attention is divided
    between these multiple paths.
    """

    name: str # fighter, cleric, magic-user, etc. Often cross-referenced with
              # FIRST_EDITION_CLASS_PREREQS and FIRST_EDITION_CLASS_LIST
    level: int = 1
    experience: int = 0
    active: bool = True # Used if dual-classing

@dataclass
class CharacterRace:
    """
    Created 31/07/2026
    """

    name: str
    ability_limits: dict
    modifiers: dict
    movement: int
    infravision: int | None
    languages: list[str]
    
@dataclass
class Character:
    """ 
    Created 12/07/2026
    Last modified 25/07/2026
    28/07/2026: Added ignore_1e_gender_rule
    31/07/2026:
    
    The 'Character' class stores all the relevant data about the character:
    name, ability scores, etc. 
    All character attribute names are stored in lower case: any formatting will occur
    when the character sheet is output.
    """
    name: str
    race: CharacterRace | None = None
    classes: list[CharacterClass] = field(default_factory=list)
    hit_points: int = 0
    ability_scores: dict = field(default_factory=lambda: {
        "strength": "Unassigned", 
        "intelligence": "Unassigned", 
        "wisdom": "Unassigned", 
        "dexterity": "Unassigned", 
        "constitution": "Unassigned", 
        "charisma": "Unassigned"
    })
    ignore_1e_gender_rule = None
    biography: dict = field(default_factory=lambda: {
        "height": 0,
        "weight": 0,
        "age": 0,
        "gender": "Unassigned",
        "sex": "Unassigned",
        "hair": "Unassigned",
        "eyes": "Unassigned"
        
    })


    
