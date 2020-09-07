from abc import ABCMeta, abstractmethod

bodydict={"大":3,"中":2,"小":1}

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self,kind,body,character):
        self.kind=kind
        self.body=body
        self.character=character

    @property
    def is_ferocious(self):
        if bodydict[self.body] >= 2 and self.kind == "食肉" and self.character == "凶猛":
            return True
        else:
            return False


class Cat(Animal):
    sound = "MIAO MIAO"

    def __init__(self,name,kind,body,character):
        super().__init__(kind,body,character)
        self.name=name

    @classmethod
    def cat_sound(cls):
        print(cls.sound)

    @property
    def is_pet(self):
        if self.is_ferocious == True:
            return False
        else:
            return True


class Dog(Cat):

    sound = "WOW WOW"


class Zoo(object):
    all_animal={}

    def __init__(self,name):
        self.name=name

    def add_animal(self,instance):
        if instance not in self.all_animal:
            self.all_animal[instance]=id(instance)
        else:
            return "already got this animal"
            
    # def add_animal(self,instance):
    #     if id(instance) == self.total_animal[instance]:
    #         return "already got this animal"
    #     else:
    #         self.total_animal[instance]=id(instance)

def hasattr(zoo,instance):
    if zoo.all_animal.get(instance):
        return True
    else:
        return False


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')