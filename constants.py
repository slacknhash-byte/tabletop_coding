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

# Created 26/07/2026
# Modified 27/07/2026
FIRST_EDITION_CLASS_PREREQS = {
    "cleric": {
        "races": {
            "pc": [
                "half-elf", 
                "half-orc", 
                "human"
             ],
            "npc": [
                "dwarf", 
                "elf", 
                "gnome", 
                "half-elf", 
                "half-orc", 
                "human"
            ]
        },
        "level_limits": {
            "dwarf": 8,
            "elf": 7,
            "gnome": 7,
            "half-elf": 5,
            "half-orc": 4,
            "human": None
        },
        "exceed_level_limits": {},
        "minimum_abilities": {
            "wisdom": 9
        },
        "xp_bonus": {
            "wisdom": 16
        }        
    },
    "druid": {
        "races": {
            "pc": [
                "half-elf", 
                "human"
            ],
            "npc": [
                "half-elf", 
                "halfling", 
                "human"
            ]
        },
        "level_limits": {
            "half-elf": None,
            "halfling": 6,
            "human": None
        },
        "exceed_level_limits": {},
        "minimum_abilities": {
            "wisdom": 12,
            "charisma": 15
        },
        "xp_bonus": {
            "wisdom": 16,
            "charisma": 16
        }        
    },
    "fighter": {
        "races": {
            "pc": [
                "dwarf", 
                "elf", 
                "gnome", 
                "half-elf", 
                "halfling", 
                "half-orc", 
                "human"
            ],
            "npc": [
                "dwarf", 
                "elf", 
                "gnome", 
                "half-elf", 
                "halfling", 
                "half-orc", 
                "human"
            ]
        },
        "level_limits": {
            "dwarf": 7,
            "elf": 5,
            "gnome": 5,
            "half-elf": 6,
            "halfling": 4,
            "half-orc": 10,
            "human": None
        },
        "exceed_level_limits": {
            "dwarf": {
                "ability_scores": {
                    "strength": {
                        17: 8,
                        18: 9
                    }
                }
            },
            "elf": {
                "ability_scores": {
                    "strength": {
                        17: 6,
                        18: 7
                    }
                }
            },
            "gnome": {
                "ability_scores": {
                    "strength": {
                        18: 6
                    }
                }            
            },
            "half-elf": {
                "ability_scores": {
                    "strength": {
                        17: 7,
                        18: 8
                    }
                }            
            },
            "halfling": {
                "ability_scores": {
                    "strength": {
                        17: {
                            "sub-race": {
                                "tallfellow": 5
                            }
                        },
                        18: {
                            "sub-race": {
                                "tallfellow": 6,
                                "stout": 5
                            }
                        }
                    }
                }            
            }            
        },
        "minimum_abilities": {
            "strength": 9,
            "constitution": 7
        },
        "xp_bonus": {
            "strength": 16,
        }        
    },
    "paladin": {
        "races": {
            "pc": [
                "human"
            ],
            "npc": [
                "human"
            ]
        },
        "level_limits": {
            "human": None
        },
        "exceed_level_limits": {},
        "minimum_abilities": {
            "strength": 12,
            "intelligence": 9,
            "wisdom": 13,
            "constitution": 9,
            "charisma": 17
        },
        "xp_bonus": {
            "strength": 16,
            "wisdom": 16
        }
    },    
    "ranger": {
        "races": {
            "pc": [
                "half-elf", 
                "human"
            ],
            "npc": [
                "half-elf", 
                "human"
            ]
        },
        "level_limits": {
            "half-elf": 7,
            "human": None
        },
        "exceed_level_limits": {
            "half-elf": {
                "ability_scores": {
                    "strength": {
                        17: 8
                    }
                }
            }
        },
        "minimum_abilities": {
            "strength": 13,
            "intelligence": 13,
            "wisdom": 14,
            "constitution": 14,
        },
        "xp_bonus": {
            "strength": 16,
            "intelligence": 16,
            "wisdom": 16
        }
    },        
    "magic-user": {
        "races": {
            "pc": [
                "elf", 
                "half-elf", 
                "human"
            ],
            "npc": [
                "half-elf", 
                "human"
            ]
        },
        "level_limits": {
            "elf": 9,
            "half-elf": 7,
            "human": None
        },
        "exceed_level_limits": {
            "elf": {
                "ability_scores": {
                    "intelligence": {
                        17: 10,
                        18: 11
                    }
                }
            },        
            "half-elf": {
                "ability_scores": {
                    "intelligence": {
                        17: 7,
                        18: 8
                    }
                }
            },        
        },
        "minimum_abilities": {
            "intelligence": 9,
        },
        "xp_bonus": {
            "intelligence": 16,
        }
    },        
    "illusionist": {
        "races": {
            "pc": [
                "gnome",
                "human"
            ],
            "npc": [
                "gnome", 
                "human"
            ]
        },
        "level_limits": {
            "gnome": 5,
            "human": None
        },
        "exceed_level_limits": {
            "gnome": {
                "ability_scores": {
                    "intelligence": {
                        17: 6,
                        18: 7
                    },
                    "dexterity": {
                        17: 6,
                        18: 7
                    }
                }
            }
        },
        "minimum_abilities": {
            "intelligence": 15,
            "dexterity": 16
        },
        "xp_bonus": {}
    },        
    "thief": {
        "races": {
            "pc": [
                "dwarf", 
                "elf", 
                "gnome", 
                "half-elf", 
                "halfling", 
                "half-orc", 
                "human"
            ],
            "npc": [
                "dwarf",
                "elf", 
                "gnome", 
                "half-elf", 
                "halfling", 
                "half-orc", 
                "human"
            ]
        },
        "level_limits": {
            "dwarf": None,
            "elf": None,
            "gnome": None,
            "half-elf": None,
            "halfling": None,
            "half-orc": 6,
            "human": None
        },
        "exceed_level_limits": {
            "half-orc": {
                "ability_scores": {
                    "dexterity": {
                        17: 7,
                        18: 8
                    }
                }
            }
        },
        "minimum_abilities": {
            "dexterity": 9,
        },
        "xp_bonus": {
            "dexterity": 16,
        }        
    }, 
    "assassin": {
        "races": {
            "pc": [
                "dwarf", 
                "elf", 
                "gnome", 
                "half-elf", 
                "half-orc", 
                "human"
            ],
            "npc": [
                "dwarf",
                "elf", 
                "gnome", 
                "half-elf", 
                "half-orc", 
                "human"
            ]
        },
        "level_limits": {
            "dwarf": 9,
            "elf": 10,
            "gnome": 8,
            "half-elf": 11,
            "half-orc": None,
            "human": None
        },
        "exceed_level_limits": {},
        "minimum_abilities": {
            "strength": 12,
            "intelligence": 11,
            "dexterity": 12
        },
        "xp_bonus": {}
    },  
    "monk": {
        "races": {
            "pc": [
                "human"
            ],
            "npc": [
                "human"
            ]
        },
        "level_limits": {
            "human": None
        },
        "exceed_level_limits": {},
        "minimum_abilities": {
            "strength": 15,
            "wisdom": 15,
            "dexterity": 15,
            "constitution": 11
        },
        "xp_bonus": {}
    }     
}

# Created 28/07/2026
FIRST_EDITION_RACE_LIST = (
    "dwarf",
    "elf",
    "gnome",
    "half-elf",
    "halfling",
    "half-orc",
    "human"
)

# Created 28/07/2026
# Modified 30/07/2026 to force order
FIRST_EDITION_CLASS_LIST = (
    "assassin",
    "cleric",
    "druid",
    "fighter",
    "illusionist",
    "magic-user",
    "monk",
    "paladin",
    "ranger",
    "thief"
)

# Created 28/07/2026

FEMININE_ABBREVIATION_LIST = (
    "f","fem","female","feminine","F","FEM","FEMALE","FEMININE"
)

MASCULINE_ABBREVIATION_LIST = (
    "m","mal","male","masculine","M","MAL","MALE","MASCULINE"
)


GENDER_ABBREVIATION_LIST = {
    "m" : "male",
    "f" : "female",
    
    "nb" : "nonbinary",
}

AFFIRMATIVES = (
    "y","Y","yes","YES","Yes"
    )

NEGATIVES = (
    "n","N","no","NO","No"
    )

"""
Created 31/07/2026
Wondered if a module that contains everything for each race might work better.
"""
FIRST_EDITION_RACES = {
    "dwarf": {
        "ability_limits": {
            "male": {                    
                "strength": {
                    "minimum": 8,
                    "maximum": 18
                },
                "intelligence": {
                    "minimum": 3,
                    "maximum": 18
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 18
                },
                "dexterity": {
                    "minimum": 3,
                    "maximum": 17
                },
                "constitution": {               
                    "minimum": 12,
                    "maximum": 19
                },
                "charisma": {
                    "minimum": 3,
                    "maximum": 16
                }
            },
            "female": {
                "strength": {
                    "minimum": 8,
                    "maximum": 17
                },
                "intelligence": {
                    "minimum": 3,
                    "maximum": 18
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 18
                },
                "dexterity": {
                    "minimum": 3,
                    "maximum": 17
                },
                "constitution": {               
                    "minimum": 12,
                    "maximum": 19
                },
                "charisma": {
                    "minimum": 3,
                    "maximum": 16
                }                
            }
        },
        "ability_modifiers": {
            "constitution": 1,
            "charisma": -1
        },
        "movement": 6,
        "infravision": 60,
        "languages": [
            "common",
            "dwarf",
            "gnome",
            "goblin",
            "kobold",
            "orc"
        ],
        "allowed_classes": {
            "pc": [
                "fighter",
                "thief",
                "assassin"
            ],
            "npc": [
                "cleric",
                "fighter",
                "thief",
                "assassin"
            ]
        }
    },
    "elf": {
        "ability_limits": {
            "male": {
                "strength": {
                    "minimum": 3,
                    "maximum": 18
                },
                "intelligence": {
                    "minimum": 8,
                    "maximum": 18
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 18
                },
                "dexterity": {
                    "minimum": 7,
                    "maximum": 19
                },
                "constitution": {               
                    "minimum": 6,
                    "maximum": 18
                },
                "charisma": {
                    "minimum": 8,
                    "maximum": 18
                }
            },
            "female": {
                "strength": {
                    "minimum": 3,
                    "maximum": 16
                },
                "intelligence": {
                    "minimum": 8,
                    "maximum": 18
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 18
                },
                "dexterity": {
                    "minimum": 7,
                    "maximum": 19
                },
                "constitution": {               
                    "minimum": 6,
                    "maximum": 18
                },
                "charisma": {
                    "minimum": 8,
                    "maximum": 18
                }                
            }
        },
        "ability_modifiers": {
            "dexterity": 1,
            "constitution": -1,
        },
        "movement": 12,
        "infravision": 60,
        "languages": [
            "common",
            "elf",
            "gnoll",
            "gnome",
            "goblin",
            "halfling",
            "hobgoblin",
            "orc",
        ],
        "allowed_classes": {
            "pc": [
                "fighter",
                "magic-user",
                "thief",
                "assassin"
            ],
            "npc": [
                "cleric",
                "fighter",
                "magic-user",
                "thief",
                "assassin"
            ],
        }
    },
    "gnome": {
        "ability_limits": {
            "male": {
                "strength": {
                    "minimum": 6,
                    "maximum": 18
                },
                "intelligence": {
                    "minimum": 7,
                    "maximum": 18
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 18
                },
                "dexterity": {
                    "minimum": 3,
                    "maximum": 18
                },
                "constitution": {               
                    "minimum": 8,
                    "maximum": 18
                },
                "charisma": {
                    "minimum": 3,
                    "maximum": 18
                }
            },
            "female": {
                "strength": {
                    "minimum": 6,
                    "maximum": 15
                },
                "intelligence": {
                    "minimum": 7,
                    "maximum": 18
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 18
                },
                "dexterity": {
                    "minimum": 3,
                    "maximum": 18
                },
                "constitution": {               
                    "minimum": 8,
                    "maximum": 18
                },
                "charisma": {
                    "minimum": 3,
                    "maximum": 18
                }                
            }
        },
        "ability_modifiers": { },
        "movement": 6,
        "infravision": 60,
        "languages": [
            "burrowing mammals",
            "common",
            "dwarf",
            "gnome",
            "goblin",
            "halfling",
            "kobold"
        ],
        "allowed_classes": {
            "pc": [
                "fighter",
                "illusionist",
                "thief",
                "assassin"
            ],
            "npc": [
                "cleric",
                "fighter",
                "illusionist",
                "thief",
                "assassin"                
            ]
        }
    },
    "half-elf": {
        "ability_limits": {
            "male": {
                "strength": {
                    "minimum": 3,
                    "maximum": 18
                },
                "intelligence": {
                    "minimum": 4,
                    "maximum": 18
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 18
                },
                "dexterity": {
                    "minimum": 6,
                    "maximum": 18
                },
                "constitution": {               
                    "minimum": 6,
                    "maximum": 18
                },
                "charisma": {
                    "minimum": 3,
                    "maximum": 18
                }
            },
            "female": {
                "strength": {
                    "minimum": 3,
                    "maximum": 17
                },
                "intelligence": {
                    "minimum": 4,
                    "maximum": 18
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 18
                },
                "dexterity": {
                    "minimum": 6,
                    "maximum": 18
                },
                "constitution": {               
                    "minimum": 6,
                    "maximum": 18
                },
                "charisma": {
                    "minimum": 3,
                    "maximum": 18
                }                
            }
        },
        "ability_modifiers": {
        },
        "movement": 12,
        "infravision": 60,
        "languages": [
            "common",
            "elvish",
            "gnoll",
            "gnome",
            "goblin",
            "hobgoblin",
            "orcish",
        ],
        "allowed_classes": {
            "pc": [
                "cleric",
                "druid",
                "fighter",
                "ranger",
                "magic-user",
                "thief",
                "assassin"
            ],
            "npc": [
                "cleric",
                "druid",
                "fighter",
                "ranger",
                "magic-user",
                "thief",
                "assassin"
            ],
        }
    },
    "halfling": {
        "ability_limits": {
            "male": {
                "strength": {
                    "minimum": 6,
                    "maximum": 17
                },
                "intelligence": {
                    "minimum": 6,
                    "maximum": 18
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 17
                },
                "dexterity": {
                    "minimum": 8,
                    "maximum": 18
                },
                "constitution": {               
                    "minimum": 10,
                    "maximum": 19
                },
                "charisma": {
                    "minimum": 3,
                    "maximum": 18
                }
            },
            "female": {
                "strength": {
                    "minimum": 6,
                    "maximum": 14
                },
                "intelligence": {
                    "minimum": 6,
                    "maximum": 18
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 17
                },
                "dexterity": {
                    "minimum": 8,
                    "maximum": 18
                },
                "constitution": {               
                    "minimum": 10,
                    "maximum": 19
                },
                "charisma": {
                    "minimum": 3,
                    "maximum": 18
                }                
            }
        },
        "ability_modifiers": {
            "strength": -1,
            "dexterity": 1
        },
        "movement": 6,
        "infravision": {
            "subrace": {
                "hairfoot": 0,
                "stout": 60,
                "tallfellow": 0
                }
            }
        },
        "languages": [
            "common",
            "dwarf",
            "elf",           
            "gnome",
            "goblin",
            "halfling",
            "orc",
        ],
        "allowed_classes": {
            "pc": [
                "fighter",
                "thief"
            ],
            "npc": [
                "fighter",
                "druid",
                "thief"
            ],            
    },
    "half-orc": {
        "ability_limits": {
            "male": {
                "strength": {
                    "minimum": 6,
                    "maximum": 18
                },
                "intelligence": {
                    "minimum": 3,
                    "maximum": 17
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 14
                },
                "dexterity": {
                    "minimum": 3,
                    "maximum": 17
                },
                "constitution": {               
                    "minimum": 13,
                    "maximum": 19
                },
                "charisma": {
                    "minimum": 3,
                    "maximum": 12
                }
            },
            "female": {
                "strength": {
                    "minimum": 6,
                    "maximum": 18
                },
                "intelligence": {
                    "minimum": 3,
                    "maximum": 17
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 14
                },
                "dexterity": {
                    "minimum": 3,
                    "maximum": 17
                },
                "constitution": {               
                    "minimum": 13,
                    "maximum": 19
                },
                "charisma": {
                    "minimum": 3,
                    "maximum": 12
                }                
            }
        },
        "ability_modifiers": {
            "strength": 1,
            "constitution": 1,
            "charisma": -2
        },
        "movement": 12,
        "infravision": 60,
        "languages": [
            "common",
            "orcish",
        ],
        "allowed_classes": {
            "pc": [
                "cleric",
                "fighter",
                "thief",
                "assassin"
            ],
            "npc": [
                "cleric",
                "fighter",
                "thief",
                "assassin"
            ]
        }
    },
    "human": {
        "ability_limits": {
            "male": {
                "strength": {
                    "minimum": 3,
                    "maximum": 18
                },
                "intelligence": {
                    "minimum": 3,
                    "maximum": 18
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 18
                },
                "dexterity": {
                    "minimum": 3,
                    "maximum": 18
                },
                "constitution": {               
                    "minimum": 13,
                    "maximum": 18
                },
                "charisma": {
                    "minimum": 3,
                    "maximum": 18
                }
            },
            "female": {
                "strength": {
                    "minimum": 3,
                    "maximum": 18
                },
                "intelligence": {
                    "minimum": 3,
                    "maximum": 18
                },
                "wisdom": {
                    "minimum": 3,
                    "maximum": 18
                },
                "dexterity": {
                    "minimum": 3,
                    "maximum": 18
                },
                "constitution": {               
                    "minimum": 13,
                    "maximum": 18
                },
                "charisma": {
                    "minimum": 3,
                    "maximum": 18
                }                
            }
        },
        "ability_modifiers": { },
        "movement": 12,
        "infravision": 0,
        "languages": [ ],
        "allowed_classes": {
            "pc": [
                "cleric",
                "druid",
                "fighter",
                "ranger",
                "paladin",
                "magic-user",
                "illusionist",
                "thief",
                "assassin",
                "monk"
            ],
            "npc": [
                "cleric",
                "druid",
                "fighter",
                "ranger",
                "paladin",
                "magic-user",
                "illusionist",
                "thief",
                "assassin",
                "monk"
            ]
        }
    }    
}


