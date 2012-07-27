import os,itertools

global filepath=[]
class FoF(object):
	
	def __init__(self,path):
#		filepath=[]
		filepath=filepath.append(self.FileOrFolder(path))
		print filepath
	
	def FileOrFolder(path):
		temp=path
		path_length=len(list(temp))
		if(path_length==0):
			#This means the path given is a file, not folder.
			return path
		else:
			temp=path
			for i in temp:
				if(len(i[1]) == 0 and len(i[2]) == 0):
					#This means the given path is a folder with no subfolders and files in it.
					return 0
				elif(len(i[1]) != 0 and len(i[2]) == 0):
					#This means the path given is a folder with subfolders but no files in it.
					return FoF(i[1]) 
				elif(len(i[0]) == 0 and len(i[2]) != 0):
					#This means the path given is a folder with files but no subfolders in it.
					return FoF(i[2])
				else:
					#Work on this.
					return 1
