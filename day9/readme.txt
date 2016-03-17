#__auth__ chenjinpeng
#程序最初实现在python3 环境下，需安装模块paramiko，yaml
# 主要实现了批量的执行命令以及上传文件功能，实际批量下载用不上，暂为开发
程序结构
    ├── bin
    │   ├── index.py  # 程序入口
    │   └── __init__.py
    ├── conf
    │   ├── conf.yaml # 全区配置文件，yaml格式记录了组，ip，以及用户的账号信息
    │   └── __init__.py
    ├── modules  #
    │   ├── cmd.py  #调用的方法 全在这里
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── cmd.cpython-34.pyc
    │       └── __init__.cpython-34.pyc
    ├── readme.txt
    └── var
        ├── err.log  # 错误记录日志文件
        ├── __init__.py
        └── sys.log  # 正确记录日志文件

    执行前请执行help帮助
        >>> python3 index.py help
        readme帮助
            命令格式一般分为 args[1] 组名 args[2] 方法 args[3] 命令或者其他
    全局执行的命令格式为 group 或者*选1
        >>> python "group | *" cmd.run "command"(执行命令)
        >>> python "group | *" cmd.put "本地路径,远程路径"(上传文件，注意逗号",")

