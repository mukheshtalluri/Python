"""
What object-oriented programing: Oops is the programing paradigm. Here we will treat everything as object it will help us
to create large projects and easy maintainability and reusability.

Object: Object is real word entity in programing terms. Object will behave how they define in the class.

Class: Class is a blueprint where we can define the behavior of the object we can create as many objects as based on the class

Understanding of class and object in easy way: Human robert is the class. we will define behavior of the robert in the form
of methods and what robert require we will provide in the form of arguments. Normally we will call all thing as the class.
based on the above human robert design we can create no.of human roberts as per the requirement. This is object.

Example : College entry form --> It is a class it will common for all but when it come to a person fill this form that is object
it will be specific to that person.

Constructor: Constructor is used to initialise the arguments. In above case we create variables after the object creation
while using constructor while define object only we will provide all the arguments.Constructor will be call automatically
when object will call. There are two types of constructors are there
Default constructor: It won't take any arguments as the input other self parameter.
Parameterised constructor: Here we will pass some arguments along with the self key word.

Decorators: Decorators are the functions which will change the run time behavior of the existing function without changing existing code.

Getters and setters: Getters and Setters used to access the data of an object. In python, we can directly access the
data when we want to encapsulate the data and when we want to access control will see the setters and getters.

Inheritance: Inheritance is the property where we can access the parent class methods and attributes in the child class.
Different types of Inheritance are there
Single Inheritance: Inherit property from the single class.
Multiple Inheritance: Inherit property from the different parent classes.
Multilevel Inheritance: Inherit property from the grandparent class.
Hierarchical Inheritance: Parent class Inherited by the multiple child classes.
Hybrid Inheritance: using multiple types of inheritance.

Access modifiers: Access modifiers will help us to control the access of class attributes and methods while inheriting.
There are few types of access modifiers will be there will discuss them
Public: By default all classes are public we can access them outside of class as well.
Private: Protected methods can accessible in side of class only.
Protected: Protected method can be accessible with the class and it's subclass.

Static methods: Static methods will belong to the class not to the instance. we can call by the class name not by the object name.

Class variables and Instant variables: Class variables will be defined at the class level and it will access to among the
all instants. Instant variables are subjected too only to the particular instant.

Class methods: Class methods are associated with the classes not with the instants, no need to provide self keyword instead
we need to mention class representation and when we want change something we need by the class method. We can use class method
as the alternative to the constructor.

Super keyword: Super keyword is used to inherit property from the parent class. When we have multiple parent classes inherited
by the child classes super keyword will help to inherit property from the parent class.

Method overriding: Method overriding is the process redefine method in the child class which already there in parent class.
method overriding essential in case of polymorphism.

"""

# Class
class Details:
    name = "Bob"
    profession = "Software Engineer"

    def info(self): # Self keyword will represent the instantaneous class.
        print(f"My name is {self.name} and my profession is {self.profession}.")

# Object
obj = Details()
obj.name = "Karthik"
print(obj.name)
print(obj.profession)
obj.info()

# By using same class we can create no.of objects as required.
a = Details()
a.name = "Robbin"
a.profession = "Hard Engineer"
a.info()

# Constructor - __init__ will be constructor. This is Default constructor.
class Greet:
    def __init__(self):
        print("Hello everyone..!")

Greet()
class PersonInfo:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def info(self):
        print(f"My name is {self.name} and i am a {self.profession}.")

person1 = PersonInfo("Bala krishna", "Actor")
person1.info()
person1 = PersonInfo("Raja mouli", "Director")
person1.info()


# Decorators - How decorator will work, I want to perform division operation with respect to any input given by the user
# decorator will help us to give us numerator value always higher than denominator.
def my_decorator(func):
    def wrapper(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return wrapper

@my_decorator
def division(a, b):
    result = a / b
    return result

print(division(2, 4))

# Setters and Getters
class Person:
    def __init__(self, name):
        self. _name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def set_name(self, name):
        self._name = name

person = Person("Rocky")
print(person.name)
person.set_name = "Rolex"
print(person.name)

# Inheritance
# Single Inheritance
class Parent:
    def fun1(self):
        print("This is parent class.")

class Child(Parent):
    def fun2(self):
        print("This is child class.")

obj = Child()
obj.fun1()
obj.fun2()

# Multiple Inheritance
class Father:
    father_name = "Daddy"
    def father(self):
        print(self.father_name)

class Mother:
    mother_name = "Mommy"
    def mother(self):
        print(self.mother_name)

class Son(Father, Mother):
    def parents(self):
        print("Father name :", self.father_name)
        print("Mother name :", self.mother_name)

son = Son()
son.parents()

# Multilevel Inheritance
class GrandParent:
    def grand_parent(self):
        print("I am GrandParent")

class Parent(GrandParent):
    def parent(self):
        print("I am Parent")

class Son(Parent):
    def son(self):
        print("I am Child")

son = Son()
son.son()
son.parent()
son.grand_parent()

# Hierarchical Inheritance
class Father:
    def father(self):
        print("I am Father")

class Son(Father):
    def son(self):
        print("I am Son")

class Daughter(Father):
    def daughter(self):
        print("I am Daughter")

son = Son()
son.son()
son.father()
daughter = Daughter()
daughter.daughter()
daughter.father()

# Hybrid Inheritance

class Father:
    def father(self):
        print("I am Father")

class Son(Father):
    def son(self):
        print("I am Son")

class Daughter(Father):
    def daughter(self):
        print("I am Daughter")

class AnthorSon(Son, Father):
    def anthorson(self):
        print("I am anthor son.")

anthorson = AnthorSon()
anthorson.anthorson()
anthorson.son()
anthorson.father()


# Access modifiers
# Public Access modifier
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Bob", 20)
print(student.name)
print(student.age)

# Private Access modifier - In python there is know such strict concept.
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __funName(self):
        self.y = 25
        print(self.y)

class Subject(Student):
    pass

obj = Student("Abhishek", 25)
obj1 = Subject

# print(obj.__name)
# print(obj.__age)
#
# print(obj1.__name)
# print(obj1.__age)

# Name mangled
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am non mangled attribute"
        self.__mangled_attribute = "I am mangled attribute"

# my_object = MyClass()
# print(my_object._nonmangled_attribute)
# print(my_object.__mangled_attribute)
# print(my_object._MyClass__mangled_attribute)

# Protected Access modifier
class Student:
    def __init__(self):
        self._name = "Bob"
    def _funName(self):
        return "Betting Bob"
class Subject(Student):
    pass
obj = Student()
obj1 = Subject()

# print(obj._name)
# print(obj._funName())
#
# print(obj1._name)
# print(obj1._funName())


# Static methods
class Math:
    def __init__(self, num):
        self.num = num

    def add_to_num(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b

a = Math(5)
print(a.num)
a.add_to_num(6)
print(a.num)
# Static method
print(Math.add(7, 4))


# Class variable vs Instant variable
# Class variable
class MyClass:
    class_variable = 0
    def __init__(self):
        MyClass.class_variable += 1

    def print_class_variable(self):
        print(MyClass.class_variable)

myclass = MyClass()
myclass.print_class_variable()

myclass1 = MyClass()
myclass1.print_class_variable()

# Instant variable
class MyClass:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

obj1 = MyClass("John")
obj2 = MyClass("Jane")
obj1.print_name()
obj2.print_name()


# Class methods
class Employee:
    company = "apple"
    def show(self):
        print(f"I am working at {self.company}.")
    @classmethod
    def newcompany(cls, new_company):
        cls.company = new_company

e = Employee()
e.show()
e.newcompany("Tesla")
e.show()
print(Employee.company)

# Class method as the constructor
class Student:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromstring(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

string = "Bob-12345"
s1 = Student.fromstring(string)
print(s1.name)
print(s1.salary)

# Super keyword
class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")
class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")
class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()

# Method overriding
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()


# rec = Shape(3, 5)
# print(rec.area())

c = Circle(5)
print(c.area())









