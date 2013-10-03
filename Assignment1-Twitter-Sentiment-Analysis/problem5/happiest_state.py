import sys
import json
import re

scores = {} # initialize sentiments dictionary

def calculate_tweet_sentiment(tweet_file):
    # initialize tweets dictionary
    tweet_scores = dict()
    counter = 0
    # 1. Read all tweets from file
    for line in tweet_file.readlines():
        tweet = json.loads(line)

        # 2. Verify each tweet for location, language
        city_state = get_city_state(tweet)
        if city_state:
            tweet_key = "text" 
            if tweet_key in tweet.keys(): 
                tweet_text = tweet[tweet_key].encode('utf-8')
                sentiment_score = calculate_sentiment_for_tweet(tweet_text)
                state = get_state(city_state)
                if state:
                    if state == "San Francisco":
		        break
                    counter += 1
                    if state in tweet_scores.keys():
                        tweet_scores[state] += sentiment_score
                    else:
                        tweet_scores[state] = sentiment_score
         
        if counter == 90:
            break;
    tweet_file.close()
    print_happiest_tweet(tweet_scores)

def get_state(city_state):
    if city_state.find(",") != -1:
        state = re.split(', ', city_state)
        if state[1]:
            if len(state[1]) == 2:
                #print state
                return state[1]


def get_city_state(tweet):
    #if is_English_language_in_tweet(tweet):
        city_state = get_city_state_in_tweet(tweet)
        return city_state

def get_city_state_in_tweet(tweet):
    key = "place"
    if key in tweet.keys():
        if tweet[key]:
            if tweet[key]["country"] == "United States":
                if tweet[key]["full_name"]: # refers to city and state
                    #print "place:", tweet[key]
                    return tweet[key]["full_name"]

def is_English_language_in_tweet(tweet):
    key = "lang"
    if key in tweet.keys():
        #print "lang:", tweet[key]
        if tweet[key] == "en":
            return True

def print_happiest_tweet(tweet_scores):
   #for key,value in sorted(tweet_scores.iteritems(), key=lambda (k,v): (v,k)):
   #    print key, "%.04f" % value
   import operator
   print max(tweet_scores.iteritems(), key = operator.itemgetter(1))[0]
  

# Go through each word in the tweet and compare with existing word
# for sentiment
def calculate_sentiment_for_tweet(tweet_text):
    sentiment = 0
    for word in tweet_text.lower().split():
	if word in scores.keys():
            sentiment += scores[word]
    return sentiment

def create_sentiment_dict(sent_file):
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    sent_file.close()


def hw(sent_file, tweet_file):
    create_sentiment_dict(sent_file)
    calculate_tweet_sentiment(tweet_file)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
