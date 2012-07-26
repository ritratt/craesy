all:	craesy
	sudo yum install python

craesy:	pbkdf2
	pip install pbkdf2
pbkdf2:	pip
	$ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

pip:	
	sudo sh install.sh
	
