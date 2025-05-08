from dog import Dog
from cat import Cat

if __name__ == "__main__":
    # Create instances
    dog = Dog("Buddy", "Woof")
    cat = Cat("Whiskers", "Meow")

    # Demonstrate functionality
    print("--- Dog ---")
    dog.get_sound()

    print("\n--- Cat ---")
    cat.get_sound()