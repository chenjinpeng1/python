#多线程的queue： 本身是线程安全的 ，自带锁，多线程中使用
# 多进程的Queue,进程间的数据通信 必须通过multiprocess来导入Queue
#managers 不同进程共享数据，通信 等同 Queue