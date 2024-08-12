import os
import tarfile

def extract_tar(file):
    with tarfile.open(file, "r:xz") as tar:
        tar.extractall()

oldfile = "Es9ZY.tar.xz"
all_txt_files = []
unique_txt=set([])
counter=1
extract_tar(oldfile)

while True:
    checktar = False
    with open("same.txt","r") as f:
        content=f.read()
        all_txt_files.append(str(counter)+": "+content)
        unique_txt.add(content)
    os.remove("same.txt")
    counter+=1
    listfilename=os.listdir()
    for item in listfilename:
        if item.endswith(".tar.xz") and item!=oldfile:
            extract_tar(item)
            os.remove(item)
            checktar = True
            break
    if not checktar:
        break

with open("output.txt","w") as f:
    for item in all_txt_files:
        f.write(item)
with open("passwords.txt","w") as f:
    for item in unique_txt:
        f.write(item)