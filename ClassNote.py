#*#1.关于对Python中类(class)和对象(object)的理解：
(1)在Python中，所有数据(包括数字和字符串)实际上都是对象，
在Python中，有int类，float类，str类，list类，dict类，tuple类等。
例如：
整数：3；严格说，3是int类的一个对象；
n = 3，严格说，n是一个引用了int类的对象的变量，即n是一个引用
这个int对象的值是3

如下程序：
    print(id(3))
    print(type(3))
    n = 3
    print(id(n))
    print(type(n))

    #输出：
    8791299617088
    <class 'int'>
    8791299617088
    <class 'int'>


###7.隐藏数据域(__variable)
对于类中的隐藏数据，不能由实例化对象访问，即不能使用object.__variable访问
可以使用类中的方法访问，object.getvariable()

    
#*#16 对于一个类型叫做A, A()本身就是它本身的对象，a = A(3)是一个引用了A()类对象的对象
    class A:
        def __init__(self, a):
            self.__a = a
        
        def printa(self):
            print(self.__a)
        
    def main():
        A(3).printa()
    
###9.关于继承的几点注意事项：
(1)子类并不是父类的一个子集。通常，一个子类比它的父类包含更多的信息和方法。
(2)不要为了重用方法盲目的扩建一个类，子类和父类必须是一种关系才有意义。比如，从Person类中扩展Tree子类
则毫无意义。
(3)python允许从几个类派生出一个子类，叫做多重继承。如下：
class Subclass(SuperClass1, SuperClass2, ...)
	initializer
	methods
	
#*#10.覆盖方法(子类和父类使用一样的方法头), 如果在子类中没有用super()调用父类同名函数，则子类同名函数会
#覆盖父类中同名函数

'''
覆盖方法：__str__()
'''
(1)
super()指向父类，super.__init__()调用父类的__init__()
    def __init__(self, c):
        #在子类中用super()调用父类的__init__(),则父类的__init__()方法不会被覆盖
        super().__init__()
        self.__c = c

(2)
    def __str__(self):
        #super().__str__()，则子类的__str__()不会覆盖父类的该方法，可以在子类中同时使用子类的__str__()和父类的
        #该方法
        return super().__str__() + " radius: " + str(radius)
    
(3)
    class Student:
        def __str__(self):
            return "Student"
        def printStudent(self):
            print(self.__str__())

    class GraduateStudent(Student):
         #def __str__(self):
         #   return "GraduateStudent"
        
         def printStudent(self):
            super().printStudent()

    a = Student()
    b = GraduateStudent()
    a.printStudent()
    b.printStudent()

=>
Student
Student #即super().printStudent(),也可以调用用super()普通方法


    class Student:
        def __str__(self):
            return "Student"
         
        def printStudent(self):
            print(self.__str__())
        
    class GraduateStudent:
        def __str__(self):
            return "GraduateStudent"
     
    def main():
        a = Student()
        b = GraduateStudent()
        a.printStudent()
        b.printStudent()
=>
Student
GraduateStudent

'''
动态绑定(覆盖方法，重写父类方法)(dynamic binding)
    工作机制：假设对象o是类C1,C2,C3...Cn-1,Cn的实例，这里的C1是C2的子类，C2是C3的子类，... ，Cn-1是Cn的子类，
也就是说，Cn是最通用的类，C1是最特定的类。在Python中，Cn是object类。如果对象o调用一个方法p，那么Python
会依次在类C1,C2,...,Cn-1,Cn中查找方法p的实现，知道查到为止。一旦找到一个实现，就停止查找然后调用这个第一
次找到的实现。
'''

#*#17. 多态和方法重载的区别
(1)多态：同名方法在不同类中有不同的实现
    class Triangle:
        def __init__(self,width,height):
            self.width = width
            self.height = height
     
        def getArea(self):
            area=self.width* self.height / 2
            return area
     
    class Square:
        def __init__(self,size):
            self.size = size
     
        def getArea(self):    # 同一个方法在不同的类中最终呈现出不同的效果，即为多态
            area = self.size * self.size
            return area
     
def main():    
    a=Triangle(5,5)
    print(a.getArea())
    b=Square(5)
    print(b.getArea())

main()

(2)方法重载：子类在继承父类的基础上，对父类的方法重写


#*#11.object类
在Python中所有定义的类都是object类的子类，object类中包含如下方法：
__new__(): 当创建一个对象时，该方法自动被调用，这个方法随后调用__init__()方法来初始化这个对象。一般只应该覆盖
            __init__()方法来初始化这个新类中定义的数据域。在新类中覆盖object类中__new__()方法，可以返回描述
            该方法的一个字符串
__init__()：该方法只能用于初始化属性，不能返回任何值和使用print()等函数打印值
__str__()：该方法只能用于返回一个描述该对象的一个字符串，不能使用print()等方法，当在一个新类中定义__str__()方法时，object类中的__str__()方法
            被覆盖
__eq__()：x.__eq__(y)，判断x和y两个对象是否相等，相等返回True，不相等返回False。

#如下程序：
    class A:
        def __init__(self, i):
            self.i = i
        
        def __str__(self):
            return "A"
        
        def __eq_(self, other):
            return self.i == other.i
        
    def main():
        x = A(1)
        y = A(1)
        print(x == y)
        print(x)

    main()
=>
False
A

    class A:
        def __init__(self):

#上述方法都在创建对象时就被自动初始化且被调用
    class A:
        def __init__(self):
            self.i = i
        
        def m1(self):
            self.i += 1
        
        #覆盖object类中的__str__()方法
        def __str__(self):
            return "i is" + str(self.i)
            
    def main():
        #在创建对象x时，__str__()方法被初始化且被调用
        x = A(8)
        
        #调用__str__()方法打印当前self.i的值
        print(x) #输出：i is 8


###14.类之间的关系：关联，聚合，继承
(1)关联：一个学生选一门课程是Student和Course类之间的一种关联，一个教员教授一门课是Faculty类和Course类
之间的一种关联。
(2)聚合：是关联的一种特殊形式，它反应了两个对象之间的归属关系。

'''
(1)设计Course类
'''

    class Course:
        def __init__(self, courseName):
            self.__courseName = courseName
            self.__students = []
            
        def getCourseName(self):
            return self.__courseName

        def addStudent(self, student):
            self.__students.append(student)
        
        def dropStudent(self, student):
            self.__students.remove(student)
        
        def getStudents(self):
            return str(self.__students)

        def getNumberOfStudents(self):
            return str(len(self.__students))
        
    def main():
        course1 = Course("Digit Circuit")
        course1.addStudent("Jane")
        course1.addStudent("Mary")
        course1.addStudent("Tom")
        course1.addStudent("Mike")
        print("Course name is: " + course1.getCourseName())
        print("Students name are: " + course1.getStudents())
        print("The Number of student is: " + course1.getNumberOfStudents())
        course1.dropStudent("Tom")
        print("----------------------------------------------------------")
        print("course name is: " + course1.getCourseName())
        print("Now students name are: " + course1.getStudents())
        print("Now the Number of student is: " + course1.getNumberOfStudents())
        
    main()

#输出：
Course name is: Digit Circuit
Students name are: ['Jane', 'Mary', 'Tom', 'Mike']
The Number of student is: 4
----------------------------------------------------------
course name is: Digit Circuit
Now students name are: ['Jane', 'Mary', 'Mike']
Now the Number of student is: 3

'''
(当创建一个Course对象时，就会创建一个列表对象)。一个COurse对象包含一个列表的引用。为了简化
起见，可以认为Course对象包含这个列表。
'''

'''
(2)为栈设计类：栈是一种后进先出的保存数据的数据结构类型
可以使用两种方法来对堆栈进行建模，并且使用列表来存储栈中的元素：
#使用继承：可以定义扩展list类的栈类
#使用组合，可以在Stack类中创建一个列表
#两种方法都可以，但是使用组合会更好，因为这样可以定义一个完整的新栈类而不需要继承list类中不需要的
和不适用的方法。
'''

#created Stack class using compsition
    class Stack:
        def __init__(self):
            self.__elements = []
        
        #Return True if stack is empty
        def isEmpty(self):
            return len(self.__elements) == 0
        
        #Return True if stack is empty, else return the top element of stack
        def peek(self):
            if self.isEmpty():
                return True
            else:
                return self.__elements[len(self.__elements) - 1]
        
        #push a element into stack
        def push(self, element):
            self.__elements.append(element)
        
        #pop the top element and return it
        def pop(self):
            return self.__elements.pop()
        
        #Return the size of stack
        def getSize(self):
            return len(self.__elements)

        #print the size of stack
        def printSize(self):
            print(self.getSize())
            
        #print the top element of stack
        def printTopElement(self):
            print(self.peek())
            
    def main():
        stack = Stack()
        stack.push('a')
        stack.push('b')
        stack.push('c')
        stack.push('d')
        stack.peek()
        stack.printTopElement()
        stack.printSize()
        print("-------------------------------------------------------------------------------")
        stack.pop()
        stack.pop()
        stack.push('e')
        stack.peek()
        stack.printTopElement()
        stack.printSize()
        
    main()

#输出：
d
4
-------------------------------------------------------------------------------
e
3


#*#15当在__init__()中给属性设定了默认值时，不能在创建对象的时候再传入参数的值来修改属性的值，
#因为已经为参数设定了默认值，而不是通过把参数的值传递给属性来修改属性的值，所以不能通过传入参数修改属性的值
#只能通过内部方法修改器setter修改其值

    class Fan:
        def __init__(self, speed, on, radius, color):
            SPEED_SLOW = 1
            self.__speed = SPEED_SLOW
            self.__on = False
            self.__radius = 5
            self.__color = "blue"
            
        def getSpeed(self):
            return str(self.__speed)
        
        def getOn(self):
            return str(self.__on)
        
        def getRadius(self):
            return str(self.__radius)
        
        def getColor(self):
            return self.__color
        
        def setSpeed(self, speed):
            self.__speed = speed
        
        def setOn(self, on):
            self.__on = on
        
        def setRadius(self, radius):
            self.__radius = radius
        
        def setColor(self, color):
            self.__color = color
        
    def main():
        SPEED_SLOW = 1
        SPEED_MEDIUM = 2
        SPEED_FAST = 3
        fan1 = Fan(SPEED_FAST, True, 10, "yellow")
        fan2 = Fan(SPEED_MEDIUM, False, 5, "blue")
        fan1.setSpeed(SPEED_FAST)
        fan1.setOn(True)
        fan1.setRadius(10)
        fan1.setColor("yellow")
        fan2.setSpeed(SPEED_MEDIUM)
        fan2.setOn(False)
        fan2.setRadius(5)
        fan2.setColor("blue")
        print("fan1: ")
        print("speed:" + fan1.getSpeed())
        print("on:" + fan1.getOn())
        print("radius:" + fan1.getRadius())
        print("color:" + fan1.getColor())
        print("--------------------------------------------------------------------------")
        print("fan2: ")
        print("speed:" + fan2.getSpeed())
        print("on:" + fan2.getOn())
        print("radius:" + fan2.getRadius())
        print("color:" + fan2.getColor())
        
    main()

#输出：
fan1: 
speed:3
on:True
radius:10
color:yellow
--------------------------------------------------------------------------
fan2: 
speed:2
on:False
radius:5
color:blue


###18 由于在Python中，变量是弱类型变量，只有在变量被复制的时候才创建它并为它指定一个值，所以在构造方法
#__init__()中，可以在其中写入参数，在创建对象时传入参数的值；也可以不在其中写入参数，而是在属性被赋制
#的时候赋值默认值，并使用修改器修改属性的值
#下例中，A的属性就是__x, __y, __z
    class A:
    def __init__(self):
        self.__x = 3
        self.__y = 4
        self.__z = []
        
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
    def getz(self):
        return self.__z
    
    def setx(self, x):
        self.__x = x
    
    def sety(self, y):
        self.__y = y
        
    def setz(self, element):
        self.__z.append(element)
    
def main():
    a = A()
    print(a.getx())
    print(a.gety())
    a.setx(5)
    a.sety(6)
    print(a.getx())
    print(a.gety())
    a.setz('q')
    a.setz('w')
    a.setz('e')
    print(a.getz())
    
main()
=>
3
4
5
6
['q', 'w', 'e']
