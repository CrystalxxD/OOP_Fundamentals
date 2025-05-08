from weapons import Weapon, Sword, Bow, Longbow, Shortbow

def create_weapon():
    print("\nCreate a new weapon:")
    print("1. Generic Weapon")
    print("2. Sword")
    print("3. Bow")
    print("4. Longbow")
    print("5. Shortbow")
    
    choice = input("Choose weapon type (1-5): ")
    name = input("Enter weapon name: ")
    damage = int(input("Enter damage: "))
    
    if choice == "1":
        category = input("Enter weapon category: ")
        return Weapon(name, category, damage)
    elif choice == "2":
        damage_type = input("Enter damage type (default: Slashing): ") or "Slashing"
        return Sword(name, damage, damage_type)
    elif choice == "3":
        damage_type = input("Enter damage type (default: Piercing): ") or "Piercing"
        return Bow(name, damage, damage_type)
    elif choice == "4":
        bow_range = int(input("Enter range (default: 150): ") or 150)
        return Longbow(name, damage, bow_range)
    elif choice == "5":
        bow_range = int(input("Enter range (default: 80): ") or 80)
        return Shortbow(name, damage, bow_range)
    else:
        print("Invalid choice!")
        return None

def main():
    inventory = []
    
    # Pre-populate with some weapons
    inventory.append(Sword("Excalibur", 15))
    inventory.append(Bow("Robin's Bow", 10))
    inventory.append(Longbow("Elven Longbow", 12))
    inventory.append(Shortbow("Goblin Shortbow", 8))
    
    while True:
        print("\nWeapon Inventory System")
        print("1. Add new weapon")
        print("2. View all weapons")
        print("3. Search weapons")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            weapon = create_weapon()
            if weapon:
                inventory.append(weapon)
                print(f"{weapon.name} added to inventory!")
        elif choice == "2":
            print("\nAll Weapons:")
            for i, weapon in enumerate(inventory, 1):
                print(f"\nWeapon #{i}:")
                weapon.get_stats()
        elif choice == "3":
            search_term = input("Enter weapon name to search: ").lower()
            found = [w for w in inventory if search_term in w.name.lower()]
            if found:
                print("\nSearch Results:")
                for weapon in found:
                    weapon.get_stats()
                    print("---")
            else:
                print("No weapons found!")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()