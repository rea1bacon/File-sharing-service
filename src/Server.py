# File sender (server)
#!/usr/bin/python
import socket
from time import sleep



class server:
    def __init__(self,filedesc : list,pwd = None):
        self.accept = True
        self.filedesc = filedesc
        self.pwd = pwd
    
    
    def Close(self):
        # Close connection
        self.accept = False
    
    
    def StartServer(self):
        # Start server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("",0))
        server.settimeout(200)
        server.listen(1)
        print(f"\n🔌 Binded to port {server.getsockname()[1]}")
        while self.accept:
            client, address = server.accept()
            print(f"➡  New connection from {address[0]}")
            self.Handler(client)
        server.close()
    
    
    def Recv(self,client,lg : int):
            while True:
                a = client.recv(lg)
                if a != b"":
                    return a
                
    
    def Handler(self,client):
        HEADER = self.Recv(client,255)
        print(HEADER)
        #Verify header : good protocol
        if HEADER != b"FILE-RECV\n":
            print("❌ bad header ! Operation aborted...")
            self.accept = False
            return 
        if self.pwd != None:
            client.send(b"PWD:REQ\n")
            while True:
                cpwd = str(self.Recv(client,255).decode('utf-8')).strip()
                if cpwd != self.pwd:
                    client.send(b"BAD\n")
                else:
                    client.send(b"GOO\n")
                    break
        else :
            client.send(b"PWD:NO\n")
            
        # Send metadata
        for key,value in self.filedesc.items():
            if key != "buffer":
                kv = bytes(f"{key} {value}\n",'utf-8')
                sleep(0.1)
                print(kv)
                client.send(kv)
            
        if self.Recv(client,255) == b"RECV\n":
            print(f"💌 Starting Transfer of {self.filedesc['name']}...")
            for i in self.filedesc["buffer"]:
                sleep(0.1)
                client.send(i)
            if self.Recv(client,255) == b"DONE\n":
                print("✅ Transfer is done !")
                self.accept = False
                return 
                
                    

            
            
        


