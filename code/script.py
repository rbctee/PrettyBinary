from classes import ELF

path = "/tmp/file.elf64"
elf = ELF(path)

print(elf.executable_header.__dict__)