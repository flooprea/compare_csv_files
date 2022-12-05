import time

print(type(time.time()))

path = rf'C:\Users\florin.oprea\Downloads\compare_files\resultfile.txt'
pth = path.split("\\")
print(pth[-1])