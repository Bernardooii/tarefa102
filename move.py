import os
import shutil

from_dir = "C:/Users/User/OneDrive/Documentos/Projetos/tarefa102"
to_dir = "C:/Users/User/OneDrive/Documentos/Projetos/tarefa102/Arquivos"

list = os.listdir(from_dir)
#print(list)
os.mkdir("ArquivosGif")

for i in list:
    name,extension=os.path.splitext(i)
    if extension=="":
        continue
    if extension in [".gif"]:
        path1 = from_dir + "/" + i
        #print("path1",path1)
        path2 = to_dir + "/ArquivosGif"
        path3 = to_dir + "/ArquivosGif/" + i
        if os.path.exists(path2):
            print("Movendo o arquivo ", name)
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("Movendo o arquivo ", name)
            shutil.move(path1, path3)


list1 = os.listdir(from_dir)
#print(list1)
os.mkdir("Arquivos")

for a in list1:
    name,extension=os.path.splitext(a)
    if extension=="":
        continue
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir +"/" + a
        #print("path1",path1)
        path2 = to_dir + "/Arquivos"
        path3 = to_dir + "/Arquivos/" + i
        if os.path.exists(path2):
            print("Movendo o arquivo ", name)
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("Movendo o arquivo ", name)
            shutil.move(path1, path3)


