import socket,random,string,redis 
         
ip = '127.0.0.2' 
port = 3128
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((ip, port))        
s.listen(5)
conn,addr = s.accept()

########GeneratingRandomString
def randomString(stringLength=64):
	letters = string.ascii_letters
	return ''.join(random.choice(letters) for i in range(stringLength))	
#print(randomString(64))

########STORINGRANDOMSTRINGTOREDISMEMORYCACHE
r = redis.Redis()
kirim = randomString(64)
r.set("serversend",kirim)
#print(r.get("serversend"))

########SendingRandomString
conn.send(kirim.encode())
print ("random string transmitted succesfully\n")

########ReceivingStringFromClient
pesan = conn.recv(100)
print("string from client",pesan,"\n")

#########CheckingStringFromClientWithStoredStringinRedis
if r.get("serversend")==pesan :
	conn.send(b'true')
	print("true")
else :
	conn.send(b'false')
	print ("false")
