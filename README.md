# ITTFinalProject

----------------
Overview
----------------
This Django Project has 3 different functionalities.
  - Upload and Run Java Program files.
  - Upload and Run Powershell files.
  - Monitor the AWS EC2 instances and S3 buckets in different regions.
  
----------------
Installation
----------------

----------------
Prerequisites
----------------

  - Pycharm Professional Edition
  - Python 3.6

  - Create a folder named PythonOnWeb in G Drive (or any other drive) and clone the project there

----------------
Edit the Configuration file: congiguration.py
----------------

  - CLASSPATH1 = "C:\\Program Files\\Java\\jdk1.8.0_171\\bin\\javac"
  - CLASSPATH2 = "C:\\Program Files\\Java\\jdk1.8.0_171\\bin\\java"
Put the absolute path of JDK on disk

The Django Project "Learning" and all other Java, Powershell files should be in this directory. Modify the path as required. 
Note: Do not change the forward slashes format otherwise the program won't work.
  - UPLOAD_FILES_PATH = "G:\\PythonOnWeb"
  - FILE_STORE_PATH = "G:\\PythonOnWeb\\"

Enter the AWS Credentials in ACCESS_KEY and SECRET_KEY to run AWS monitoring functionality
  - ACCESS_KEY = ""
  - SECRET_KEY = ""

----------------
Run the project
----------------
  
  To install all the requirement files run:  pip install -r requirements.txt 
   - python manage.py makemigrations
   - python manage.py migrate
   - start server using the command: python manage.py runserver
   
----------------
Create superuser
----------------

Create a superuser or access the Django management shell.
  - python manage.py runserver
  - start server again and access django admin using below url:
  - http://127.0.0.1:8000:8000/admin/login/?next=/admin/
  - provide username/password and access Django admin
   
 
