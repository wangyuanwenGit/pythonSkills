# 几种专为算法设计的设计模式

# 1.策略模式
# 定义一系列算法，将每个算法都封装起来，并且使他们之间可以互相替换，策略模式使算法
# 可以独立于使用它的用户而变化
# 优点：
# 算法（规则）可自由地切换
# 避免使用多重条件判断
# 方便扩展和增加新的算法（规则）。

class Person:
    '''人类'''
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def show_myself(self):
        print(self.name + " " + str(self.age) + " years old, " + 
                str(self.weight) + "kg, " + str(self.height) + "m.")


class ICompare:
    '''比较算法'''
    def comparable(self, person1, person2):
        '''person1 > person2 return value > 0, person1 == person2 return 0,
        perason1 < person2 return value < 0'''
        pass


class CompareByAge(ICompare):
    '''通过年龄排序'''
    def comparable(self, person1, person2):
        return person1.age - person2.age


class CompareByHeight(ICompare):
    '''通过身高排序'''
    def comparable(self, person1, person2):
        return person1.height - person2.height


class SortPerson:
    '''Person的排序类'''
    def __init__(self, compare):
        self.__compare = compare

    def sort(self, personList):
        '''排序算法,这里采用最简单的冒泡排序'''
        n = len(personList)
        for i in range(0, n - 1):
            for j in range(n - i -1):
                if(self.__compare.comparable(personList[j], personList[j + 1]) > 0):
                    tmp = personList[j]
                    personList[j] = personList[j + 1]
                    personList[j + 1] = tmp
            j += 1
        i += 1


'''测试代码：'''

def testSortPerson():
    personList = [
            Person("Tony", 2, 54.5, 0.82),
            Person("Jack", 31, 74.5, 1.80),
            Person("Nick", 19, 44.5, 1.78),
            Person("Helen", 20, 45.7, 1.60)
            ]
    sorter0 = SortPerson(CompareByAge())
    sorter0.sort(personList)
    print("根据年龄进行排序后的结果：")
    for person in personList:
        person.show_myself()

    sorter1 = SortPerson(CompareByHeight())
    sorter1.sort(personList)
    print("根据身高进行排序后的结果：")
    for person in personList:
        person.show_myself()


if __name__ == '__main__':
    testSortPerson()

# 当然，以上把代码也可以使用python内置方法解决：

# from operator import itemgetter, attrgetter
# sortedPerson = sorted(personList, key = attrgetter('age'))
# sortedPerson1 = sorted(personList, key = attrgetter('height'))

# 使用这个模式更易于扩展，自定义一些算法排序更好实现，
# 如身高和体重进行权重综合排序

class CompareByHeightAndWeight(ICompare):
    '''根据身高和体重的综合情况来排序（身高和体重的权重分别为0.6和0.4）'''
    def comparabel(self, person1, person2):
        value1 = person1.height * 0.6 + person1.weight * 0.4
        value2 = person2.height * 0.6 + person2.weight * 0.4
        return value1 - value2

# 2.模板模式
# 定义一个操作中的算法的框（骨）架， 而将算法中用到的某些具体的步骤放到子类中
# 去实现，使得子类可以在不改变算法结构的情况下重新定义该算法的某些特定步骤，
# 这个定义骨架的方法就叫模板方法

# 对一些复杂的算法进行分割，将其算法中固定不变的部分设计为模板方法和父类具体方法，
# 而一些可以改变的细节由其子类来实现，即一次性实现一个算法的不变部分，并将可变的行为留给子类来实现



# 3.访问模式
# 封装一些作用于某种数据结构中哥元素的操作，它可以在不改变数据结构的前提下定义作用于
# 这些元素的新的操作

# 访问模式的核心思想在于：可以在不改变数据结构的前提下定义作用于这些元素的新操作。将数据结构与
# 具体算法解耦，而且能更方便地扩展新的操作。

from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstructmethod来定义抽象类和抽象方法

class DataNode(metaclass=ABCMeta):
    '''数据结构类'''
    def accept(self, visitor):
        '''接受访问者的访问'''
        visitor.visit(self)


class Visitor(metaclass=ABCMeta):
    '''访问者'''
    @abstructmethod
    def visit(self, data):
        '''对数据对象的访问操作'''
        pass


class ObjectStructure:
    '''数据结构的管理类，也是数据对象的一个容器，可遍历容器内的所有元素'''
    def __init__(self):
        self.__datas = []

    def add(self, dataElement):
        self.__datas.append(dataElement)

    def action(self, visitor):
        '''进行数据访问的操作'''
        for data in self.__datas:
            visitor.visit(data)



class Animals(DataNode):
    '''动物类'''
    def __init__(self, isMale, weight):
        self.__isMale = isMale
        self.__weight = weight

    def isMale(self):
        return self.__isMale

    def getWeight(self):
        return self.__weight


class Cat(Animal):
    '''猫'''
    def speak(self):
        print("miao~")


class Dog(Animal):
    '''狗'''
    def speak(self):
        print("wang~")


class GenderCounter(Visitor):
    '''性别统计'''
    def __init__(self):
        self.__maleCat = 0
        self.__femaleCat = 0
        self.__maleDog = 0
        self.__femaleDog = 0

    def visit(self, data):
        if isinstance(data, Cat):
            if data.isMale():
                self.__maleCat += 1
            else:
                self.__femaleCat += 1
        elif isinstance(data, Dog):
            if data.isMale():
                self.__maleDog += 1
            else:
                self.__femaleDog += 1
        else:
            print("Not support this type!")

    def getInfo(self):
        print(str(self.__maleCat) + "只雄猫，" + str(self.__femaleCat) + "只雌猫，"
                + str(self.__maleDog) + "只雄狗，" + str(self.__femaleDog) + "只雌狗。")


class WeightCounter(Visitor):
    '''体重的统计'''
    def __init__(self):
        self.__catNum = 0
        self.__catWeight = 0
        self.__dogNum = 0
        self.__dogWeight = 0

    def visit(self, data):
        if isinstance(data, Cat):
            self.__catNum +=1
            self.__catWeight += data.getWeight()
        elif isinstance(data, Dog):
            self.__dogNum += 1
            self.__dogWeight += data.getWeight()
        else:
            print("Not Support this type!")

    def getInfo(self):
        print("猫的平均体重是：%0.2fkg, 狗的平均体重是：%0.2fkg" % 
                ((self.__catWeight / self.__catNum), (self.__dogWeight / self.__dogNum)))

def testAnimal():
    animals = ObjectStructure()

    animals.add(Cat(True, 5.1))
    animals.add(Cat(False, 4.3))
    animals.add(Dog(True, 8))
    animals.add(Dog(False, 21))
    animals.add(Dog(False, 25))
    
    genderCounter = GenderCounter()
    animals.action(genderCounter)
    genderCounter.getInfo()
    print()
    weightCounter = WeightCounter()
    animals.action(weightCounter)
    weightCounter.getInfo()

