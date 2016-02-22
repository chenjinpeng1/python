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
# print(os.listdir())#列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove('aa.py')#删除一个文件
# os.rename("learn.py","learning.py")# 重命名文件/目录
# print(os.stat('learning.py'))#  获取文件/目录信息
# print(os.sep) #    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
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
# import xml.etree.ElementTree as ET

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
# import xml.etree.ElementTree as ET
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
# a=ET.parse('test.xml')
# b=a.getroot()
# for i in b:
#     print(b.tag,b.attrib)
#     for ii in i:
#         print(ii.tag,i.text)


# import configparser
#
# config = configparser.ConfigParser()
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                       'Compression': 'yes',
#                      'CompressionLevel': '9'}
# config["aaa"] = {'ServerAliveInterval': '45',
#                       'Compression': 'yes',
#                      'CompressionLevel': '9'}
#  # 第二种写入方式
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
#
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'     # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('example.ini', 'w') as configfile:
#    config.write(configfile)
# #
# import configparser
# config=configparser.ConfigParser()
# print(config.sections())
#
# config.read('example.ini')
#
# print('bitbucket.org' in config)
# print(config['bitbucket.org']['user'])
# print(config['DEFAULT']['Compression'])
# topsecret = config['topsecret.server.com']
# print(topsecret['forwardX11'])
# print(topsecret['host port'])
# for key in config['bitbucket.org']: print(key)
# print(config['bitbucket.org']['ForwardX11'])
#
#
# import configparser
#
# config = configparser.ConfigParser()
# config.read('example.ini')
#
#
# # ########## 移除全部类似1层keys ##########
# sec = config.remove_section('aaa')
# config.write(open('example2.ini', "w"))
# # ######### 增加 ##########
# sec = config.has_section('wupeiqi') # 查询如果没有就增加
# sec = config.add_section('wupeiqi')
# config['wupeiqi']['age'] = '21'
# config.write(open('example2.ini', "w"))
#
# # ######## 修改 #########
# config.set('wupeiqi','age','22')
# config.write(open('example2.ini', "w"))
# # ######  删除2层keys
# config.remove_option('wupeiqi','age')
# config.write(open('example2.ini', "w"))


# import hashlib
# ######## md5 ########
#
# a = hashlib.md5()
# a.update(b'Hello')
# a.update(b'It,s me')
# print(a.digest())  # 2禁制格式
# print(a.hexdigest()) # 16禁制格式
# a.update(b'aaaaaaaaaaaaaaa')
# print(a.hexdigest())
#
# # ######## sha1 ########
#
# hash = hashlib.sha1()
# hash.update(b'admin')
# print(hash.hexdigest())
#
# # ######## sha256 ########
#
# hash = hashlib.sha256()
# hash.update(b'admin')
# print(hash.hexdigest())
#
#
# # ######## sha384 ########
#
# hash = hashlib.sha384()
# hash.update(b'admin')
# print(hash.hexdigest())
#
# # ######## sha512 ########
#
# hash = hashlib.sha512()
# hash.update(b'admin')
# print(hash.hexdigest())


# import hmac

# #一般更多用于消息加密，
# import hmac
# h = hmac.new('wueiqi')
# h.update('hellowo')
# print (h.hexdigest())


import subprocess
# a=subprocess.run('ipconfig');print(a) # 调用系统命令.返回显示值 3.5以前不支持
# subprocess.call('ipconfig')## 在3.5以前的版本中 该写法会报错。多一个参数,只能如下格式
# subprocess.call(['df','-h'])
#或者
# subprocess.call('df -h',shell=True)

# a=subprocess.call('ipconfig');print(a) #3.5以前调用系统命令这样写,但是返回的是返回值，而不是命令执行结果（显示值），若想打印显示值则：
# a=subprocess.Popen('ipconfig',stdout=subprocess.PIPE) #3.5以前的版本
# print(a.stdout.read())   # 打印ipconfig的显示结果而不是打印返回值



# a=subprocess.Popen('df -h',shell=True,stdout=subprocess.PIPE);print(a.stdout.read())
'''
打印执行命令的显示，而不是返回结果（stdout=subprocess.PIPE）表示管道符，意将显示通过管道符传入，
然后通过a.stdout.read()打印出来显示
'''
'''
>>>subprocess.call('sdf',shell=True)# 报错
/bin/sh: sdf: command not found
127
subprocess.check_call('sdf',shell=True)  抛出异常
/bin/sh: sdf: command not found
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib64/python2.6/subprocess.py", line 505, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command 'sdf' returned non-zero exit status 127
'''
# import subprocess
#
# obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# obj.stdin.write("print ('hello')")
# obj.stdin.write("print ('hello1')")
# obj.stdin.write("print ('hello2')")
# obj.stdin.write("print ('hello3')")
#
# out_error_list = obj.communicate(timeout=10)
# print (out_error_list)


import logging

#create logger
logger = logging.getLogger('TEST-LOG') #公开接口
logger.setLevel(logging.DEBUG) # 默认级别


# create console handler and set level to debug
ch = logging.StreamHandler()  #输出到屏幕
ch.setLevel(logging.DEBUG)

# create file handler and set level to warning  # 输出到文件
fh = logging.FileHandler("access.log")
fh.setLevel(logging.WARNING)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # 规定输出格式

# add formatter to ch and fh
ch.setFormatter(formatter) #哪个对象应用上述格式
fh.setFormatter(formatter)#哪个对象应用上述格式

# add ch and fh to logger
logger.addHandler(ch) #应用到接口
logger.addHandler(fh)#应用到接口

# 'application' code # 输出日志信息
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')


