from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from .forms import SignUpForm,EditUserForm,AcceptFile,WriteCode,AcceptParameters
from . import functions,Compile_Run,AWS_using_boto,configuration
import sys,os

# Create your views here.
def home(request):
    return render(request,'authenticate/home.html',{})

def bucket_list(request):
    buckets = AWS_using_boto.show_buckets()
    return render(request,'authenticate/bucket_list.html',{'buckets':buckets})

def aws_option(request):
    return render(request,'authenticate/aws_option.html',{})

def aws_detail(request): #Not Using this Function
    details=""
    region=""
    if (request.method == 'GET'):
        region = request.GET.get("name")
        print("Name is ", region)
        details = AWS_using_boto.retrieve_instance_from_region(region)
        #return render(request, 'authenticate/aws_detail.html', {'details': details}, {'region': region})
    return render(request, 'authenticate/aws_detail.html', {'details': details,'region':region})

def aws_view(request):
    details = ""
    region = ""
    regions = AWS_using_boto.retrieve_instances()
    if (request.method == 'GET'):
        region = request.GET.get("name")
        print("Name is ", region)
        details = AWS_using_boto.retrieve_instance_from_region(region)
    return render(request, 'authenticate/aws.html', {'regions':regions,'details': details,'region':region})

def azure_view(request):
    return render(request, 'authenticate/azure.html', {})

def run_ide(request):
    if(request.method=='POST'):
        form = WriteCode(request.POST)
        #print (request.POST['results'])
        file_name,file_classname = functions.write_temp_file(request.POST['results'])
        #DIRNAME = os.path.dirname(__file__)
        classpath1 = configuration.CLASSPATH1
        classpath2 = configuration.CLASSPATH2
        upload_path = configuration.UPLOAD_FILES_PATH
        #classpath1, classpath2, upload_path = functions.read_json_file("Java")

        sys.path.insert(0, upload_path)  # Define The Directory To Look For The File
        os.chdir(upload_path)
        parameter_value = request.POST['parameters']
        try:
            Compile_Run.compile_java(classpath1, file_name)
            display = Compile_Run.execute_java(classpath2, file_name,parameter_value)
            #Compile_Run.compile_java('C:\\Program Files\\Java\\jdk-9.0.1\\bin\\javac', file_name)
            #display = Compile_Run.execute_java('C:\\Program Files\\Java\\jdk-9.0.1\\bin\\java', file_name,parameter_value)
            print(display)
            return render(request, "authenticate/display.html", {'display': display})
        except:
            display = "Code has errors. Cannot Execute"
            return render(request, "authenticate/display.html", {'display': display})
        finally:
            os.remove(file_name)
            print(file_classname)
            os.remove(file_classname)
    else:
        form = WriteCode()
    return render(request, 'authenticate/run_ide.html',{'form':form})

def powershell(request):
    if (request.method == 'POST'):
        file = AcceptFile(request.POST, request.FILES)
        parameters = AcceptFile(request.POST['parameters'])
        if (file.is_valid()):
            functions.handle_uploaded_file(request.FILES['file'])
            messages.success(request, 'File Uploaded Successfully')
            file_name = request.FILES['file'].name
            parameter_value = request.POST['parameters']
            file_path=""
            try:
                upload_file = configuration.UPLOAD_FILES_PATH
                #upload_file = functions.read_json_file("Powershell")
                file_path = upload_file + "\\"+file_name

                #file_path = "G:\Romu\PycharmProjects\\"+file_name
                display = Compile_Run.run_powershell(file_path, parameter_value)
                return render(request, "authenticate/display.html", {'display': display})
            except:
                display = "Code has errors. Cannot Execute"
                return render(request, "authenticate/display.html", {'display': display})
            finally:
                os.remove(file_path)
    else:
        file = AcceptFile()
    return render(request, "authenticate/powershell.html", {'form': file})

def java_options(request):
    return render(request, 'authenticate/JavaOptions.html', {})

def execution_page_java(request):

    file_name = request.GET.get("name")
    print("Name is ", file_name)
    if (request.method == 'POST' and 'save_submit' in request.POST):
        param = AcceptParameters(request.POST)
        classpath1 = configuration.CLASSPATH1
        classpath2 = configuration.CLASSPATH2
        upload_path = configuration.UPLOAD_FILES_PATH
        #classpath1, classpath2, upload_path = functions.read_json_file("Java")
        sys.path.insert(0, upload_path)  # Define The Directory To Look For The File
        os.chdir(upload_path)
        parameter_value = request.POST['parameters']
        print (file_name)
        file_classname, ext = os.path.splitext(file_name)
        file_classname = file_classname + ".class"
        try:
            Compile_Run.compile_java(classpath1, file_name)
            display = Compile_Run.execute_java(classpath2, file_name, parameter_value)
            # Compile_Run.compile_java('C:\\Program Files\\Java\\jdk-9.0.1\\bin\\javac', file_name)
            # display = Compile_Run.execute_java('C:\\Program Files\\Java\\jdk-9.0.1\\bin\\java', file_name, parameter_value)
            print(display)
            return render(request, "authenticate/display.html", {'display': display})
        except:
            display = "Code has errors. Cannot Execute"
            return render(request, "authenticate/display.html", {'display': display})
    else:
        param = AcceptParameters()
    return render(request, "authenticate/execution_page_java.html", {'form': param,'program':file_name})


def execute_java(request):
    L = functions.get_list_of_java_files()
    if (request.method == 'POST'):
        return render(request, 'authenticate/execution_page_java.html', {})
    return render(request, 'authenticate/execute_java.html', {'List':L})

def display_java(request):
    return render(request, 'authenticate/display.html', {})

def run_java(request):
    if(request.method=='POST' and 'save_submit' in request.POST):
        file = AcceptFile(request.POST,request.FILES)
        #AcceptFile(request.POST['parameters'])
        param = AcceptParameters(request.POST)
        #print(param)
        if(file.is_valid()):
            functions.handle_uploaded_file(request.FILES['file'])
            messages.success(request, 'File Uploaded Successfully')
            classpath1 = configuration.CLASSPATH1
            classpath2 = configuration.CLASSPATH2
            upload_path = configuration.UPLOAD_FILES_PATH
            #classpath1,classpath2,upload_path = functions.read_json_file("Java")

            sys.path.insert(0, upload_path)  # Define The Directory To Look For The File
            os.chdir(upload_path)
            #sys.path.insert(0, "G:\Romu\PycharmProjects")           #Define The Directory To Look For The File
            #os.chdir("G:\Romu\PycharmProjects")

            file_name = request.FILES['file'].name
            parameter_value = request.POST['parameters']

            file_classname, ext = os.path.splitext(file_name)
            file_classname = file_classname+".class"
            try:
                Compile_Run.compile_java(classpath1, file_name)
                display = Compile_Run.execute_java(classpath2,file_name,parameter_value)

                #Compile_Run.compile_java('C:\\Program Files\\Java\\jdk-9.0.1\\bin\\javac', file_name)
                #display = Compile_Run.execute_java('C:\\Program Files\\Java\\jdk-9.0.1\\bin\\java', file_name, parameter_value)
                print(display)
                return render(request, "authenticate/display.html", {'display': display})
            except:
                display = "Code has errors. Cannot Execute"
                return render(request, "authenticate/display.html", {'display': display})
            '''finally:
                os.remove(file_name)
                os.remove(file_classname)'''
    elif(request.method=='POST' and 'save' in request.POST):
        file = AcceptFile(request.POST, request.FILES)
        param= ""
        AcceptFile(request.POST['parameters'])
        if (file.is_valid()):
            functions.handle_uploaded_file(request.FILES['file'])
            messages.success(request, 'File Uploaded Successfully')
            return redirect("JavaOptions")
    else:
        file = AcceptFile()
        param = ""
        #param= AcceptParameters()
    return render(request, "authenticate/run_java.html", {'form': file,'param':param})

def login_user(request):

    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Logged in successfully')
            return redirect('home')
        else:
            messages.success(request,'Failed to Log in! Try again...')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('home')

def register_user(request):
    if(request.method=='POST'):
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request, 'Successfully registered')
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'authenticate/register.html', context)

def edit_profile(request):
    if (request.method == 'POST'):
        form = EditUserForm(request.POST,instance=request.user)
        if (form.is_valid()):
            form.save()
            messages.success(request, 'You have successfully edited your profile')
            return redirect('home')
    else:
        form = EditUserForm(instance=request.user)
    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)

def change_password(request):
    if (request.method == 'POST'):
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if (form.is_valid()):
            form.save()
            messages.success(request, 'You have successfully changed your password')
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)