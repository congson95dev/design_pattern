# Explaination:
# Thay vì tạo đối tượng Dog hoặc Cat trực tiếp, ta sẽ tạo ra chúng thông qua một factory class, 
# giúp cho việc tạo đối tượng trở nên linh hoạt hơn và giảm sự phụ thuộc.
# chúng ta sử dụng AnimalFactory để tạo ra các đối tượng Dog và Cat thông qua phương thức get_animal()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def get_animal(self, animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            return None

animal_factory = AnimalFactory()

dog = animal_factory.get_animal("dog", "Max")
print(dog.name)   # Output: Max
print(dog.speak())   # Output: Woof!

cat = animal_factory.get_animal("cat", "Luna")
print(cat.name)   # Output: Luna
print(cat.speak())   # Output: Meow!