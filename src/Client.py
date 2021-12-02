import socket,sys,FileHandler


class client:
    def __init__(self,port: int,ip: str,output):
        self.port = port
        self.ip = ip
        self.output = output
    
    
    def Recv(self,client,lg : int):
            while True:
                a = client.recv(lg)
                if a != b"":
                    return a
    
    def connect(self):
        print(f"🔌 Connecting to {self.ip,self.port}")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((self.ip,self.port))
            self.Handler(client)
        except Exception as e:
            print(e,"❌ Remote host not connected...")
            return
    
    
    def Handler(self,client):
        client.send(b"FILE-RECV\n")
        cpwd = self.Recv(client,7).decode('utf-8').strip()
        if cpwd == "PWD:REQ":
            print("❕ Password required !")
            while True:
                pwd = input("Enter password : ")
                client.send(bytes(pwd+"\n",'utf-8'))
                if self.Recv(client,255) == b"GOO\n": break
                print("❌ Bad password, try again.")
        print("🗒 Reciving metadata...")
        name = self.Recv(client,255).decode('utf-8').strip().split()[1]
        size = self.Recv(client,255).decode('utf-8').strip().split()[1]
        size = int(size)
        ext = self.Recv(client,255).decode('utf-8').strip().split()[1]
        print(f"-File Name : {name}\n-Extension : {ext}\n-File size : {round(size / 10**6,2)} Mb")
        while True:
            conf = input("❔ Proceed to transfer ? (y/n) : ")
            if conf == "y":
                break
            elif conf == "n":
                print("❌ Operation aborted...")
                sys.exit() 
        client.send(b"RECV\n")
        Buffer = b""
        if size % 5000 == 0:
            a = int(size / 5000)
        else:
            a = int(size // 5000) + 1
        
        print("👂 Receiving data...")
        # Setup progress bar
        ach = [" " for i in range(50)]
        for i in range(1,a+1):
            Buffer+=self.Recv(client,5000)
            # i * 100 / a
            Totprg = int((i * 50)/a)
            for j in range(Totprg):
                ach[j] = "="
            print(f"[{''.join(ach)}] {int(Totprg * 2)} %",end="\r")
        print("\n")
        client.send(b"DONE\n")
            
            
            
        writef = FileHandler.Handler(FileName=name if self.output == None else self.output,HexBuffer=Buffer)
        writef.WriteFile()
        
        