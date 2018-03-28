import socket
server = socket.socket()
server.bind(('localhost',6869))#绑定要监听端口
server.listen()#监听


while True:
	print('等电话中...')
	 
	conn,addr = server.accept()#等电话进来
	#conn就是客户端连过来而在服务器端为其生成的一个连接实例
	# print(conn,addr)
	print('电话来了')
	
	
	while True:
		data = conn.recv(1024)  #最大8192(8k)
		#recv默认是阻塞的
		if not data:
			break
		print('recv:',data.decode())
		conn.send(data.upper())
		
server.close()
	
