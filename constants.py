""" constants.py 
Created 24/07/2026
Last modified 25/07/2026

This file contains frequently used game-mechanical terms and their abbreviations, and
lookups for ability score prerequisites. 
 
Racial minimum and maximum scores for the various player character races, 
stratified by gender. Included solely for purposes of reproducing the effects
of the 1E Player's Handbook faithfully. There will be logic in the 
character generator to bypass it by way of the ignore_gender_stats variable.

Just 'cause Gygax wrote it doesn't necessarily mean I agree.
"""

# Created 24/07/2026 
ABILITY_NAMES = (
    "strength",
    "intelligence",
    "wisdom",
    "dexterity",
    "constitution",
    "charisma",
)

# Created 24/07/2026
ABBREVIATION_MAP = {
    "str": "strength",
    "int": "intelligence",
    "wis": "wisdom",
    "dex": "dexterity",
    "con": "constitution",
    "cha": "charisma",
}

# Created 24/07/2026
INPUT_TRANSLATION_MAP = {
    "str": "strength",
    "strength": "strength",
    "int": "intelligence",
    "intel": "intelligence",
    "intelligence": "intelligence",
    "wis": "wisdom",
    "wisdom": "wisdom",
    "dex": "dexterity",
    "dexterity": "dexterity",
    "con": "constitution",
    "constitution": "constitution",
    "cha": "charisma",
    "char": "charisma",
    "charisma": "charisma",
}

# Created 24/07/2026
ABILITY_SHORT_NAMES = {
    "strength": "str",
    "intelligence": "int",
    "wisdom": "wis",
    "dexterity": "dex",
    "constitution": "con",
    "charisma": "cha",
}

# Created 25/07/2026  
FIRST_EDITION_RACE_PREREQS = {
     "male": {
        "dwarf": {
            "strength": {
                "minimum":8,
                "maximum":18
            },
            "intelligence": {
                "minimum":3,
                "maximum":18
            },
            "wisdom": {
                "minimum":3,
                "maximum":18
            },
            "dexterity": {
                "minimum":3,
                "maximum":17
            },
            "constitution": {               
                "minimum":12,
                "maximum":19
            },
            "charisma": {
                "minimum":3,
                "maximum":16
            }
        },
        "elf": {
            "strength": {
                "minimum":3,
                "maximum":18
            },
            "intelligence": {
                "minimum":8,
                "maximum":18
            },
            "wisdom": {
                "minimum":3,
                "maximum":18
            },
            "dexterity": {
                "minimum":7,
                "maximum":19
            },
            "constitution": {               
                "minimum":6,
                "maximum":18
            },
            "charisma": {
                "minimum":8,
                "maximum":18
            }
        },
        "gnome": {
            "strength": {
                "minimum":6,
                "maximum":18
            },
            "intelligence": {
                "minimum":7,
                "maximum":18
            },
            "wisdom": {
                "minimum":3,
                "maximum":18
            },
            "dexterity": {
                "minimum":3,
                "maximum":17
            },
            "constitution": {               
                "minimum":8,
                "maximum":19
            },
            "charisma": {
                "minimum":3,
                "maximum":18
            }
        },
        "half-elf": {
            "strength": {
                "minimum":3,
                "maximum":18
            },
            "intelligence": {
                "minimum":4,
                "maximum":18
            },
            "wisdom": {
                "minimum":3,
                "maximum":18
            },
            "dexterity": {
                "minimum":3,
                "maximum":17
            },
            "constitution": {               
                "minimum":6,
                "maximum":18
            },
            "charisma": {
                "minimum":3,
                "maximum":18
            }
        },        
        "halfling": {
            "strength": {
                "minimum":6,
                "maximum":17
            },
            "intelligence": {
                "minimum":6,
                "maximum":18
            },
            "wisdom": {
                "minimum":3,
                "maximum":17
            },
            "dexterity": {
                "minimum":8,
                "maximum":18
            },
            "constitution": {               
                "minimum":10,
                "maximum":19
            },
            "charisma": {
                "minimum":3,
                "maximum":18
            }
        },
        "half-orc": {
            "strength": {
                "minimum":6,
                "maximum":18
            },
            "intelligence": {
                "minimum":3,
                "maximum":17
            },
            "wisdom": {
                "minimum":3,
                "maximum":14
            },
            "dexterity": {
                "minimum":3,
                "maximum":17
            },
            "constitution": {               
                "minimum":13,
                "maximum":19
            },
            "charisma": {
                "minimum":3,
                "maximum":12
            }
        },        
    },
    "female": {
        "dwarf": {
            "strength": {
                "minimum":8,
                "maximum":17
            },
            "intelligence": {
                "minimum":3,
                "maximum":18
            },
            "wisdom": {
                "minimum":3,
                "maximum":18
            },
            "dexterity": {
                "minimum":3,
                "maximum":17
            },
            "constitution": {               
                "minimum":12,
                "maximum":19
            },
            "charisma": {
                "minimum":3,
                "maximum":16
            }
        },
        "elf": {
            "strength": {
                "minimum":3,
                "maximum":16
            },
            "intelligence": {
                "minimum":8,
                "maximum":18
            },
            "wisdom": {
                "minimum":3,
                "maximum":18
            },
            "dexterity": {
                "minimum":7,
                "maximum":19
            },
            "constitution": {               
                "minimum":6,
                "maximum":18
            },
            "charisma": {
                "minimum":8,
                "maximum":18
            }
        },
        "gnome": {
            "strength": {
                "minimum":6,
                "maximum":15
            },
            "intelligence": {
                "minimum":7,
                "maximum":18
            },
            "wisdom": {
                "minimum":3,
                "maximum":18
            },
            "dexterity": {
                "minimum":3,
                "maximum":17
            },
            "constitution": {               
                "minimum":8,
                "maximum":19
            },
            "charisma": {
                "minimum":3,
                "maximum":18
            }
        },
        "half-elf": {
            "strength": {
                "minimum":3,
                "maximum":17
            },
            "intelligence": {
                "minimum":4,
                "maximum":18
            },
            "wisdom": {
                "minimum":3,
                "maximum":18
            },
            "dexterity": {
                "minimum":3,
                "maximum":17
            },
            "constitution": {               
                "minimum":6,
                "maximum":18
            },
            "charisma": {
                "minimum":3,
                "maximum":18
            }
        },        
        "halfling": {
            "strength": {
                "minimum":6,
                "maximum":14
            },
            "intelligence": {
                "minimum":6,
                "maximum":18
            },
            "wisdom": {
                "minimum":3,
                "maximum":17
            },
            "dexterity": {
                "minimum":8,
                "maximum":18
            },
            "constitution": {               
                "minimum":10,
                "maximum":19
            },
            "charisma": {
                "minimum":3,
                "maximum":18
            }
        },
        "half-orc": {
            "strength": {
                "minimum":6,
                "maximum":18
            },
            "intelligence": {
                "minimum":3,
                "maximum":17
            },
            "wisdom": {
                "minimum":3,
                "maximum":14
            },
            "dexterity": {
                "minimum":3,
                "maximum":17
            },
            "constitution": {               
                "minimum":13,
                "maximum":19
            },
            "charisma": {
                "minimum":3,
                "maximum":12
            }
        }        
    }
}
