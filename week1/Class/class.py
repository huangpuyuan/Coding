class Dog:
    # 类属性
    species = "Canis familiaris"

    # 初始化方法
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age    # 实例属性

    # 实例方法
    def bark(self):
        return f"{self.name} says woof!"


# 创建对象
my_dog = Dog("Buddy", 3)

# 访问对象的属性
print(my_dog.name)  # 输出: Buddy
print(my_dog.age)   # 输出: 3

# 调用对象的方法
print(my_dog.bark())  # 输出: Buddy says woof!


# 访问类属性
print(Dog.species)  # 输出: Canis familiaris

# 修改类属性
Dog.species = "Canis lupus familiaris"
print(my_dog.species)  # 输出: Canis lupus familiaris


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def bark_sound():
        return "Woof!"

# 使用类方法
print(Dog.get_species())  # 输出: Canis familiaris

# 使用静态方法
print(Dog.bark_sound())  # 输出: Woof!


class Puppy(Dog):  # Puppy 继承自 Dog
    def __init__(self, name, age, training_level):
        super().__init__(name, age)  # 调用父类的初始化方法
        self.training_level = training_level

    def bark(self):
        return f"{self.name} says woof! (Training level: {self.training_level})"

# 创建 Puppy 对象
my_puppy = Puppy("Max", 1, "Beginner")
print(my_puppy.bark())  # 输出: Max says woof! (Training level: Beginner)


class Dog:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.age = age

    def get_name(self):
        return self.__name  # 通过方法访问私有属性

# 创建对象
my_dog = Dog("Buddy", 3)
print(my_dog.get_name())  # 输出: Buddy
# print(my_dog.__name)  # 会引发 AttributeError
