"""
================================================================
BACKEND CONCEPTS - PART 1: Object-Oriented Programming (OOPs)
================================================================
Complete Beginner Guide with Python Examples

================================================================
SECTION 1: WHAT IS OOP?
================================================================

OOP = Object-Oriented Programming
A way to organize code using "objects" that contain BOTH:
  - DATA (attributes/properties)
  - BEHAVIOR (methods/functions)

Real-world analogy:
  Think of a CAR:
    - Data: color, brand, speed, fuel_level
    - Behavior: start(), accelerate(), brake(), refuel()

WHY USE OOP?
  1. ORGANIZED CODE - Group related data and functions together
  2. REUSABLE - Create templates (classes) and reuse them
  3. MAINTAINABLE - Change one class without breaking others
  4. MODELS REAL WORLD - Easy to think about

4 PILLARS OF OOP:
  1. Encapsulation
  2. Abstraction
  3. Inheritance
  4. Polymorphism


================================================================
SECTION 2: CLASS AND OBJECT
================================================================

CLASS = A blueprint/template for creating objects.
  Think: "cookie cutter" - defines the SHAPE

OBJECT = An instance of a class.
  Think: "cookie" - an actual thing created from the template

One class can create MANY objects, each with different data.
"""


# ============================================================
# Basic Class Definition
# ============================================================
class Car:
    """A simple Car class - this is the BLUEPRINT."""
    
    # CLASS VARIABLE: shared by ALL instances
    total_cars = 0
    
    def __init__(self, brand, color, speed=0):
        """
        CONSTRUCTOR: Called automatically when creating an object.
        __init__ sets up the object's initial state.
        
        self = reference to the current object being created
        """
        # INSTANCE VARIABLES: unique to each object
        self.brand = brand
        self.color = color
        self.speed = speed
        self.is_running = False
        
        Car.total_cars += 1  # increment class variable
    
    def start(self):
        """Method: a function that belongs to the class."""
        self.is_running = True
        print(f"{self.brand} started!")
    
    def accelerate(self, amount):
        if self.is_running:
            self.speed += amount
            print(f"{self.brand} speed: {self.speed} km/h")
        else:
            print("Start the car first!")
    
    def brake(self):
        self.speed = max(0, self.speed - 20)
        print(f"{self.brand} braking. Speed: {self.speed} km/h")
    
    def __str__(self):
        """String representation (like toString in Java)."""
        return f"{self.color} {self.brand} (speed: {self.speed})"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"Car('{self.brand}', '{self.color}', {self.speed})"


# Creating OBJECTS (instances) from the class:
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print("--- Class and Object ---")
car1.start()
car1.accelerate(60)
print(car1)                  # calls __str__
print(f"Total cars: {Car.total_cars}")  # 2


"""
================================================================
SECTION 3: THE 4 PILLARS OF OOP
================================================================


PILLAR 1: ENCAPSULATION
========================

Encapsulation = BUNDLING data + methods together
AND HIDING internal details from outside.

Access Modifiers in Python:
  public:     self.name        (accessible from anywhere)
  protected:  self._name       (convention: don't access directly)
  private:    self.__name      (name mangling: harder to access)

WHY? To protect data from accidental modification.
"""


class BankAccount:
    """Example of Encapsulation."""
    
    def __init__(self, owner, balance=0):
        self.owner = owner          # public
        self._account_type = "Savings"  # protected (convention)
        self.__balance = balance    # private (name mangled)
    
    # GETTER - controlled way to READ private data
    def get_balance(self):
        return self.__balance
    
    # SETTER - controlled way to MODIFY private data
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. Balance: {self.__balance}")
        else:
            print("Invalid amount!")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount!")
    
    # Python PROPERTY decorator (pythonic way for getters/setters)
    @property
    def balance(self):
        """Getter using property decorator."""
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        """Setter using property decorator."""
        if value >= 0:
            self.__balance = value
        else:
            raise ValueError("Balance cannot be negative!")


print("\n--- Encapsulation ---")
account = BankAccount("Alice", 1000)
account.deposit(500)          # Controlled access
account.withdraw(200)
print(f"Balance: {account.balance}")   # Using property
# account.__balance              # ERROR! Private attribute


"""
PILLAR 2: INHERITANCE
========================

Inheritance = Creating a NEW class from an EXISTING class.
The new class (child) INHERITS all attributes and methods of
the parent class, and can ADD or OVERRIDE them.

WHY? Code reuse! Don't rewrite common functionality.

         Animal (Parent/Base/Super class)
        /      \
     Dog        Cat (Child/Derived/Sub class)
    /    \
 Labrador  Poodle (Multi-level inheritance)
"""


class Animal:
    """Parent class."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        return f"{self.name} makes a sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"


class Dog(Animal):
    """Child class - inherits from Animal."""
    
    def __init__(self, name, breed):
        # Call parent's __init__
        super().__init__(name, species="Dog")
        self.breed = breed  # new attribute specific to Dog
    
    def speak(self):
        """OVERRIDE parent's method."""
        return f"{self.name} says Woof!"
    
    def fetch(self):
        """NEW method specific to Dog."""
        return f"{self.name} fetches the ball!"


class Cat(Animal):
    """Another child class."""
    
    def __init__(self, name):
        super().__init__(name, species="Cat")
    
    def speak(self):
        return f"{self.name} says Meow!"


print("\n--- Inheritance ---")
dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers")

print(dog.speak())     # Woof! (overridden method)
print(cat.speak())     # Meow! (overridden method)
print(dog.info())      # inherited from Animal
print(dog.fetch())     # Dog-specific method
print(f"Is Dog an Animal? {isinstance(dog, Animal)}")  # True


# --- Multiple Inheritance ---
class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Animal, Flyable, Swimmable):
    """Inherits from multiple classes."""
    def __init__(self, name):
        super().__init__(name, "Duck")
    
    def speak(self):
        return f"{self.name} says Quack!"

duck = Duck("Donald")
print(f"\n{duck.speak()}, {duck.fly()}, {duck.swim()}")


"""
PILLAR 3: POLYMORPHISM
========================

Polymorphism = "Many forms"
Same method name, DIFFERENT behavior depending on the object.

Already seen above: speak() behaves differently for Dog, Cat, Duck.
"""


print("\n--- Polymorphism ---")
animals = [Dog("Rex", "German Shepherd"), Cat("Tom"), Duck("Daffy")]

# Same method call, different behavior for each type!
for animal in animals:
    print(f"  {animal.speak()}")


# --- Operator Overloading (another form of polymorphism) ---
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        """Overload == operator."""
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # uses __add__
print(f"\n{v1} + {v2} = {v3}")  # Vector(4, 6)


"""
PILLAR 4: ABSTRACTION
========================

Abstraction = HIDE complex implementation, show only ESSENTIAL features.

Like driving a car:
  - You use steering wheel, pedals, gear (interface)
  - You don't need to know how the engine works (hidden complexity)

In Python: Use Abstract Base Classes (ABC).
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class - CANNOT be instantiated directly."""
    
    @abstractmethod
    def area(self):
        """Every shape MUST implement this."""
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def description(self):
        """Concrete method - shared by all shapes."""
        return f"I am a shape with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


print("\n--- Abstraction ---")
# shape = Shape()  # ERROR! Can't instantiate abstract class
circle = Circle(5)
rect = Rectangle(4, 6)
print(circle.description())
print(f"Rectangle area: {rect.area()}, perimeter: {rect.perimeter()}")


"""
================================================================
SECTION 4: OTHER IMPORTANT OOP CONCEPTS
================================================================
"""


# --- Static Methods and Class Methods ---
class MathUtils:
    pi = 3.14159
    
    @staticmethod
    def add(a, b):
        """Static method: no access to instance or class. Just a utility."""
        return a + b
    
    @classmethod
    def circle_area(cls, radius):
        """Class method: has access to class (cls), not instance."""
        return cls.pi * radius ** 2

print("\n--- Static & Class Methods ---")
print(f"Add: {MathUtils.add(3, 5)}")
print(f"Circle area: {MathUtils.circle_area(5)}")


# --- Composition (HAS-A relationship) ---
"""
Inheritance = IS-A relationship (Dog IS AN Animal)
Composition = HAS-A relationship (Car HAS AN Engine)

Often, composition is PREFERRED over inheritance.
  "Favor composition over inheritance" - common design principle.
"""

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine started!"

class SportsCar:
    def __init__(self, brand, hp):
        self.brand = brand
        self.engine = Engine(hp)  # HAS-A Engine (composition)
    
    def start(self):
        return f"{self.brand}: {self.engine.start()} ({self.engine.horsepower}HP)"

print("\n--- Composition ---")
ferrari = SportsCar("Ferrari", 500)
print(ferrari.start())


"""
================================================================
SECTION 5: SOLID PRINCIPLES (Interview Favorite!)
================================================================

S - Single Responsibility Principle
    A class should have only ONE reason to change.
    
O - Open/Closed Principle
    Open for extension, closed for modification.
    (Add new behavior by adding new classes, not modifying existing)
    
L - Liskov Substitution Principle
    Child class should be usable wherever parent class is expected.
    
I - Interface Segregation Principle
    Don't force clients to depend on methods they don't use.
    (Many small interfaces > one big interface)
    
D - Dependency Inversion Principle
    Depend on abstractions, not concrete implementations.


================================================================
SECTION 6: DESIGN PATTERNS (Common Interview Questions)
================================================================

1. SINGLETON: Only one instance of a class exists.
"""

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(f"\n--- Singleton ---")
print(f"Same object? {s1 is s2}")  # True


"""
2. FACTORY: Create objects without specifying exact class.
3. OBSERVER: When one object changes, notify all dependents.
4. STRATEGY: Define a family of algorithms, make them interchangeable.

These are commonly asked in interviews - understand the concept.


================================================================
SUMMARY
================================================================

4 PILLARS:
  1. Encapsulation:  Bundle data + methods, hide internals
  2. Inheritance:    Create new class from existing (IS-A)
  3. Polymorphism:   Same interface, different behavior
  4. Abstraction:    Hide complexity, show essentials

KEY CONCEPTS:
  - Class vs Object (blueprint vs instance)
  - Constructor (__init__)
  - self keyword
  - Access modifiers (public, _protected, __private)
  - @property, @staticmethod, @classmethod
  - Composition vs Inheritance (HAS-A vs IS-A)
  - SOLID principles
  - Design patterns (Singleton, Factory, Observer)
"""
