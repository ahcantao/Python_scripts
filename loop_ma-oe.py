#This script will run while the C:\ disk has any space left
#used for educational purposes only
import os
path = "C:/temp/"

if not os.path.exists(path):
    os.makedirs(path)
with open(path + "rodando.txt", "a") as f:  
    while 1>0:
        f.write("rodando, ma oe!\n")