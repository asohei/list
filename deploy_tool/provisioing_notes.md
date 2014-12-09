#Required http server setting

	nginx 
	setup sites-available and create ln -s to sites-enabled

#Tested python version

	3.4.2

	As of 2014.11, installking python3.4.2 on debian required source instllation together witl some dev packages manually.

#Requred Python Package

	Installed thru fabfile.py
		or pip install -r requirements.txt 



#Nginx virtual hosting config

see "list-stagin.t23.jp" file's top part comments.

# deamon process

see "list-staging" script file's top part comments.


# server folder structure

/home/username
- sites
  - list-staging.t23.jp
    - database
    - source
    - static
    - v-python3.4
  


