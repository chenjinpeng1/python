#!/usr/bin/env python
# -*- coding:utf-8 -*-
#auth _*_ chenjinpeng _*_

def fetch(backend):
    result = []
    with open('db1','r',encoding='utf-8') as f:
        flag= False
        for line in f:
            if line.strip().startswith("backend") and  line.strip() == "backend "+ backend:
                flag=True
                continue
            if flag and line.strip().startswith('backend'):
                flag=False
                break
            if flag and line.strip():
                result.append(line.strip())
    return result
ret=fetch('www.oldboy.org')
def add(backend,record):
    record_list=fetch(backend)
    if not record_list:
        #backend 不存在
        with open('db1','r')as old,open('db2','w')as new:
            for line in old:
                new.write(line)
            new.write("\nbackend " + backend + "\n")
            new.write(" " * 8 + record + "\n")

    else:
        # backend 存在
        if record in record_list:
            #record已经存在
         pass
        else:
            #backend存在，record不存在
            record_list.append(record)
            with open('db1','r')as old,open('db2','w')as new:
                flag=False
                for line in old:
                    if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                        print(line.strip())
                        flag=True
                        new.write(line)
                        for new_line in record_list:
                            new.write(" " * 8 + new_line + "\n")
                            print(new_line)
                        continue
                    if flag and line.strip().startswith('backend'):
                        flag=False
                        new.write(line)
                        continue
                    if line.strip() and not flag: 
                        new.write(line)


bk = "www.oldboy.org"
rd = "server 100.1.7.29 100.1.7.29 weight 20 maxconn 30"
add(bk,rd)
