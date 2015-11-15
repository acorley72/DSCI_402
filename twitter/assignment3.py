from twitter_util import *
from sentiment import *

stopwords= []
def fillStopwords(stopwords):
	data = open("stopwords.txt", 'rb').read().split("\r\n")
	for line in data:
		try:
			stopwords.append(line)
		except:
			print("JSON-unopenable tweet encountered")
	return stopwords
stopwords= fillStopwords(stopwords)
print(stopwords)

	
def rank_tweets(tweet_file, n):
	codes = get_sentiment_codes("../util-data-files/AFINN-111.txt")
	tweets = read_tweets(tweet_file)
	scores = {}
	total = 0
	for line in tweets:
		if "text" in line.keys():
			txt = text(line, 'text').split()
			score = 0
			non_sentiment_words = []
			for word in txt:
				total += 1
				if word[0] == "@" or word[0] == "`" or word[0] == "#" or word[0] =="&" or word =="RT" or word[0] =="!" or word[0] =="?" or(word in stopwords):
					continue
				if word in codes:
					score += codes[word]
				else:
					non_sentiment_words.append(word)
					if word  not in scores.keys():
						scores[word] = [0,1]
					else: 
						scores[word] = scores[word]
						scores[word][1] += 1
				for word in non_sentiment_words:
					scores[word][0] += score
		else:
			continue 	
	print(total)
			
	#Normalize
	for s in scores:
		scores[s] = scores[s][0] / scores[s][1]

	#Order by Value
	srt = sorted(scores.items(),key = lambda x : x[1])
	
	#print first n
	print("Unhappiest")
	for i in range(n):
		print(srt[i])
		print("\n")
	
	srt.reverse()
	print("Happiest")
	for i in range(n):
		print(srt[i])
		print("\n")	
	
rank_tweets("./twitter_data/trump.json", 10)
