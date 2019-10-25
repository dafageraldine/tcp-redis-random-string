import socket

ip = '127.0.0.2'
port = 3128
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
print("connected to the server\n")

#################receivingrandomstring
pesan = s.recv(100)
print("random string from server",pesan,"\n")

#################resendthestring
s.send(pesan)

#################feedbacktrueorfalsefromserver
pesan2 = s.recv(5)
print(pesan2)