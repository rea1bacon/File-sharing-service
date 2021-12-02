#!/usr/bin/python
import FileHandler, Server, os, argparse, Client



parser = argparse.ArgumentParser(description='File Transfer application')
parser.add_argument('--recv', action='store_true',help='Launch in receiver mode')
parser.add_argument('--send', action='store_true',help='Launch in sender mode')
parser.add_argument('-pwd', type=str,help='Use a password (optionnal)')
parser.add_argument('-adr', type=str,help='Remote host to connect to')
parser.add_argument('-port',type=int,help='Port to connect to')
parser.add_argument('-f',type=str,help='Path/to/file')
parser.add_argument('-o',type=str,help='Output location')


args = parser.parse_args()

if __name__ == "__main__":
    if args.send and args.f != None:
        file = args.f
        SUCCESS,filedesc = FileHandler.Handler(Path=file).ReadFile()
        if SUCCESS:
            server = Server.server(filedesc,args.pwd)
            server.StartServer()
        else:
            print(filedesc)
    
    elif args.recv:
        if args.port != None and args.adr != None:
            client = Client.client(args.port,args.adr,args.o)
            client.connect()
            
    