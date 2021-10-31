import sys
import struct

# currently the classes are written for x64 binaries
class ExecutableHeader():
    def __init__(self, data: bytes):
        self.e_ident = {
            'magic_value': data[:4].hex(),
            'ei_class': data[4:5].hex(),
            'ei_data': data[5:6].hex(),
            'ei_version': data[6:7].hex(),
            'ei_osabi': data[7:8].hex(),
            'ei_abiversion': data[8:9].hex(),
            'ei_pad': data[9:16][::-1].hex()
        }
        self.e_type = data[16:18][::-1].hex()
        self.e_machine = data[18:20][::-1].hex()
        self.e_version = data[20:24][::-1].hex()
        self.e_entry = data[24:32][::-1].hex()
        self.e_phoff = data[32:40][::-1].hex()
        self.e_shoff = data[40:48][::-1].hex()
        self.e_flags = data[48:52][::-1].hex()
        self.e_ehsize = data[52:54][::-1].hex()
        self.e_phentsize = data[54:56][::-1].hex()
        self.e_phnum = data[56:58][::-1].hex()
        self.e_shentsize = data[58:60][::-1].hex()
        self.e_shnum = data[60:62][::-1].hex()
        self.e_shstrndx = data[62:64][::-1].hex()

class ELF():
    def __init__(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
        except Exception as e:
            print(f"[!] Couldn't read file: {file_path}. Error: {repr(e)}")
            sys.exit(1)

        self.executable_header = ExecutableHeader(data)
        
        