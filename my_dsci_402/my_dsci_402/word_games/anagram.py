#1. build word histogram (dictionary)
def word_hist(word):
	h = {}
	for lett in word:
		if not(h.has_key(lett)):
			h[lett] = 0
		h[lett] += 1
	return h 

#find all anagrams of a word in a word list 	
def all_anagrams(word,word_list):
	wh = word_hist(word)
	anagrams = []
	for w in word_list:
		if word_hist(w) == wh:
			anagrams.append(w)
	return anagrams 
	
