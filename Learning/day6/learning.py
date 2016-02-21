#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
#------------------------------------OS模块-------------------------
import os
# print(os.getcwd()) # 获取当前脚本目录
# os.chdir('test') # 改变当前脚本的工作目录 == cd
# print(os.curdir) # 返回当前目录 ‘.’
# print(os.pardir) # 返回当前目录的父目录 ‘..’
# os.makedirs('test/aa')
# os.removedirs('test/aa') #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推,不为空报错
# os.mkdir('test') #生成单级目录；相当于shell中mkdir dirname 文件存在则报错
# os.rmdir('test')    #删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
print(os.listdir())#列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove('aa.py')#删除一个文件
# os.rename("learn.py","learning.py")# 重命名文件/目录
# print(os.stat('learning.py'))#  获取文件/目录信息
print(os.sep) #    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# os.linesep#    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
# os.pathsep#    输出用于分割文件路径的字符串
# os.name#    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
# os.system("bash command")#  运行shell命令，直接显示
# os.environ#  获取系统环境变量
# os.path.abspath(path)#  返回path规范化的绝对路径
# os.path.split(path)#  将path分割成目录和文件名二元组返回
# os.path.dirname(path)#  返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.basename(path)#  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.exists(path)#  如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)#  如果path是绝对路径，返回True
# os.path.isfile(path)#  如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)#  如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])#  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path)#  返回path所指向的文件或者目录的最后存取时间
# os.path.getmtime(path)#  返回path所指向的文件或者目录的最后修改时间
import xml.etree.ElementTree as ET

# tree = ET.parse("test.xml")
# root = tree.getroot()
# print(root.tag)
# for child in root:
#     print(child.tag, child.attrib)
#     for i in child:
#         print(i.tag,i.text)
# for node in root.iter('year'):
#     print(node.tag,node.text)
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("updated","yes")
#
# tree.write("test.xml")
#删除node
# for country in root.findall('country'):
#    rank = int(country.find('rank').text)
#    if rank > 50:
#      root.remove(country)
#
# tree.write('output.xml')
import xml.etree.ElementTree as ET
# new_xml = ET.Element("namelist")
# name = ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
# age = ET.SubElement(name,"age",attrib={"checked":"no"})
# sex = ET.SubElement(name,"sex")
# sex.text = '33'
# name2 = ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
# age = ET.SubElement(name2,"age")
# age.text = '19'
#
# et = ET.ElementTree(new_xml) #生成文档对象
# et.write("test.xml", encoding="utf-8",xml_declaration=True)
#
# ET.dump(new_xml) #打印生成的格式
a=ET.parse('test.xml')
b=a.getroot()
for i in b:
    print(b.tag,b.attrib)
    for ii in i:
        print(ii.tag,i.text)