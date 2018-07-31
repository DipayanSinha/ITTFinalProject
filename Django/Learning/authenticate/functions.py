import string
import glob
import os
from . import configuration

def handle_uploaded_file(f): #Storing Files in Directory
    with open(configuration.FILE_STORE_PATH + f.name, 'wb+') as destination:
    #with open('G:\Romu\PycharmProjects\\'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def write_temp_file(str):
    list_of_strings = str.split()
    if(["public","class"] in list_of_strings):
        i = list_of_strings.index("class")
    else:
        i = list_of_strings.index("class")
    f_name = list_of_strings[i+1]+".java"
    f_classname = list_of_strings[i+1]+".class"
    f = open(configuration.FILE_STORE_PATH + f_name, "w+")
    #f = open("G:\\Romu\\PycharmProjects\\"+f_name, "w+")
    f.write(str)
    f.close()
    return f_name,f_classname

def get_list_of_java_files():
    files_names = []
    for file in glob.glob(configuration.FILE_STORE_PATH + "*.java"):
    #for file in glob.glob('G:\\Romu\\PycharmProjects\*.java'):
        files_names.append(os.path.relpath(file, configuration.UPLOAD_FILES_PATH))
        #files_names.append(os.path.relpath(file, "G:\\Romu\\PycharmProjects"))
    return files_names
    #return glob.glob("G:\\Romu\\PycharmProjects\*.java")

#get_list_of_java_files()