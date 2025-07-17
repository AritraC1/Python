# Metaclass
# A metaclass is the class of a class. Just like objects are instances of classes, classes themselves are instances of metaclasses. Python's built-in metaclass is `type`. It is used to customize class creation behavior, enforce coding rules (e.g., class names, attribute types), and auto-register or inject logic into all classes. By default, every class in Python is created using the built-in `type` metaclass.

# Creating a class manually using `type`
MyClass = type("MyClass", (), {"x": 10})

obj = MyClass()
print("[type] obj.x =", obj.x)
print("[type] type(MyClass) =", type(MyClass))

print()

# Basic Custom Metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"[MyMeta] Creating class: {name}")
        dct["created_by"] = "MyMeta"
        return super().__new__(cls, name, bases, dct)

class MyClassWithMeta(metaclass=MyMeta):
    pass

print("Created by:", MyClassWithMeta.created_by)

print()

# `__new__` vs `__init__` in Metaclasses
class MetaExample(type):
    def __new__(cls, name, bases, dct):
        print(f"[__new__] Creating class {name}")
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f"[__init__] Initializing class {name}")
        super().__init__(name, bases, dct)

class ExampleClass(metaclass=MetaExample):
    pass

print()

# Enforce Class Naming Rules
class UppercaseValidator(type):
    def __new__(cls, name, bases, dct):
        if not name.isupper():
            raise TypeError("Class name must be uppercase.")
        return super().__new__(cls, name, bases, dct)

class VALID(metaclass=UppercaseValidator):
    pass

# class invalid(metaclass=UppercaseValidator):  # Raises TypeError
#     pass

print()

# Inheritance & Metaclass Behavior
class LoggerMeta(type):
    def __new__(cls, name, bases, dct):
        dct['log'] = lambda self: print(f"{name} log triggered")
        return super().__new__(cls, name, bases, dct)

class Parent(metaclass=LoggerMeta):
    pass

class Child(Parent):
    pass

Child().log()  # Output: Child log triggered


'''
Real-World Use Cases:
1. Django ORM: Uses metaclasses to enforce model fields
2. Plugin systems: Auto-register classes into global registries
3. DSLs: SQLAlchemy uses metaclasses for table mapping
4. Enforce coding standards: Naming, method types, etc.
5. Singleton pattern: Control number of instances at class level

WHEN TO AVOID METACLASSES: Use decorators or mixins when possible (simpler and easier to test). Use metaclasses only if you must alter how classes themselves are constructed.
'''
