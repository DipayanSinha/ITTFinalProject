import string
import json
import glob
import os

def handle_uploaded_file(f): #Storing Files in Directory
    data = read_json_file(choice="")
    with open(data['file_store_path'] + f.name, 'wb+') as destination:
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
    data = read_json_file(choice="")
    f = open(data['file_store_path'] + f_name, "w+")
    #f = open("G:\\Romu\\PycharmProjects\\"+f_name, "w+")
    f.write(str)
    f.close()
    return f_name,f_classname

def read_json_file(choice):
    with open('G:\Romu\PythonOnWeb\Learning\\authenticate\Classpath.json') as data_file:    #Need to change
        data = json.load(data_file)
        if(choice=="Java"):
            return read_Java(data)
        elif (choice == "Powershell"):
            return (data["upload_files_path"])
        else:
            return data

def read_Java(data):
    return (data['classpath1'], data['classpath2'], data['upload_files_path'])

def read_Powershell(data):
    return (data["upload_files_path"])

'''def read_json_file(choice):
    with open('G:\Romu\PycharmProjects\Learning\\authenticate\Classpath.json') as data_file:    #Need to change
        data = json.load(data_file)
        if (choice=="Java"):
            print(data['classpath1'],data['classpath2'],data["upload_files_path"])
            return (data['classpath1'],data['classpath2'],data['upload_files_path'])
        elif (choice=="Powershell"):
            return (data["upload_files_path"])
'''
def get_list_of_java_files():
    files_names = []
    data = read_json_file(choice="")
    for file in glob.glob(data["file_store_path"]+"*.java"):
    #for file in glob.glob('G:\\Romu\\PycharmProjects\*.java'):
        files_names.append(os.path.relpath(file, data["upload_files_path"]))
        #files_names.append(os.path.relpath(file, "G:\\Romu\\PycharmProjects"))
    return files_names
    #L = (glob.glob("G:\\Romu\\PycharmProjects\*.java"))
    #return glob.glob("G:\\Romu\\PycharmProjects\*.java")

get_list_of_java_files()