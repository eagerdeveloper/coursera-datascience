import sys
import json

    #print type(tweets)
    #print tweets.keys()
    #print results
    #print line["text"]

scores = {} # initialize sentiments dictionary

term_scores = {}
term_counts = {}

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
            #print "%.04f" % sentiment_score
            #tweet_scores[tweet_text] = sentiment_score
    
    tweet_file.close()
    print_term_sentiment(term_scores)


def print_term_sentiment(term_scores):
   for key, value in term_scores.items():
    print key, "%.04f" % value

# Go through each word in the tweet and compare with existing word
# for sentiment
def calculate_sentiment_for_tweet(tweet_text):
    sentiment = 0
#    print "TWEET: ", tweet_text
    for word in tweet_text.lower().split():
	if word in scores.keys():
            sentiment += scores[word]

    if sentiment != 0:
        for word in tweet_text.lower().split():
	    if word not in scores.keys():
                if word not in term_scores.keys():
                    term_counts[word] = 1
                    term_scores[word] = sentiment
                else:
                    term_counts[word] += 1
                    term_scores[word] = float(1.0 * sentiment) / term_counts[word]

     
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
