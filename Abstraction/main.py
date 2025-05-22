from shapey import Circle, Rectangle, Square

def test_circle():
    print("Testing Circle:")
    circle = Circle(5)
    print(f"Perimeter: {circle.perimeter():.2f}")
    print(f"Area: {circle.area():.2f}")
    print(f"Volume (sphere): {circle.volume():.2f}")
    print()

def test_rectangle():
    print("Testing Rectangle:")
    rectangle = Rectangle(4, 6)
    print(f"Perimeter: {rectangle.perimeter()}")
    print(f"Area: {rectangle.area()}")
    print(f"Volume (with height 3): {rectangle.volume(3)}")
    print()

def test_square():
    print("Testing Square:")
    square = Square(4)
    print(f"Perimeter: {square.perimeter()}")
    print(f"Area: {square.area()}")
    print(f"Volume (cube): {square.volume()}")
    print(f"Volume (with height 2): {square.volume(2)}")
    print()

if __name__ == "__main__":
    test_circle()
    test_rectangle()
    test_square()