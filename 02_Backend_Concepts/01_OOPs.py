"""
================================================================================
OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON - COMPLETE BEGINNER'S GUIDE
================================================================================

This guide assumes you have ZERO knowledge of OOP. We'll build from the ground up.

================================================================================
CHAPTER 1: WHAT IS OBJECT-ORIENTED PROGRAMMING?
================================================================================

Before OOP, we wrote code like this (Procedural Programming):
-----------------------------------------------------------------

    name = "Alice"
    age = 25
    email = "alice@example.com"
    
    def send_email(email, message):
        print(f"Sending to {email}: {message}")
    
    send_email(email, "Hello!")

PROBLEM: As programs grow, we have hundreds of variables and functions floating 
around. Hard to organize! Which variables belong together? Which functions work 
with which data?

SOLUTION: Object-Oriented Programming (OOP)
-----------------------------------------------------------------

OOP says: "Let's GROUP related data and functions TOGETHER into a single unit 
called an OBJECT."

Think of real-world objects:
    
    A CAR object has:
        - DATA (properties): color, brand, speed, fuel_level
        - ACTIONS (methods): start(), accelerate(), brake(), refuel()
    
    A PERSON object has:
        - DATA: name, age, email, address
        - ACTIONS: send_email(), celebrate_birthday(), move()

WHY IS THIS BETTER?
    ✓ ORGANIZED: Related things are grouped together
    ✓ REUSABLE: Create templates and reuse them
    ✓ MAINTAINABLE: Changes in one place don't break everything
    ✓ INTUITIVE: Mirrors how we think about the real world


THE 4 PILLARS OF OOP (We'll cover each in detail):
    1. ENCAPSULATION  - Bundle data + methods, hide internal details
    2. INHERITANCE    - Create new classes from existing ones
    3. POLYMORPHISM   - Same method name, different behaviors
    4. ABSTRACTION    - Hide complexity, show only essentials


================================================================================
CHAPTER 2: CLASSES AND OBJECTS - THE FOUNDATION
================================================================================

WHAT IS A CLASS?
-----------------------------------------------------------------

A CLASS is a BLUEPRINT or TEMPLATE for creating objects.

Think of it like:
    - An architectural blueprint for a house
    - A cookie cutter shape
    - A car manufacturing design

The class DEFINES:
    - What DATA each object will have (attributes/properties)
    - What ACTIONS each object can perform (methods/functions)

Example: A "Dog" class might define:
    - Data: name, breed, age, color
    - Actions: bark(), eat(), sleep(), play()


WHAT IS AN OBJECT?
-----------------------------------------------------------------

An OBJECT is a SPECIFIC INSTANCE created from a class.

Think of it like:
    - An actual house built from the blueprint
    - An actual cookie made from the cookie cutter
    - An actual car manufactured from the design

Example: From the "Dog" class, we can create:
    - dog1 = Dog with name="Buddy", breed="Labrador", age=3
    - dog2 = Dog with name="Max", breed="Poodle", age=5
    - dog3 = Dog with name="Charlie", breed="Beagle", age=2

ONE class can create UNLIMITED objects, each with DIFFERENT data!


KEY TERMINOLOGY:
-----------------------------------------------------------------
    CLASS      = Blueprint/Template (the design)
    OBJECT     = Instance (actual thing created from the blueprint)
    ATTRIBUTE  = Data/Property stored in an object (name, age, color)
    METHOD     = Function that belongs to a class (bark(), eat())
    INSTANCE   = Another word for object


================================================================================
CHAPTER 3: CREATING YOUR FIRST CLASS - STEP BY STEP
================================================================================
"""


# ============================================================
# STEP 1: The Simplest Possible Class
# ============================================================

# Let's start with the ABSOLUTE BASICS - an empty class
class Dog:
    pass  # 'pass' means "do nothing, just a placeholder"

# Creating an object from this class:
my_dog = Dog()

print("=" * 80)
print("STEP 1: Simplest Class")
print("=" * 80)
print(f"my_dog is an object of type: {type(my_dog)}")
print(f"Memory address of my_dog: {id(my_dog)}")
print()

"""
WHAT JUST HAPPENED?
-------------------
1. We DEFINED a class called 'Dog' (the blueprint)
2. We CREATED an object called 'my_dog' using Dog()
3. Python allocated memory for this object
4. The variable 'my_dog' stores a REFERENCE (memory address) to that object

MEMORY VISUALIZATION:
---------------------
    
    STACK (stores variable names)          HEAP (stores actual objects)
    ┌─────────────────────┐               ┌──────────────────────┐
    │  my_dog  ───────────┼──────────────>│  Dog object          │
    │  (reference/pointer)│               │  at memory: 0x7f8... │
    └─────────────────────┘               └──────────────────────┘

The variable 'my_dog' doesn't contain the object itself.
It contains the MEMORY ADDRESS (reference) pointing to where the object lives.
"""


# ============================================================
# STEP 2: Adding Attributes (Data) to the Class
# ============================================================

class Dog:
    """A Dog class with attributes."""
    
    def __init__(self, name, breed, age):
        """
        __init__ is the CONSTRUCTOR (also called INITIALIZER)
        
        WHEN IS IT CALLED?
        - Automatically called when you create a new object: Dog("Buddy", "Labrador", 3)
        
        WHAT DOES IT DO?
        - Sets up the initial state of the object
        - Assigns values to the object's attributes
        
        PARAMETERS:
        - self: Reference to the object being created (Python passes this automatically)
        - name, breed, age: Values we want to store in this specific dog object
        """
        self.name = name      # self.name means "this object's name attribute"
        self.breed = breed    # self.breed means "this object's breed attribute"
        self.age = age        # self.age means "this object's age attribute"

# Creating multiple dog objects:
dog1 = Dog("Buddy", "Labrador", 3)
dog2 = Dog("Max", "Poodle", 5)
dog3 = Dog("Charlie", "Beagle", 2)

print("=" * 80)
print("STEP 2: Class with Attributes")
print("=" * 80)
print(f"Dog 1: {dog1.name}, {dog1.breed}, {dog1.age} years old")
print(f"Dog 2: {dog2.name}, {dog2.breed}, {dog2.age} years old")
print(f"Dog 3: {dog3.name}, {dog3.breed}, {dog3.age} years old")
print()

"""
WHAT IS 'self'?
---------------
'self' is a reference to the CURRENT OBJECT.

When you write:
    dog1 = Dog("Buddy", "Labrador", 3)

Python internally does this:
    1. Creates a new Dog object in memory
    2. Calls __init__(newly_created_object, "Buddy", "Labrador", 3)
    3. Inside __init__, 'self' refers to that newly_created_object
    4. self.name = "Buddy" means: "Store 'Buddy' in THIS object's name attribute"

WHY IS IT CALLED 'self'?
- It's just a convention! You could call it 'this' or 'obj' or anything.
- But EVERYONE uses 'self' in Python, so stick with it.


MEMORY VISUALIZATION AFTER CREATING 3 DOGS:
--------------------------------------------

STACK                           HEAP
┌──────────────┐               ┌─────────────────────────┐
│ dog1 ────────┼──────────────>│ Dog object at 0x1000    │
│              │               │   name = "Buddy"        │
│              │               │   breed = "Labrador"    │
│              │               │   age = 3               │
└──────────────┘               └─────────────────────────┘
                               
┌──────────────┐               ┌─────────────────────────┐
│ dog2 ────────┼──────────────>│ Dog object at 0x2000    │
│              │               │   name = "Max"          │
│              │               │   breed = "Poodle"      │
│              │               │   age = 5               │
└──────────────┘               └─────────────────────────┘
                               
┌──────────────┐               ┌─────────────────────────┐
│ dog3 ────────┼──────────────>│ Dog object at 0x3000    │
│              │               │   name = "Charlie"      │
│              │               │   breed = "Beagle"      │
│              │               │   age = 2               │
└──────────────┘               └─────────────────────────┘

Each object is SEPARATE in memory with its OWN copy of the attributes!
"""


# ============================================================
# STEP 3: Adding Methods (Behavior) to the Class
# ============================================================

class Dog:
    """A Dog class with attributes AND methods."""
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.energy = 100  # All dogs start with full energy
    
    def bark(self):
        """A method (function that belongs to the class)."""
        print(f"{self.name} says: Woof! Woof!")
    
    def play(self, minutes):
        """Method that modifies the object's state."""
        self.energy -= minutes * 2
        if self.energy < 0:
            self.energy = 0
        print(f"{self.name} played for {minutes} minutes. Energy: {self.energy}")
    
    def sleep(self, hours):
        """Method that restores energy."""
        self.energy += hours * 10
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} slept for {hours} hours. Energy: {self.energy}")
    
    def get_info(self):
        """Method that returns information about the dog."""
        return f"{self.name} is a {self.age}-year-old {self.breed} with {self.energy} energy"

# Using methods:
dog = Dog("Buddy", "Labrador", 3)

print("=" * 80)
print("STEP 3: Class with Methods")
print("=" * 80)
print(dog.get_info())
dog.bark()
dog.play(20)
dog.sleep(5)
print(dog.get_info())
print()

"""
WHAT ARE METHODS?
-----------------
Methods are FUNCTIONS that belong to a class.

Key differences from regular functions:
    1. Defined INSIDE a class
    2. First parameter is ALWAYS 'self' (reference to the object)
    3. Can access and modify the object's attributes using 'self'

When you call:
    dog.bark()

Python internally does:
    Dog.bark(dog)  # Passes 'dog' as the 'self' parameter

This is why methods always have 'self' as the first parameter!


MEMORY IMPACT OF METHOD CALLS:
-------------------------------

When you call dog.play(20):
    1. Python finds the 'play' method in the Dog class
    2. Passes 'dog' as 'self' and 20 as 'minutes'
    3. Inside play(), self.energy -= 40 modifies the object's energy attribute
    4. The change is PERMANENT - it modifies the object in memory

Before: dog.energy = 100
After:  dog.energy = 60  (100 - 40)

The object in the HEAP is modified directly!
"""


# ============================================================
# STEP 4: Class Variables vs Instance Variables
# ============================================================

class Dog:
    """Dog class demonstrating class vs instance variables."""
    
    # CLASS VARIABLE: Shared by ALL instances of the class
    species = "Canis familiaris"  # All dogs are the same species
    total_dogs = 0                # Counter for total dogs created
    
    def __init__(self, name, breed, age):
        # INSTANCE VARIABLES: Unique to each object
        self.name = name
        self.breed = breed
        self.age = age
        
        # Increment the class variable when a new dog is created
        Dog.total_dogs += 1
    
    def bark(self):
        print(f"{self.name} says: Woof!")
    
    @classmethod
    def get_total_dogs(cls):
        """Class method: works with class variables, not instance variables."""
        return f"Total dogs created: {cls.total_dogs}"
    
    @staticmethod
    def is_good_boy():
        """Static method: doesn't access class or instance variables."""
        return "Yes! All dogs are good boys/girls!"

# Creating dogs:
dog1 = Dog("Buddy", "Labrador", 3)
dog2 = Dog("Max", "Poodle", 5)
dog3 = Dog("Charlie", "Beagle", 2)

print("=" * 80)
print("STEP 4: Class Variables vs Instance Variables")
print("=" * 80)
print(f"Dog1 name (instance var): {dog1.name}")
print(f"Dog1 species (class var): {dog1.species}")
print(f"Dog2 species (class var): {dog2.species}")
print(f"All dogs share same species: {dog1.species == dog2.species == dog3.species}")
print(Dog.get_total_dogs())
print(Dog.is_good_boy())
print()

"""
CLASS VARIABLES vs INSTANCE VARIABLES:
--------------------------------------

INSTANCE VARIABLES (self.variable_name):
    - Unique to EACH object
    - Created in __init__ using 'self'
    - Each object has its OWN copy
    - Example: self.name, self.age, self.breed

CLASS VARIABLES (defined at class level):
    - SHARED by ALL objects of the class
    - Defined outside __init__, at the class level
    - Only ONE copy exists, shared by all instances
    - Example: species, total_dogs


MEMORY VISUALIZATION:
---------------------

CLASS LEVEL (shared by all)
┌─────────────────────────────┐
│ Dog class                   │
│   species = "Canis..."      │  ← ONE copy, shared by all
│   total_dogs = 3            │  ← ONE copy, shared by all
└─────────────────────────────┘
         ↑           ↑           ↑
         │           │           │
    ┌────┴───┐  ┌───┴────┐  ┌───┴────┐
    │ dog1   │  │ dog2   │  │ dog3   │  ← All point to same class variables
    │ name="Buddy" │ name="Max" │ name="Charlie"
    │ breed="Lab"  │ breed="Poodle" │ breed="Beagle"
    │ age=3   │  │ age=5  │  │ age=2  │  ← Each has own instance variables
    └────────┘  └────────┘  └────────┘


WHEN TO USE WHICH?
------------------
Use INSTANCE variables when: Each object needs its own value (name, age, color)
Use CLASS variables when: All objects share the same value (species, constants)


TYPES OF METHODS:
-----------------

1. INSTANCE METHOD (regular method):
   - Has 'self' as first parameter
   - Can access instance variables (self.name) and class variables (Dog.species)
   - Example: def bark(self)

2. CLASS METHOD (@classmethod):
   - Has 'cls' as first parameter (reference to the class, not instance)
   - Can access class variables, but NOT instance variables
   - Called on class: Dog.get_total_dogs()
   - Example: @classmethod def get_total_dogs(cls)

3. STATIC METHOD (@staticmethod):
   - No 'self' or 'cls' parameter
   - Cannot access instance or class variables
   - Just a regular function that logically belongs to the class
   - Example: @staticmethod def is_good_boy()
"""


"""
================================================================================
CHAPTER 4: THE 4 PILLARS OF OOP
================================================================================

Now that you understand classes and objects, let's learn the 4 fundamental 
principles that make OOP powerful.


================================================================================
PILLAR 1: ENCAPSULATION
================================================================================

WHAT IS ENCAPSULATION?
----------------------

Encapsulation means TWO things:
    1. BUNDLING data and methods together in a class
    2. HIDING internal details and controlling access to data

Think of a CAPSULE (medicine pill):
    - The medicine is INSIDE the capsule (hidden)
    - You can't directly touch the medicine
    - You take the whole capsule (controlled access)

Real-world example: A TV Remote
    - HIDDEN: Complex circuitry, infrared signals, battery connections
    - EXPOSED: Simple buttons (power, volume, channel)
    - You don't need to know HOW it works, just WHAT buttons to press


WHY DO WE NEED ENCAPSULATION?
------------------------------

Without encapsulation:
    account_balance = 1000
    account_balance = -500  # Oops! Negative balance! No validation!

With encapsulation:
    account.set_balance(-500)  # Method checks: "Error! Can't be negative!"


ACCESS MODIFIERS IN PYTHON:
----------------------------

Python has 3 levels of access control (using naming conventions):

1. PUBLIC (no underscore):
   - Accessible from ANYWHERE
   - Example: self.name
   - Use for: Data that's safe to access/modify directly

2. PROTECTED (single underscore _):
   - Convention: "Please don't access directly, but you CAN if needed"
   - Example: self._account_type
   - Use for: Internal implementation details
   - Note: Not enforced by Python, just a convention!

3. PRIVATE (double underscore __):
   - Name mangling: Python makes it harder to access
   - Example: self.__balance
   - Use for: Sensitive data that should NEVER be accessed directly
   - Accessed through getter/setter methods


Let's see encapsulation in action:
"""


class BankAccount:
    """
    Example of Encapsulation.
    
    We want to protect the balance from invalid modifications.
    Users should NOT be able to set balance to negative values!
    """
    
    def __init__(self, owner, balance=0):
        self.owner = owner                    # PUBLIC: Anyone can access
        self._account_type = "Savings"        # PROTECTED: Convention - don't access directly
        self.__balance = balance              # PRIVATE: Cannot access directly
        self.__transaction_history = []       # PRIVATE: Internal data
    
    def get_balance(self):
        """GETTER method: Controlled way to READ private data."""
        return self.__balance
    
    def deposit(self, amount):
        """SETTER method: Controlled way to MODIFY private data with validation."""
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposited: {amount}")
            print(f"✓ Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("✗ Invalid amount! Must be positive.")
    
    def withdraw(self, amount):
        """Another SETTER method with business logic."""
        if amount <= 0:
            print("✗ Invalid amount! Must be positive.")
        elif amount > self.__balance:
            print(f"✗ Insufficient funds! You have ${self.__balance}")
        else:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrew: {amount}")
            print(f"✓ Withdrew ${amount}. New balance: ${self.__balance}")
    
    def get_transaction_history(self):
        """Controlled access to private transaction history."""
        return self.__transaction_history.copy()  # Return a copy, not the original!
    
    @property
    def balance(self):
        """
        PROPERTY decorator: Pythonic way to create getters.
        Now you can use: account.balance (instead of account.get_balance())
        """
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        """
        PROPERTY SETTER: Pythonic way to create setters.
        Now you can use: account.balance = 500
        """
        if value >= 0:
            self.__balance = value
            self.__transaction_history.append(f"Balance set to: {value}")
        else:
            raise ValueError("Balance cannot be negative!")


print("=" * 80)
print("PILLAR 1: ENCAPSULATION")
print("=" * 80)

account = BankAccount("Alice", 1000)

print(f"Owner (public): {account.owner}")

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)

print(f"Balance using property: ${account.balance}")

print("\nTransaction History:")
for transaction in account.get_transaction_history():
    print(f"  - {transaction}")

print("\n--- Trying to access private variables ---")
print(f"Can access public: {account.owner}")
print(f"Can access protected (but shouldn't): {account._account_type}")

try:
    print(account.__balance)
except AttributeError as e:
    print(f"✗ Cannot access private variable directly: {e}")

print(f"But can access through getter: ${account.get_balance()}")
print()

"""
WHAT HAPPENED IN MEMORY?
------------------------

When we created: account = BankAccount("Alice", 1000)

HEAP:
┌─────────────────────────────────────┐
│ BankAccount object at 0x5000        │
│                                     │
│ PUBLIC:                             │
│   owner = "Alice"                   │  ← Accessible anywhere
│                                     │
│ PROTECTED:                          │
│   _account_type = "Savings"         │  ← Convention: don't access
│                                     │
│ PRIVATE (name mangled):             │
│   _BankAccount__balance = 1000      │  ← Python renames it!
│   _BankAccount__transaction_history │  ← Python renames it!
│                                     │
└─────────────────────────────────────┘

Python's name mangling for private variables:
    self.__balance  →  becomes  →  self._BankAccount__balance

This makes it HARDER (but not impossible) to access from outside.
The goal is to DISCOURAGE direct access, not make it impossible.


KEY TAKEAWAYS:
--------------
✓ Encapsulation = Bundling + Hiding
✓ Use public for safe data, private for sensitive data
✓ Provide getter/setter methods for controlled access
✓ @property decorator makes getters/setters look like attributes
✓ Protects data from invalid states (negative balance, etc.)
"""


"""
================================================================================
PILLAR 2: INHERITANCE
================================================================================

WHAT IS INHERITANCE?
--------------------

Inheritance allows you to create a NEW class based on an EXISTING class.

The new class (CHILD/DERIVED/SUB class):
    ✓ INHERITS all attributes and methods from the parent
    ✓ Can ADD new attributes and methods
    ✓ Can OVERRIDE (change) inherited methods

The existing class (PARENT/BASE/SUPER class):
    ✓ Remains unchanged
    ✓ Can be used to create multiple child classes


REAL-WORLD ANALOGY:
-------------------

Think of biological inheritance:
    - You inherit traits from your parents (eye color, height, etc.)
    - But you also have your own unique traits
    - You can do things differently than your parents

In programming:
    Animal (parent)
        ↓ inherits
    Dog (child) - has everything Animal has + dog-specific stuff
        ↓ inherits
    Labrador (grandchild) - has everything Dog has + labrador-specific stuff


WHY USE INHERITANCE?
--------------------

WITHOUT inheritance (code duplication):
    class Dog:
        def __init__(self, name):
            self.name = name
        def eat(self): ...
        def sleep(self): ...
        def speak(self): return "Woof"
    
    class Cat:
        def __init__(self, name):
            self.name = name
        def eat(self): ...        # DUPLICATE CODE!
        def sleep(self): ...      # DUPLICATE CODE!
        def speak(self): return "Meow"

WITH inheritance (code reuse):
    class Animal:
        def __init__(self, name):
            self.name = name
        def eat(self): ...
        def sleep(self): ...
    
    class Dog(Animal):
        def speak(self): return "Woof"  # Only dog-specific code
    
    class Cat(Animal):
        def speak(self): return "Meow"  # Only cat-specific code


INHERITANCE HIERARCHY:
----------------------

         Animal (Parent/Base/Super class)
        /      \
     Dog        Cat (Child/Derived/Sub class)
    /    \
 Labrador  Poodle (Grandchild - Multi-level inheritance)

This is called an "IS-A" relationship:
    - Dog IS-A Animal
    - Labrador IS-A Dog
    - Labrador IS-A Animal (through Dog)
"""


class Animal:
    """Parent/Base class - defines common behavior for all animals."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100
    
    def eat(self):
        """Method inherited by all animals."""
        self.energy += 20
        if self.energy > 100:
            self.energy = 100
        return f"{self.name} is eating. Energy: {self.energy}"
    
    def sleep(self):
        """Method inherited by all animals."""
        self.energy = 100
        return f"{self.name} is sleeping. Energy restored!"
    
    def speak(self):
        """Generic method - child classes will override this."""
        return f"{self.name} makes a sound"
    
    def info(self):
        """Method inherited by all animals."""
        return f"{self.name} is a {self.species} with {self.energy} energy"


class Dog(Animal):
    """
    Child class - inherits from Animal.
    
    Syntax: class ChildClass(ParentClass):
    """
    
    def __init__(self, name, breed):
        """
        Child's constructor.
        
        We need to call the parent's __init__ to initialize inherited attributes!
        """
        # Call parent's __init__ using super()
        super().__init__(name, species="Dog")
        
        # Add new attribute specific to Dog
        self.breed = breed
    
    def speak(self):
        """
        OVERRIDE parent's method.
        
        When Dog calls speak(), it uses THIS version, not Animal's version.
        """
        return f"{self.name} says: Woof! Woof!"
    
    def fetch(self):
        """
        NEW method - only Dogs have this, not all Animals.
        """
        self.energy -= 10
        return f"{self.name} fetches the ball! Energy: {self.energy}"


class Cat(Animal):
    """Another child class inheriting from Animal."""
    
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color
    
    def speak(self):
        """Override speak() with cat-specific behavior."""
        return f"{self.name} says: Meow!"
    
    def scratch(self):
        """NEW method - only Cats have this."""
        return f"{self.name} scratches the furniture!"


print("=" * 80)
print("PILLAR 2: INHERITANCE")
print("=" * 80)

dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers", "Orange")

print("\n--- Using Inherited Methods ---")
print(dog.eat())      # Inherited from Animal
print(cat.sleep())    # Inherited from Animal

print("\n--- Using Overridden Methods ---")
print(dog.speak())    # Dog's version (overridden)
print(cat.speak())    # Cat's version (overridden)

print("\n--- Using Child-Specific Methods ---")
print(dog.fetch())    # Only Dog has this
print(cat.scratch())  # Only Cat has this

print("\n--- Using Inherited info() Method ---")
print(dog.info())     # Inherited from Animal
print(cat.info())     # Inherited from Animal

print("\n--- Checking Inheritance ---")
print(f"Is dog an instance of Dog? {isinstance(dog, Dog)}")
print(f"Is dog an instance of Animal? {isinstance(dog, Animal)}")
print(f"Is dog an instance of Cat? {isinstance(dog, Cat)}")
print()

"""
WHAT IS super()?
----------------

super() gives you access to the PARENT class.

Common uses:
    1. super().__init__(...) - Call parent's constructor
    2. super().method_name() - Call parent's method from child

Why use super() instead of Parent.__init__(self, ...)?
    - Works correctly with multiple inheritance
    - More maintainable (if parent class name changes)
    - Follows Python best practices


MEMORY VISUALIZATION:
---------------------

When you create: dog = Dog("Buddy", "Labrador")

HEAP:
┌─────────────────────────────────────┐
│ Dog object at 0x6000                │
│                                     │
│ FROM ANIMAL (inherited):            │
│   name = "Buddy"                    │
│   species = "Dog"                   │
│   energy = 100                      │
│                                     │
│ FROM DOG (new):                     │
│   breed = "Labrador"                │
│                                     │
│ METHODS (from both classes):        │
│   eat()     ← from Animal           │
│   sleep()   ← from Animal           │
│   info()    ← from Animal           │
│   speak()   ← OVERRIDDEN in Dog     │
│   fetch()   ← NEW in Dog            │
└─────────────────────────────────────┘

The Dog object contains EVERYTHING from Animal PLUS its own additions!


METHOD RESOLUTION ORDER (MRO):
------------------------------

When you call dog.speak(), Python searches for the method in this order:
    1. Dog class (found! Use Dog's speak())
    2. If not found, search Animal class
    3. If not found, search object class (base of all classes)

When you call dog.eat(), Python searches:
    1. Dog class (not found)
    2. Animal class (found! Use Animal's eat())

You can see the MRO: print(Dog.__mro__)
"""


# --- Multi-level Inheritance ---
class Labrador(Dog):
    """Grandchild class - inherits from Dog, which inherits from Animal."""
    
    def __init__(self, name, is_service_dog=False):
        super().__init__(name, breed="Labrador")
        self.is_service_dog = is_service_dog
    
    def assist(self):
        """Method specific to Labrador."""
        if self.is_service_dog:
            return f"{self.name} is assisting their owner!"
        return f"{self.name} is just a regular good boy!"


print("=" * 80)
print("MULTI-LEVEL INHERITANCE")
print("=" * 80)

lab = Labrador("Max", is_service_dog=True)
print(lab.speak())    # From Dog
print(lab.eat())      # From Animal (through Dog)
print(lab.fetch())    # From Dog
print(lab.assist())   # From Labrador
print(f"\nMax is a Dog: {isinstance(lab, Dog)}")
print(f"Max is an Animal: {isinstance(lab, Animal)}")
print(f"Max is a Labrador: {isinstance(lab, Labrador)}")
print()


# --- Multiple Inheritance ---
"""
Multiple Inheritance: A class can inherit from MULTIPLE parent classes.

Syntax: class Child(Parent1, Parent2, Parent3):

Use with caution! Can get complex.
"""

class Flyable:
    """Mixin class - adds flying ability."""
    def fly(self):
        return f"{self.name} is flying!"

class Swimmable:
    """Mixin class - adds swimming ability."""
    def swim(self):
        return f"{self.name} is swimming!"

class Duck(Animal, Flyable, Swimmable):
    """Duck inherits from Animal, Flyable, AND Swimmable."""
    
    def __init__(self, name):
        super().__init__(name, species="Duck")
    
    def speak(self):
        return f"{self.name} says: Quack!"


print("=" * 80)
print("MULTIPLE INHERITANCE")
print("=" * 80)

duck = Duck("Donald")
print(duck.speak())   # From Duck (overridden)
print(duck.eat())     # From Animal
print(duck.fly())     # From Flyable
print(duck.swim())    # From Swimmable
print()

"""
KEY TAKEAWAYS:
--------------
✓ Inheritance = IS-A relationship (Dog IS-A Animal)
✓ Child class inherits all attributes and methods from parent
✓ Use super() to call parent's methods
✓ Override methods to change behavior in child class
✓ Add new methods/attributes specific to child class
✓ Python supports multi-level and multiple inheritance
✓ Check inheritance: isinstance(object, Class)
"""


"""
================================================================================
PILLAR 3: POLYMORPHISM
================================================================================

WHAT IS POLYMORPHISM?
---------------------

Polymorphism = "Poly" (many) + "morph" (forms) = Many forms

The same method name can have DIFFERENT behaviors depending on which object calls it.

REAL-WORLD ANALOGY:
-------------------

Think of a "SPEAK" button:
    - Press it on a dog → "Woof!"
    - Press it on a cat → "Meow!"
    - Press it on a duck → "Quack!"

Same button (method name), different sounds (behaviors)!


WHY IS THIS USEFUL?
-------------------

You can write code that works with MANY different types of objects:

    animals = [Dog(), Cat(), Duck()]
    
    for animal in animals:
        animal.speak()  # Each animal speaks differently!

You don't need to know WHAT TYPE each animal is. You just call speak() and 
each object knows how to behave correctly!


TYPES OF POLYMORPHISM:
----------------------

1. METHOD OVERRIDING (we've already seen this in Inheritance)
   - Child class provides different implementation of parent's method
   - Example: Dog.speak() vs Cat.speak()

2. DUCK TYPING (Python's approach)
   - "If it walks like a duck and quacks like a duck, it's a duck"
   - Python doesn't care about the TYPE, only that the method EXISTS

3. OPERATOR OVERLOADING
   - Redefine how operators (+, -, *, ==, etc.) work for your class
   - Example: Make Vector + Vector work
"""


print("=" * 80)
print("PILLAR 3: POLYMORPHISM")
print("=" * 80)

print("\n--- Method Overriding (Polymorphism) ---")
animals = [
    Dog("Rex", "German Shepherd"),
    Cat("Tom", "Gray"),
    Duck("Daffy")
]

for animal in animals:
    print(f"{animal.speak()}")

print("\n--- Duck Typing Example ---")

class Bird:
    """A completely different class, not inheriting from Animal."""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says: Tweet!"

class Robot:
    """Another unrelated class."""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says: Beep boop!"

things_that_speak = [
    Dog("Buddy", "Labrador"),
    Cat("Whiskers", "Orange"),
    Bird("Tweety"),
    Robot("R2D2")
]

print("\nAll these objects can speak, even though they're different types:")
for thing in things_that_speak:
    print(f"  {thing.speak()}")

print()

"""
DUCK TYPING EXPLAINED:
----------------------

In the example above:
    - Dog, Cat, Bird, Robot are COMPLETELY DIFFERENT classes
    - They DON'T inherit from the same parent
    - But they ALL have a speak() method

Python doesn't care about the TYPE. It only cares:
    "Does this object have a speak() method? Yes? Great, call it!"

This is called "Duck Typing":
    "If it walks like a duck and quacks like a duck, then it must be a duck"
    
In Python:
    "If it has a speak() method, I can call speak() on it"


CONTRAST WITH STATICALLY-TYPED LANGUAGES (Java, C++):
------------------------------------------------------

In Java, you'd need:
    interface Speakable {
        void speak();
    }
    
    class Dog implements Speakable { ... }
    class Cat implements Speakable { ... }

In Python:
    Just add a speak() method. Done! No interface needed.
"""


# --- Operator Overloading ---
print("=" * 80)
print("OPERATOR OVERLOADING")
print("=" * 80)

class Vector:
    """
    A 2D vector class demonstrating operator overloading.
    
    We'll make mathematical operators work with our custom class!
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """
        Overload the + operator.
        
        Now we can do: v3 = v1 + v2
        Python calls: v1.__add__(v2)
        """
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overload the - operator."""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Overload the * operator (scalar multiplication)."""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """
        Overload the == operator.
        
        Now we can do: if v1 == v2:
        """
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        """
        Overload str() function.
        
        Called when: print(vector) or str(vector)
        """
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """
        Overload repr() function.
        
        Developer-friendly representation.
        """
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2      # Uses __add__
v4 = v2 - v1      # Uses __sub__
v5 = v1 * 3       # Uses __mul__

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v3}")
print(f"v2 - v1 = {v4}")
print(f"v1 * 3 = {v5}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == Vector(1, 2): {v1 == Vector(1, 2)}")
print()

"""
COMMON MAGIC METHODS (DUNDER METHODS):
---------------------------------------

"Dunder" = Double UNDERscore (e.g., __init__, __add__)

ARITHMETIC OPERATORS:
    __add__(self, other)      →  +
    __sub__(self, other)      →  -
    __mul__(self, other)      →  *
    __truediv__(self, other)  →  /
    __mod__(self, other)      →  %
    __pow__(self, other)      →  **

COMPARISON OPERATORS:
    __eq__(self, other)       →  ==
    __ne__(self, other)       →  !=
    __lt__(self, other)       →  <
    __le__(self, other)       →  <=
    __gt__(self, other)       →  >
    __ge__(self, other)       →  >=

STRING REPRESENTATION:
    __str__(self)             →  str(obj), print(obj)
    __repr__(self)            →  repr(obj), developer view

CONTAINER OPERATIONS:
    __len__(self)             →  len(obj)
    __getitem__(self, key)    →  obj[key]
    __setitem__(self, key, val) → obj[key] = val
    __contains__(self, item)  →  item in obj

OBJECT LIFECYCLE:
    __init__(self, ...)       →  Constructor
    __del__(self)             →  Destructor (rarely used)
    __call__(self, ...)       →  Makes object callable like a function


KEY TAKEAWAYS:
--------------
✓ Polymorphism = Same interface, different behaviors
✓ Method overriding: Child classes change parent's method behavior
✓ Duck typing: Python cares about methods, not types
✓ Operator overloading: Make operators work with custom classes
✓ Magic methods (__add__, __str__, etc.) enable operator overloading
"""


"""
================================================================================
PILLAR 4: ABSTRACTION
================================================================================

WHAT IS ABSTRACTION?
--------------------

Abstraction means:
    1. HIDING complex implementation details
    2. SHOWING only the essential features/interface

Think of it as a "contract" or "blueprint" that says:
    "Any class that inherits from me MUST implement these methods"


REAL-WORLD ANALOGIES:
---------------------

1. DRIVING A CAR:
   - INTERFACE (what you see): Steering wheel, pedals, gear shift
   - HIDDEN: Engine mechanics, fuel injection, transmission details
   - You don't need to know HOW the engine works to drive!

2. TV REMOTE:
   - INTERFACE: Power, volume, channel buttons
   - HIDDEN: Infrared signals, circuit boards, battery connections
   - You just press buttons, don't care about the internals!

3. SMARTPHONE:
   - INTERFACE: Touch screen, apps, icons
   - HIDDEN: Operating system code, hardware drivers, network protocols
   - You tap icons, don't need to understand the code!


WHY USE ABSTRACTION?
--------------------

1. SIMPLICITY: Hide complexity, show only what's needed
2. CONSISTENCY: Force all child classes to implement required methods
3. FLEXIBILITY: Change implementation without changing interface
4. ORGANIZATION: Clear contract of what methods a class must have


IN PYTHON: ABSTRACT BASE CLASSES (ABC)
---------------------------------------

Python uses the 'abc' module to create abstract classes.

An abstract class:
    ✓ CANNOT be instantiated directly (can't create objects from it)
    ✓ Defines abstract methods (methods with no implementation)
    ✓ Child classes MUST implement all abstract methods
    ✓ Acts as a template/contract for child classes
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract Base Class for all shapes.
    
    This is a CONTRACT that says:
    "Any class that inherits from Shape MUST implement area() and perimeter()"
    
    You CANNOT create a Shape object directly!
    """
    
    @abstractmethod
    def area(self):
        """
        Abstract method - NO implementation here.
        
        Every child class MUST provide its own implementation.
        """
        pass
    
    @abstractmethod
    def perimeter(self):
        """Another abstract method - child classes MUST implement."""
        pass
    
    def description(self):
        """
        CONCRETE method - has implementation.
        
        All child classes inherit this method as-is.
        They CAN override it if needed, but don't have to.
        """
        return f"I am a shape with area {self.area():.2f}"


class Circle(Shape):
    """Concrete class - implements all abstract methods from Shape."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """MUST implement - required by Shape."""
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        """MUST implement - required by Shape."""
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    """Another concrete class implementing Shape."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """MUST implement - required by Shape."""
        return self.width * self.height
    
    def perimeter(self):
        """MUST implement - required by Shape."""
        return 2 * (self.width + self.height)


class Triangle(Shape):
    """Yet another concrete class implementing Shape."""
    
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        """MUST implement - required by Shape."""
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        """MUST implement - required by Shape."""
        return self.side1 + self.side2 + self.side3


print("=" * 80)
print("PILLAR 4: ABSTRACTION")
print("=" * 80)

print("\n--- Trying to create abstract class ---")
try:
    shape = Shape()
except TypeError as e:
    print(f"✗ Error: {e}")

print("\n--- Creating concrete classes ---")
circle = Circle(5)
rect = Rectangle(4, 6)
triangle = Triangle(base=6, height=4, side1=5, side2=5, side3=6)

shapes = [circle, rect, triangle]

print("\nAll shapes (polymorphism + abstraction):")
for shape in shapes:
    print(f"  {shape.description()}")
    print(f"    Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")

print()

"""
WHAT HAPPENED IN MEMORY?
-------------------------

Abstract Class (Shape):
    - Exists as a CLASS definition in memory
    - CANNOT create instances (objects) from it
    - Defines the CONTRACT (interface) for child classes

Concrete Classes (Circle, Rectangle, Triangle):
    - Inherit from Shape
    - MUST implement all abstract methods
    - CAN create instances (objects) from them

When you create: circle = Circle(5)

HEAP:
┌─────────────────────────────────────┐
│ Circle object at 0x7000             │
│                                     │
│ ATTRIBUTES:                         │
│   radius = 5                        │
│                                     │
│ METHODS (from Shape + Circle):      │
│   area()        ← implemented       │
│   perimeter()   ← implemented       │
│   description() ← inherited         │
└─────────────────────────────────────┘


ABSTRACTION vs ENCAPSULATION:
------------------------------

ENCAPSULATION:
    - Bundling data + methods
    - Hiding internal details (private variables)
    - Example: BankAccount hides __balance

ABSTRACTION:
    - Hiding implementation complexity
    - Showing only essential interface
    - Example: Shape defines area() but doesn't implement it


WHEN TO USE ABSTRACT CLASSES?
------------------------------

Use abstract classes when:
    ✓ You have a group of related classes
    ✓ They should all have certain methods
    ✓ But each implements those methods differently
    ✓ You want to enforce a contract

Examples:
    - Shape → Circle, Rectangle, Triangle (all need area, perimeter)
    - Animal → Dog, Cat, Bird (all need eat, sleep, speak)
    - PaymentMethod → CreditCard, PayPal, Bitcoin (all need process_payment)
    - Database → MySQL, PostgreSQL, MongoDB (all need connect, query, close)


KEY TAKEAWAYS:
--------------
✓ Abstraction = Hide complexity, show essentials
✓ Abstract classes define a CONTRACT for child classes
✓ Use ABC and @abstractmethod from abc module
✓ Cannot instantiate abstract classes directly
✓ Child classes MUST implement all abstract methods
✓ Enforces consistency across related classes
"""


"""
================================================================================
CHAPTER 5: ADDITIONAL OOP CONCEPTS
================================================================================

Beyond the 4 pillars, there are other important OOP concepts you should know.
"""


# ============================================================
# COMPOSITION vs INHERITANCE
# ============================================================

"""
INHERITANCE = IS-A relationship
    - Dog IS-A Animal
    - Circle IS-A Shape
    - Use when: Child class is a specialized version of parent

COMPOSITION = HAS-A relationship
    - Car HAS-A Engine
    - Person HAS-A Address
    - Use when: Object contains other objects as parts

IMPORTANT PRINCIPLE:
    "Favor composition over inheritance" - Gang of Four Design Patterns

WHY?
    - More flexible
    - Easier to change
    - Avoids deep inheritance hierarchies
    - Reduces coupling
"""

class Engine:
    """A simple engine class."""
    
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False
    
    def start(self):
        self.is_running = True
        return f"{self.horsepower}HP {self.fuel_type} engine started!"
    
    def stop(self):
        self.is_running = False
        return "Engine stopped."


class Wheels:
    """A wheels class."""
    
    def __init__(self, count, size):
        self.count = count
        self.size = size
    
    def info(self):
        return f"{self.count} wheels, {self.size} inches each"


class Car:
    """
    Car uses COMPOSITION - it HAS-A Engine and HAS-A Wheels.
    
    Instead of inheriting from Engine, we include an Engine object.
    This is more flexible!
    """
    
    def __init__(self, brand, hp, fuel_type):
        self.brand = brand
        self.engine = Engine(hp, fuel_type)  # HAS-A Engine
        self.wheels = Wheels(4, 18)          # HAS-A Wheels
    
    def start(self):
        return f"{self.brand}: {self.engine.start()}"
    
    def info(self):
        return f"{self.brand} with {self.wheels.info()}"


print("=" * 80)
print("COMPOSITION (HAS-A Relationship)")
print("=" * 80)

ferrari = Car("Ferrari", 500, "Gasoline")
tesla = Car("Tesla", 400, "Electric")

print(ferrari.start())
print(tesla.start())
print(ferrari.info())
print()

"""
MEMORY VISUALIZATION OF COMPOSITION:
-------------------------------------

When you create: ferrari = Car("Ferrari", 500, "Gasoline")

HEAP:
┌─────────────────────────────────────┐
│ Car object at 0x8000                │
│   brand = "Ferrari"                 │
│   engine ──────┐                    │
│   wheels ──────┼────┐               │
└────────────────┼────┼───────────────┘
                 │    │
                 ↓    ↓
    ┌────────────────────┐  ┌──────────────────┐
    │ Engine at 0x8100   │  │ Wheels at 0x8200 │
    │   horsepower = 500 │  │   count = 4      │
    │   fuel_type = "Gas"│  │   size = 18      │
    │   is_running=False │  └──────────────────┘
    └────────────────────┘

The Car object CONTAINS references to Engine and Wheels objects.
This is composition - building complex objects from simpler ones!


WHEN TO USE INHERITANCE vs COMPOSITION:
----------------------------------------

Use INHERITANCE when:
    ✓ True IS-A relationship (Dog IS-A Animal)
    ✓ Child needs ALL parent functionality
    ✓ Relationship won't change

Use COMPOSITION when:
    ✓ HAS-A relationship (Car HAS-A Engine)
    ✓ Need flexibility to swap components
    ✓ Want to avoid deep inheritance hierarchies
    ✓ Objects are made up of parts
"""


# ============================================================
# SPECIAL METHODS RECAP
# ============================================================

print("=" * 80)
print("SPECIAL METHODS (MAGIC METHODS)")
print("=" * 80)

class Book:
    """Demonstrating various special methods."""
    
    def __init__(self, title, author, pages):
        """Constructor - called when creating object."""
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation for users."""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """String representation for developers."""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Called by len(book)."""
        return self.pages
    
    def __eq__(self, other):
        """Called by book1 == book2."""
        return (self.title == other.title and 
                self.author == other.author)
    
    def __lt__(self, other):
        """Called by book1 < book2 (less than)."""
        return self.pages < other.pages
    
    def __add__(self, other):
        """Called by book1 + book2."""
        combined_title = f"{self.title} & {other.title}"
        combined_author = f"{self.author} & {other.author}"
        combined_pages = self.pages + other.pages
        return Book(combined_title, combined_author, combined_pages)

book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Advanced Python", "Jane Smith", 450)
book3 = Book("Python Basics", "John Doe", 300)

print(f"book1: {book1}")
print(f"repr(book1): {repr(book1)}")
print(f"len(book1): {len(book1)} pages")
print(f"book1 == book2: {book1 == book2}")
print(f"book1 == book3: {book1 == book3}")
print(f"book1 < book2: {book1 < book2}")

combined = book1 + book2
print(f"book1 + book2: {combined}")
print()


"""
================================================================================
CHAPTER 6: DESIGN PRINCIPLES & PATTERNS (INTERVIEW ESSENTIALS)
================================================================================

These are commonly asked in technical interviews!
"""


# ============================================================
# SOLID PRINCIPLES
# ============================================================

"""
SOLID is an acronym for 5 design principles that make code:
    - More maintainable
    - Easier to understand
    - Flexible and scalable
    - Easier to test


1. SINGLE RESPONSIBILITY PRINCIPLE (SRP)
-----------------------------------------
"A class should have only ONE reason to change"
= Each class should do ONE thing and do it well

BAD Example:
    class User:
        def save_to_database(self): ...
        def send_email(self): ...
        def generate_report(self): ...
    
    Problem: This class has 3 responsibilities!

GOOD Example:
    class User:
        def __init__(self, name): ...
    
    class UserRepository:
        def save(self, user): ...
    
    class EmailService:
        def send_email(self, user): ...
    
    class ReportGenerator:
        def generate(self, user): ...


2. OPEN/CLOSED PRINCIPLE (OCP)
-------------------------------
"Open for extension, closed for modification"
= Add new features by ADDING code, not CHANGING existing code

Use inheritance or composition to extend behavior.


3. LISKOV SUBSTITUTION PRINCIPLE (LSP)
---------------------------------------
"Child class should be usable wherever parent class is expected"
= Substituting a child for a parent shouldn't break the program

Example:
    If you have: def process_animal(animal: Animal)
    You should be able to pass Dog, Cat, Bird without issues


4. INTERFACE SEGREGATION PRINCIPLE (ISP)
-----------------------------------------
"Don't force clients to depend on methods they don't use"
= Many small, specific interfaces > One large, general interface


5. DEPENDENCY INVERSION PRINCIPLE (DIP)
----------------------------------------
"Depend on abstractions, not concrete implementations"
= Use abstract classes/interfaces, not specific classes
"""


# ============================================================
# DESIGN PATTERNS
# ============================================================

print("=" * 80)
print("DESIGN PATTERNS")
print("=" * 80)

"""
Design patterns are proven solutions to common programming problems.
"""

# --- SINGLETON PATTERN ---
print("\n--- Singleton Pattern ---")

class DatabaseConnection:
    """
    Singleton: Ensures only ONE instance of the class exists.
    
    Use case: Database connections, logging, configuration
    """
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creating new database connection...")
            cls._instance = super().__new__(cls)
            cls._instance.connection_id = id(cls._instance)
        return cls._instance
    
    def query(self, sql):
        return f"Executing query on connection {self.connection_id}: {sql}"

db1 = DatabaseConnection()
db2 = DatabaseConnection()
db3 = DatabaseConnection()

print(f"db1 is db2: {db1 is db2}")
print(f"db1 is db3: {db1 is db3}")
print(f"All three are the SAME object!")
print(db1.query("SELECT * FROM users"))
print()


"""
================================================================================
FINAL SUMMARY - EVERYTHING YOU NEED TO KNOW ABOUT OOP
================================================================================

CORE CONCEPTS:
--------------

1. CLASS vs OBJECT
   - Class = Blueprint/Template
   - Object = Instance created from the class
   - One class → Many objects

2. ATTRIBUTES (Data)
   - Instance variables: self.name (unique to each object)
   - Class variables: shared by all objects

3. METHODS (Behavior)
   - Instance methods: def method(self) - work with object data
   - Class methods: @classmethod - work with class data
   - Static methods: @staticmethod - utility functions

4. CONSTRUCTOR
   - __init__(self, ...) - initializes object
   - Called automatically when creating object
   - Sets up initial state


THE 4 PILLARS OF OOP:
---------------------

1. ENCAPSULATION
   - Bundle data + methods together
   - Hide internal details (private variables: __variable)
   - Provide controlled access (getters/setters)
   - Use @property for Pythonic getters/setters

2. INHERITANCE
   - Create new class from existing class
   - Child inherits all parent attributes/methods
   - Use super() to call parent methods
   - IS-A relationship (Dog IS-A Animal)
   - Enables code reuse

3. POLYMORPHISM
   - Same method name, different behaviors
   - Method overriding (child changes parent's method)
   - Duck typing (if it has the method, call it)
   - Operator overloading (__add__, __eq__, etc.)

4. ABSTRACTION
   - Hide complexity, show essentials
   - Use ABC and @abstractmethod
   - Define contracts for child classes
   - Cannot instantiate abstract classes


MEMORY MODEL:
-------------

STACK (Variable Names)          HEAP (Objects)
┌──────────────┐               ┌─────────────────┐
│ obj ─────────┼──────────────>│ Object data     │
│ (reference)  │               │ at 0x12345...   │
└──────────────┘               └─────────────────┘

- Variables store REFERENCES (memory addresses)
- Objects live in the HEAP
- Multiple variables can reference the same object


IMPORTANT RELATIONSHIPS:
------------------------

IS-A (Inheritance):
    Dog IS-A Animal → Use inheritance

HAS-A (Composition):
    Car HAS-A Engine → Use composition
    Favor composition over inheritance!


SPECIAL METHODS (Magic Methods):
---------------------------------

__init__(self)           → Constructor
__str__(self)            → str(obj), print(obj)
__repr__(self)           → repr(obj)
__len__(self)            → len(obj)
__add__(self, other)     → obj1 + obj2
__eq__(self, other)      → obj1 == obj2
__lt__(self, other)      → obj1 < obj2
__getitem__(self, key)   → obj[key]


ACCESS MODIFIERS:
-----------------

public:     self.name        (accessible anywhere)
protected:  self._name       (convention: internal use)
private:    self.__name      (name mangled, hard to access)


WHEN TO USE WHAT:
-----------------

Use CLASSES when:
    ✓ Grouping related data and functions
    ✓ Creating multiple similar objects
    ✓ Modeling real-world entities

Use INHERITANCE when:
    ✓ True IS-A relationship
    ✓ Need to reuse parent functionality
    ✓ Relationship is stable

Use COMPOSITION when:
    ✓ HAS-A relationship
    ✓ Need flexibility
    ✓ Building complex objects from parts

Use ABSTRACTION when:
    ✓ Defining contracts for child classes
    ✓ Enforcing method implementation
    ✓ Creating frameworks/libraries


COMMON INTERVIEW QUESTIONS:
---------------------------

Q: What is OOP?
A: Programming paradigm that organizes code using objects containing data and methods.

Q: What are the 4 pillars?
A: Encapsulation, Inheritance, Polymorphism, Abstraction

Q: What is self?
A: Reference to the current object instance

Q: Class variable vs Instance variable?
A: Class variable is shared by all instances, instance variable is unique to each object

Q: What is super()?
A: Gives access to parent class methods

Q: Composition vs Inheritance?
A: Composition (HAS-A) is often preferred over Inheritance (IS-A) for flexibility

Q: What are magic methods?
A: Special methods with double underscores (__init__, __str__, etc.) that Python calls automatically

Q: What is polymorphism?
A: Same method name, different behaviors depending on the object

Q: What is abstraction?
A: Hiding implementation details, showing only essential features using abstract classes


BEST PRACTICES:
---------------

✓ Keep classes focused (Single Responsibility)
✓ Use meaningful names
✓ Favor composition over inheritance
✓ Use private variables for sensitive data
✓ Implement __str__ and __repr__ for debugging
✓ Use @property for getters/setters
✓ Follow SOLID principles
✓ Write docstrings for classes and methods
✓ Keep inheritance hierarchies shallow (2-3 levels max)


CONGRATULATIONS!
----------------

You now have a COMPLETE understanding of Object-Oriented Programming in Python!

From absolute basics (what is a class?) to advanced concepts (abstraction, SOLID),
you've learned:
    ✓ How classes and objects work
    ✓ What happens in memory
    ✓ The 4 pillars of OOP
    ✓ When to use each concept
    ✓ Best practices and design principles

You're ready for OOP interview questions! 🎉


NEXT STEPS:
-----------

1. Practice: Create your own classes (Student, Library, Game, etc.)
2. Read code: Look at how popular libraries use OOP
3. Refactor: Take procedural code and convert it to OOP
4. Build projects: Apply OOP to real-world problems
5. Study design patterns: Learn more patterns (Factory, Observer, Strategy, etc.)


Remember: OOP is a TOOL, not a requirement. Use it when it makes your code
better, not just because you can!
"""

print("=" * 80)
print("END OF OOP GUIDE")
print("=" * 80)
print("\nYou've completed the comprehensive OOP tutorial!")
print("Run this file to see all examples in action.")
print("\nHappy coding! 🐍")
