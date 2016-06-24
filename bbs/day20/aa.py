#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
if __name__ == '__main__':

    s = set()
    s.add("aaaaa")
    s.add("bbbbbb")
    # print(s)
    with open("tzc.txt", 'w', encoding="utf-8") as f:

        for i in s:
            print(i)
            write_value = "%scccccc\n" % i
            print(write_value)
            f.write(write_value)
            f.write("eeee")
            f.write("dddd")