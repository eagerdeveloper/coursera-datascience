import sys
import json

    #print type(tweets)
    #print tweets.keys()
    #print results
    #print line["text"]

scores = {} # initialize sentiments dictionary

def calculate_tweet_sentiment(tweet_file):
    # initialize tweets dictionary
    tweet_scores = {}

    # 1. Read all tweets from file
    for line in tweet_file.readlines():
        tweet = json.loads(line)

    
        # 3. Go through each result and calculate sentiment
        tweet_key = "text" 
        if tweet_key in tweet.keys(): 
            tweet_text = tweet[tweet_key].encode('utf-8')
            #print "TWEET_TEXT: ", tweet_text
            sentiment_score = calculate_sentiment_for_tweet(tweet_text)
            print "%.04f" % sentiment_score
            #tweet_scores[tweet_text] = sentiment_score
    
    tweet_file.close()
    print_tweet_sentiment(tweet_scores)


def calculate_tweet_sentiment0(tweet_file):
    # 1. Read all tweets from file
    tweets = json.load(tweet_file)
    # 2. Parse out tweet results dict
    results = tweets["results"]

    # initialize tweets dictionary
    tweet_scores = {}
    
    # 3. Go through each result and calculate sentiment
    for line in results:
        tweet_text = line["text"]
        sentiment_score = calculate_sentiment_for_tweet(tweet_text)
        tweet_scores[tweet_text.encode('utf-8')] = sentiment_score
    
    tweet_file.close()
    #print_tweet_sentiment(tweet_scores)

def print_tweet_sentiment(tweet_scores):
   for v in tweet_scores.values():
    print "%.04f" % v

# Go through each word in the tweet and compare with existing word
# for sentiment
def calculate_sentiment_for_tweet(tweet_text):
    sentiment = 0
#    print "TWEET: ", tweet_text
    for word in tweet_text.lower().split():
	if word in scores.keys():
	#if word.encode('utf-8') in scores.keys():
 #           print "WORD: ", word, ", scores[word]: ", scores[word]
            sentiment += scores[word]

#    print "SENTIMENT: ", sentiment
    return sentiment

def create_sentiment_dict(sent_file):
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

#    print scores.items() # Print every (term, score) pair in the dictionary
    sent_file.close()


def hw(sent_file, tweet_file):
    create_sentiment_dict(sent_file)
    calculate_tweet_sentiment(tweet_file)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
