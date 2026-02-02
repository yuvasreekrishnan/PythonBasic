# Single Inheritance Example
class parent:
    def show(self):
        print("This is parent class")

class child(parent):
    def display(self):
        print("This is child class")
c = child()
c.show()
c.display()
# Multilevel Inheritance Example
class grandparent:
    def greet(self):
        print("Hello from grandparent class")

class parent(grandparent):
    def say(self):
        print("Hello from parent class")

class child(parent):
    def tell(self):
        print("Hello from child class")

ch = child()
ch.greet()
ch.say()
ch.tell()
#multiple Inheritance Example
class father:
    def father_info(self):
        print("This is father class")
class mother:
    def mother_info(self):
        print("This is mother class")
class child(father, mother):
    def child_info(self):
        print("This is child class")
c = child()
c.father_info()
c.mother_info()
c.child_info()
# Hierarchical Inheritance Example
class animal:
    def eat(self):
        print("Animal eats food")

class dog(animal):
    def bark(self):
        print("Dog barks")

class cat(animal):
    def meow(self):
        print("Cat meows")

d = dog()
d.eat()
d.bark()

c = cat()
c.eat()
c.meow()
