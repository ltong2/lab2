import socket,sys
try:
    import thread
except ImportError:
    import _thread
def clientthread(conn):
    #code here
    #while..
    while True:
        #conn,addr=s.accept()
        data = conn.recv(1024)
        if not data:
            break   

        data2=str(data)
        data2=data2[0:len(data2)-1]
        reply= '<Hello '+data2+'\n'+'>'
        conn.sendall(reply.encode("UTF-8"))
    
    
    
try:
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    sys.exit()

host=""
port =8888
try:
    s.bind((host,port))
except socket.gaierror as msg:
    sys.exit()
s.listen(5)

while 1:
    conn,addr=s.accept()
    thread.start_new_thread(clientthread,(conn,))
    
conn.close()
s.close()