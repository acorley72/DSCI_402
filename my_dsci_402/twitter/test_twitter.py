from twitter_util import *
from sentiment import *

texts = read_texts("twitter_data/adele.jason")

# n = 20
# for i in range(n):
	# print(texts[i])
	
# codes = get_sentiment_codes("../util-data-files/AFINN-111.txt")
# print(codes)

trump = read_texts("twitter_data/trump.json")
hillary = read_texts("twitter_data/hillary.json")

print("\nTRUMP")	
for t in trump[:10]:
	print(t, sentiment_score(codes, t))
	
print("\nHILLARY")	
for t in hillary[:10]:
	print(t, sentiment_score(codes, t))
	
