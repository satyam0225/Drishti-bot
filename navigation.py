import os
import shutil



def listdir():
    for i in os.listdir():
        for _ in range(3):
            print(i,end="  ")
        print("\n")


def goupdir():
    os.chdir(os.path.dirname(os.getcwd()))

def chdir(dirname):
    os.chdir(dirname)

def cwd():
    return  os.getcwd()

def pwd():
    print(os.getcwd())

def mkdir(dirname):
    os.mkdir(dirname)

def rmdir(dirname):
    os.rmdir(dirname)

def rm(filename):
    os.remove(filename)

def rmnotempty(dirname):
    shutil.rmtree(dirname)