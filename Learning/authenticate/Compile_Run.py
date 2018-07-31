import os.path,subprocess
from subprocess import STDOUT,PIPE


def compile_java(CLASSPATH,java_file):
    #subprocess.check_call(['javac', java_file])
    subprocess.check_call([CLASSPATH, java_file])

def execute_java(CLASSPATH2,java_file, stdin):

    java_class,ext = os.path.splitext(java_file)
    cmd = [CLASSPATH2, java_class]
    proc = subprocess.Popen(cmd, stdin=PIPE,stdout=PIPE, stderr=STDOUT,encoding='utf-8')
    stdout,stderr = proc.communicate(stdin)
    print ('This was "' + stdout + '"')
    return stdout

def run_powershell(powershell_file,stdin):
    p = subprocess.Popen(["powershell.exe", powershell_file], stdin=PIPE, stdout=PIPE,
                         stderr=STDOUT,encoding = 'utf-8')
    stdout, stderr = p.communicate(stdin)
    print(stdout)
    return stdout

#run_powershell("G:\\Romu\\Internship\\'In Time Tec'\\Test.ps1","")
#compile_java('C:\\Program Files\\Java\\jdk-9.0.1\\bin\\javac','Hi.java')
#execute_java('C:\\Program Files\\Java\\jdk-9.0.1\\bin\\java','Hi', 'Jon')
