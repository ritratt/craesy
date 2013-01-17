all:	base
	sudo yum install python
	sudo apt-get install python
	sudo yum install pip
	sudo apt-get install python-pip
base:	
	pip install pbkdf2
	pip install pycrypto
	sudo sh install.sh
