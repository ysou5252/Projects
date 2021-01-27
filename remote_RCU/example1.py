import socket as s

srcAddr = input("아두이노의 IP를 입력해주세요(ex. 127.0.0.1) : ")
srcPort = int(input("Port를 입력해주세요(ex. 80) : "))

sock = s.socket() #기본값 TCP
sock.connect((srcAddr, srcPort)) #서버에 연결시도
sock.send("1".encode())#데이터를 하나라도 보내야지 반응함, 바이트 배열로로 인코딩함
recvData = sock.recv(1024) #데이터를 최대 1024바이트 만큼 읽어들임
print(recvData.decode())# 받은 데이터를 디코딩해서 보여줌
sock.close() #연결 닫음


