from word_util import *
from anagram import *

#Assumes we are in the word_games directory.
words = read_words('../util-data-files/words.txt')

#Print each word 
# for word in words: 
	# print(word)

print(word_hist("ball"))
print(all_anagrams("spacecraft",words))
print(all_anagrams("live",words))

