import os,itertools

class GetFiles(object):
	def __init__(self,userpath):
		print userpath
		filepath=[]
		contents=os.walk(userpath)
		for folder in contents:
			for fileonly in folder[2]:
				filepath.append(str(folder[0])+'/'+str(fileonly))
		return filepath

