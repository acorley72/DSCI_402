#Read in a word list in 1-word-per-line format.
def read_words(filename):
	words = open(filename, 'r').readlines() #r means read only #readlines goes through one line at a time  
	#strip cleans text to get rid of \t \n or spaces 
	#lower changes it to a lower case
	return filter(lambda x: x != '', map(lambda y: y.strip().lower(), words))
	
#Anagram - takes a word and mixes up the letters to see if it can make another word suggested 
