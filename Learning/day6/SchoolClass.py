#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
#!/usr/bin/env python
# -*- coding:utf-8 -*-
class SchoolMember(object):
    member_nums = 0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()
    def enroll(self):
        SchoolMember.member_nums +=1
        print("\033[32;1mThe [%s] school member [%s] is enrolled!\033[0m" %(self.member_nums,self.name))

    def tell(self):
        print("Hello my name is %s" %self.name)
class Teacher(SchoolMember):
    def __init__(self,name,age,sex,course,salary):
        super(Teacher,self).__init__(name,age,sex)
        self.course = course
        self.salary = salary
        #SchoolMember.__init__(self,name,age,sex)
    def teaching(self):
        print("Teacher [%s] is teaching [%s]" %(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,course,tuition):
        super(Student,self).__init__(name,age,sex)
        self.course = course
        self.tuition = tuition
    def pay_tution(self):
        print("cao ,student [%s] paying tution [%s]" %(self.name,self.tuition))

t1 = Teacher("Alex",22,'F',"PY",1000)
t2 = Teacher("Tenglan",25,'N/A',"PY",900)
s1 = Student("SanJiang",24,"Female","python",15000)
s2 = Student("BaoAn",23,"F","python",5000)

t1.tell()
t1.teaching()
s1.tell()
s1.pay_tution()

# 至少 有2个不同的角色
# 玩的过程 中必须 要有冲突
# 根据不同的交互产生不同的行为
# 让用户可以玩么
# 一定要用到面向对象编程的语法及思想


