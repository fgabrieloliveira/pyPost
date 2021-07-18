# pyPost
A simple newspapper site made with django.

## How run it

### Installing the requirements
If you're on linux, make sure that you have installed the python 3 and mysql headers and libraries before install the requirements. If not, run the following command on the terminal:

Debian and derivates
```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

Red hat / CentOS
```
sudo yum install python3-devel mysql-devel
```

Now you can install the requirements, run the following on the same directory that "requirements.txt":
```
pip install -r requirements.txt
```
### Configuring the database

You'll need a mySql server. You can find how to do it online. Assuming that you have already did that, go to settings.py and change the user, password and db name on "DATABASES=", according to your mysql configuration.

### Runing the development server

To run this application on development mode, open the terminal in the directory where "manage.py" is and run the following command:
```
python manage.py runserver
```