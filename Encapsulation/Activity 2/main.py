from create_character import CreateCharacter

def test_character_system():
    print("Character Creation System Test\n")
    
    # Test first character
    print("Testing Character 1:")
    try:
        char1 = CreateCharacter("Aragorn", "warrior", 5)
        print("\nCharacter created successfully:")
        print(char1)
        
        # Test getters
        print("\nTesting getters:")
        print("Name:", char1.get_name())
        print("Class:", char1.get_classtype())
        print("Level:", char1.get_level())
        
        # Test setters
        print("\nChanging name to 'Strider'...")
        char1.set_name("Strider")
        print("New name:", char1.get_name())
        
        print("\nLeveling up...")
        char1.level_up()
        print("New level:", char1.get_level())
        
        # Test invalid class
        print("\nAttempting to set invalid class 'dragon'...")
        try:
            char1.set_classtype("dragon")
        except ValueError as e:
            print("Error:", e)
        
    except ValueError as e:
        print("Error creating character:", e)

    # Test second character
    print("\nTesting Character 2:")
    try:
        char2 = CreateCharacter("Gandalf", "wizard", 10)
        print("\nCharacter created successfully:")
        print(char2)
        
        # Test getters
        print("\nTesting getters:")
        print("Name:", char2.get_name())
        print("Class:", char2.get_class_type())
        print("Level:", char2.get_level())
        
        # Test setters
        print("\nChanging class to 'cleric'...")
        char2.set_classtype("cleric")
        print("New class:", char2.get_class_type())
        
        print("\nSetting level to 15...")
        char2.set_level(15)
        print("New level:", char2.get_level())
        
        # Test invalid level
        print("\nAttempting to set level to 0...")
        try:
            char2.set_level(0)
        except ValueError as e:
            print("Error:", e)
        
    except ValueError as e:
        print("Error creating character:", e)

    # Test character creation with invalid parameters
    print("\nTesting invalid character creation:")
    print("Attempting to create character with empty name...")
    try:
        bad_char = CreateCharacter("", "archer")
    except ValueError as e:
        print("Error:", e)

def main():
    test_character_system()
    print("\nAll tests completed.")

if __name__ == "__main__":
    main()