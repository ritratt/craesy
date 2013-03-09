import os,itertools,sys
import sh

def getfiles(userpath):
	filepath=[]
	userpath = os.path.abspath(userpath)
	contents=os.walk(userpath)
	temp = contents
	temp_list=list(temp)
	if len(temp_list)==0:	#This means that either the path points to a single file or a non-existent file/folder.
		try:
			with open(userpath) as f:	
				pass	
			return userpath.split()	#Applied split function to convert the string to a list.
		except IOError:
			print 'Invalid path.'
			sys.exit()

	contents=os.walk(userpath)
	raw_files = contents.next()
	files = sh.ls(str(raw_files[0]), '-R')
	files = str(files).split()
	ff = []
	for i in xrange(len(files)):
		if files[i][-1] == ':':
			folder = files[i][:-1]
			continue
		try:
			sh.cd(folder + '/' + files[i])
			continue
		except OSError:
			ff.append(folder + '/' + files[i])
	return ff

