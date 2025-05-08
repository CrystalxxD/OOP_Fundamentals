class CreateCharacter:
    VALID_CLASSES = ['warrior', 'wizard', 'archer', 'rogue', 'cleric']
    
    def __init__(self, name, classtype, level=1):
        self.__name = name
        self.__classtype = classtype.lower()
        self.__level = level
        
        # Validate inputs
        if not isinstance(self.__name, str) or len(self.__name.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        if self.__classtype not in self.VALID_CLASSES:
            raise ValueError(f"Class must be one of: {', '.join(self.VALID_CLASSES)}")
        if not isinstance(self.__level, int) or self.__level < 1:
            raise ValueError("Level must be a positive integer")

    # Getter methods
    def get_name(self):
        return self.__name
    
    def get_classtype(self):
        return self.__classtype
    
    def get_level(self):
        return self.__level

    # Setter methods
    def set_name(self, new_name):
        if not isinstance(new_name, str) or len(new_name.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        self.__name = new_name.strip()

    def set_classtype(self, new_classtype):
        new_classtype = new_classtype.lower()
        if new_classtype not in self.VALID_CLASSES:
            raise ValueError(f"Class must be one of: {', '.join(self.VALID_CLASSES)}")
        self.__classtype = new_classtype

    def set_level(self, new_level):
        if not isinstance(new_level, int) or new_level < 1:
            raise ValueError("Level must be a positive integer")
        self.__level = new_level

    def level_up(self):
        self.__level += 1
        return self.__level

    def __str__(self):
        return (f"Character: {self.__name}\n"
                f"Class: {self.__classtype.capitalize()}\n"
                f"Level: {self.__level}")