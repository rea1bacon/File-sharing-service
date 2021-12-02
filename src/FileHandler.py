# Handle File read and write
#!/usr/bin/python
import os
from pathlib import *



class Handler:
    def __init__(self,FileName = None, Path=None,HexBuffer = None):
        self.FileName = FileName
        self.path = Path
        self.HexBuffer = HexBuffer
    
    def ReadFile(self):
        """
        Read the file and return 
        file attributes
        buffer : content encoded in hex
        name : filename
        size : file size
        ext : file extension
        """
        self.FileName = PurePath(self.path).parts[-1]
        if os.path.isfile(self.path):
            with open(self.path,"rb") as file:
                Raw = file.read()
                HexBuffer = []
                for i in range(0,len(Raw),5000):
                    HexBuffer.append(Raw[i:i+5000])
                return True,{"buffer":HexBuffer,
                        "name":self.FileName,
                        "size" : len(Raw),
                        "ext" : Path(self.path).suffix
                }
        else:
            return False,f"❌ No file name {self.path}"
    
    
    def WriteFile(self):
        """
        Write the file in binary format
        """
        if os.path.isfile(self.FileName):
            c = input("❕ File alrady exist, do you want to overwrite ? y/n : ")
            if c == "y" : 
                pass
            elif c == "n":
                print("❌ Operation aborted...")
                return 
        with open(self.FileName,"wb") as file:
            print(f"⏬ Writing File : {self.FileName}...")
            file.write(self.HexBuffer)
            file.close()
            print(f"✅ File {self.FileName} saved !")

