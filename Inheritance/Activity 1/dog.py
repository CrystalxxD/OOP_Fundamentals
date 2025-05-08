from animal import Animal

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self._sound = sound
    
    def get_sound(self):
        super().get_sound()  # Call parent's method
        print(f"{self._name} the dog says {self._sound}!")