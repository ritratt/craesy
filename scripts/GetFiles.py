import os,itertools,sys

def getfiles(userpath):
	filepath=[]
	contents=os.walk(userpath)
	temp = contents
	temp_list=list(temp)
	#print temp_list
	if len(temp_list)==0:	#This means that either the path points to a single file or a non-existent file/folder.
		try:
	#		print userpath
			with open(userpath) as f:	
				print 'File found.'
			return userpath.split()	#Applied split function to convert the string to a list.
		except IOError:
			print 'Invalid path.'
			sys.exit()

	contents=os.walk(userpath)
	for folder in contents:
		for fileonly in folder[2]:
			filepath.append(str(folder[0])+'/'+str(fileonly))
	#		print filepath
	if (len(filepath)==0):
		print 'No files to encrypt in the given folder.'
		sys.exit()
	return filepath


