#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import time,sys
for i in range(10):
    sys.stdout.write("\r#####%s"%i)
    sys.stdout.flush()
    time.sleep(0.5)