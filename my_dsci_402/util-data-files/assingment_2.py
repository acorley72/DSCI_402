def read_words(filename):
	words = open(filename, 'r').readlines() #r means read only #readlines goes through one line at a time  
	#strip cleans text to get rid of \t \n or spaces 
	#lower changes it to a lower case
	return filter(lambda x: x != '', map(lambda y: y.strip().lower(), words))

word_list = read_words('../util-data-files/words.txt')

def word_breaks(word, word_list):
	list = []
	for position in range(len(word)):
		copy = word[position:]
		for substring in range(len(copy)):
			word1 = copy[0:substring]
			word2 = copy[substring:]
			if word1 in word_list and word1 not in list: 
				list.append(word1)
			if word2 in word_list and word2 not in list:
				list.append(word2)
	print(list)


