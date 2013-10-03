import sys
import json
import string

terms = {}
total_term_occurrences = 0

def calculate_term_frequency(tweet_file):
    # 1. Read all tweets from file
    for line in tweet_file.readlines():
        tweet = json.loads(line)
    
        # 2. Go through each result and calculate term occurrences
        tweet_key = "text" 
        if tweet_key in tweet.keys(): 
            tweet_text = tweet[tweet_key].encode('utf-8')
            calculate_term_count_for_tweet(tweet_text)
    
    tweet_file.close()

    print_term_frequency()


def print_term_frequency():
    #print 'total_term_occurrences = ', total_term_occurrences
    all_terms_frequency = 1.0/total_term_occurrences
    #print 'all_terms_frequency = ', all_terms_frequency
    for k, v in dict.items(terms):
        print k, " ", "%.04f" % (v*all_terms_frequency)
        #print k, " ", v, " ", "%.04f" % (v*all_terms_frequency)

# Go through each word in the tweet and count it
def calculate_term_count_for_tweet(tweet_text):
#    print "TWEET: ", tweet_text
    global total_term_occurrences
    global terms
    for word in tweet_text.lower().split():
        exclude = set(string.punctuation)
	word = ''.join(ch for ch in word if ch not in exclude)
	if word not in terms.keys():
            terms[word] = 1
        else:
            terms[word] = terms[word] + 1

        total_term_occurrences += 1

def hw(tweet_file):
    calculate_term_frequency(tweet_file)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
