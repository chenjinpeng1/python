#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
class SchoolMember(object): #学院成员类
    member_nums = 0  # 类变量 | 类属性
    def __init__(self,name,age,sex): # 初始化默认方法
        self.name = name  # 实例属性 | 成员属性 （self 调用自己的属性）
        self.age = age
        self.sex = sex
        self.enroll()   # 自动调用注册方法
    def enroll(self):
        SchoolMember.member_nums += 1 #注册人数加1
        print('The [%s]school member [%s] is enrolled'%(self.member_nums,self.name))
    def tell(self):
        print('Hello,my name is [%s]'%self.name)
class Teacher(SchoolMember):  # Teacher继承SchoolMember的属性
    def __init__(self,name,age,sex,course,selary): # 重写自己的属性
        super(Teacher,self).__init__(name,age,sex)  # 继承学院成员的属性
        # SchoolMember.__init__(self,name,age,sex)   #老式经典继承方法
        self.course = course
        self.selary = selary
    def teaching(self):
        print('Teaching [%s] is teaching [%s]，selary [%s]'%(self.name,self.course,self.selary))
class Student(SchoolMember):  # Student继承SchoolMember的属性
    def __init__(self,name,age,sex,course,tuition):
        super(Student,self).__init__(name,age,sex)
        self.course = course
        self.tuition = tuition
    def pay_tuition(self):
        print('student [%s] paying tuition [%s]'%(self.name,self.tuition))

# 实例化类 （把一个抽象的类变成一个具体的对象的过程叫做实例化）
t1 = Teacher('chen','24','men','PY','15000')
t2 = Teacher('Alex','28','men','PY','10000')
S1 = Student('SanJiang','22','women','Python','15000')
S2 = Student('LuNan','18','men','Python','10000')

t1.tell()
t1.teaching()
S1.tell()
S1.pay_tuition()

