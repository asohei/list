#Required packages:

	nginx
	pyton3
	git
	pip
	virtualenv
	gunicorn

	ex:
		sudo apt-get install nginx git python3 python3-pip
			to install python 3.4 for debian, we need to install from source as of 2014.11
				for sqllike, we need to install some dev packages together.

		sudo pip3 install virtualenv

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
  


