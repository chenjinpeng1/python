rpc程序执行流程


1、client端Q绑定交换器 ，等待服务端向交换器发送命令
2、server端 向交换器发送命令，通知告知客户端返回的Q，自身先订阅。client接收到数据后执行，将返回结果通过
	服务端告知的Q传送回去
3、服务端循环接收客户端的返回

